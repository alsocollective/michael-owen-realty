from django.conf.urls import patterns, include, url
from django.contrib import admin	
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),	
    url(r'^$', 'michael_site.views.home', name='home'),
    url(r'^sell/', 'michael_site.views.sell', name='home'),
	url(r'^buy/', 'michael_site.views.buy', name='home'),
	url(r'^search/', 'michael_site.views.search', name='home'),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )