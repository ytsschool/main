from django.conf.urls import patterns, include, url
from main import views
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yts.views.home', name='home'),
    # url(r'^yts/', include('yts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^blog/',include('ContributionBlog.urls')),
    url(r'^cryptopage/',include('cryptopage.urls')),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
