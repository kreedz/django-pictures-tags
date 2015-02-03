from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from pictures_tags.models import Picture, Tag

import os


def index(request):
    pictures = Picture.objects.all().order_by('-subPath', 'filename')[:3]
    tags = Tag.objects.all()
    context = {'pictures': pictures, 'tags': tags}
    return render(request, 'pictures_tags/index.html', context)

def options(request):
    return render(request, 'pictures_tags/options.html')

def updatedb(request):
    Picture.objects.all().delete()
    denied_dir = 'cache/'
    rootdir = getattr(settings, 'MEDIA_ROOT', None)
    for root, subFolders, filenames in os.walk(rootdir, followlinks=True):
        subRoot = root[len(rootdir):]
        if subRoot: subRoot += '/'
        if subRoot[:len(denied_dir)] == denied_dir:
            continue
        for filename in filenames:
            ext = os.path.splitext(filename)[1][1:]
            if ext == 'png' or ext == 'jpg' or ext == 'gif':
                Picture.objects.get_or_create(subPath=subRoot, filename=filename)
    return HttpResponse(True)

def add_tag(request):
    created = Tag.objects.get_or_create(tag=request.GET.get('tag'))[1]
    return JsonResponse({'created': created})

def delete_tag(request):
    try:
        deleted = True
        Tag.objects.get(tag__exact=request.GET.get('tag')).delete()
    except ObjectDoesNotExist:
        deleted = False
    finally:
        response = {'deleted': deleted}
    return JsonResponse(response)
