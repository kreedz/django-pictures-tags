from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pictures_tags.models import Picture

import os


def index(request):
    pictures = Picture.objects.all().order_by('-subPath', 'filename')[:3]
    context = {'pictures': pictures}
    return render(request, 'pictures_tags/index.html', context)

def options(request):
    return render(request, 'pictures_tags/options.html')

def updatedb(request):
    outtest = ''
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
                outtest += subRoot + '\n'
                #outtest += os.path.join(rootdir, subRoot, filename + '\n')
                Picture.objects.get_or_create(subPath=subRoot, filename=filename)
    return HttpResponse(outtest)
