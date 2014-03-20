from django.conf.urls import patterns, url
from advert.views import BoardListView, BoardDetailView, addit

urlpatterns = patterns('',
    url(r'^$', BoardListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BoardDetailView.as_view(), name='detail'),
)


