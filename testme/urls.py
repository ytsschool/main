#-*- encoding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('testme.views',
    url(r'^/?$', 'main', name='testme.main'),
    url(r'^file-manager/?$', 'file_manager', name='file_manager'),
    url(r'^delete-file/(?P<pk>\d+)/?$', 'delete_file', name='delete_file'),
    url(r'^download-file/(?P<pk>\d+)/?$', 'download_file', name='download_file'),
    url(r'^report-bug/?$', 'report_bug', name='report_bug'),
    url(r'^bugs/?$', 'bugs', name='bugs'),
)