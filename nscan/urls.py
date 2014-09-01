from django.conf.urls import patterns, url
from nscan import views

urlpatterns = patterns('',
    url(r'^$', views.scan, name='scan'),
    url(r'^recursive-scan/$', views.rec_search, name='rec_search'),
    url(r'^mapify/$', views.mapify, name='mapify'),
)