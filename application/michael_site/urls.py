from django.conf.urls import patterns, include, url
from django.contrib import admin	
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),	
    url(r'^$', 'michael_site.views.home', name='home'),
    url(r'^sell/', 'michael_site.views.sell', name='sell'),
    url(r'^buy/', 'michael_site.views.buy', name='buy'),
    url(r'^search/', 'michael_site.views.search', name='search'),
    
    url(r'^ajaxhome', 'michael_site.views.ajaxhome', name='ajaxhome'),
    url(r'^ajaxsell/', 'michael_site.views.ajaxsell', name='ajaxsell'),
    url(r'^ajaxbuy/', 'michael_site.views.ajaxbuy', name='ajaxbuy'),
    url(r'^ajaxsearch/', 'michael_site.views.ajaxsearch', name='ajaxsearch'),

    url(r'^ajaxproperty/', 'michael_site.views.ajaxproperty', name='ajaxproperty'),
    url(r'^ajaxneighbourhood/(?P<urlneighbourhood>.*)/$', 'michael_site.views.ajaxneighbourhood', name='ajaxneighbourhood'),
    

)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )