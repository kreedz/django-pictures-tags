from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from pictures_tags import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^options$', views.options, name='options'),
    url(r'^updatedb$', views.updatedb, name='updatedb'),
    url(r'^add-tag$', views.add_tag, name='add-tag'),
)
