from django.conf.urls import patterns, url

from cryptopage import views

urlpatterns = patterns('',
	# ex: /cryptopage/
	url(r'^$', views.index, name='index'),
	# ex: /cryptopage/main/
	url(r'main/$', views.main, name='main'),
	# ex: /cryptopage/main/check
	url(r'main/check/$', views.check, name='check'),
)