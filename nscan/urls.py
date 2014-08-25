from django.conf.urls import patterns, url
from nscan import views

urlpatterns = patterns('',
    url(r'^my/$', views.myjson, name='myjson'),
    url(r'^$', views.scan, name='scan'),
    #url(r'^switchscan/$', views.scan, name='scan'),
)