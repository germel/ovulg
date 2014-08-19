from django.conf.urls import patterns, include, url
from nscan import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.scan, name='scan'),
    url(r'^switchscan/$', views.scan, name='scan'),
)