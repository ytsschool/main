#coding=utf-8
__author__ = 'Vladimir'

from django.conf.urls import patterns,url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from ContributionBlog import views

urlpatterns = patterns('',
    url(r'^post',views.postCommitMessage,name='postCommitMessage'),
    url(r'^user_(?P<user>[^/]*)/(?P<page>[0-9]+)$',views.CommitsView.as_view(),name='userIndex'),
    url(r'^(?P<page>[0-9]+)$',views.CommitsView.as_view(),name='index'),
    #url(r'^$',RedirectView.as_view(url='ya.ru')),
)
#(\?user=(?P<user>[A-z0-9]+))?(page=(?P<page>[0 -9]+))?
#reverse('index',kwargs={'page' : '1'})