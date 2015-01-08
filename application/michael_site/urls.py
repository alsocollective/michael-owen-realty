from django.conf.urls import patterns, include, url
from django.contrib import admin	
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),	
    url(r'^$', 'michael_site.views.home', name='home'),
    url(r'^sell/', 'michael_site.views.sell', name='sell'),
    url(r'^buy/', 'michael_site.views.buy', name='buy'),
    url(r'^search/', 'michael_site.views.search', name='search'),
    
    # url(r'^ajaxhome', 'michael_site.views.home', name='ajaxhome'),
    # url(r'^ajaxsell/', 'michael_site.views.sell', name='ajaxsell'),
    # url(r'^ajaxbuy/', 'michael_site.views.buy', name='ajaxbuy'),
    # url(r'^ajaxsearch/', 'michael_site.views.search', name='ajaxsearch'),

    # url(r'^404/', 'michael_site.views.fourofour', name='fourofour'),
    # url(r'^500/', 'michael_site.views.fivehun', name='fivehun'),   


    url(r'^ajaxproperty/', 'michael_site.views.ajaxproperty', name='ajaxproperty'),
    url(r'^property/(?P<propertyid>.*)/$', 'michael_site.views.property', name='property'),
    url(r'^ajaxneighbourhood/(?P<urlneighbourhood>.*)/$', 'michael_site.views.ajaxneighbourhood', name='ajaxneighbourhood'),
    url(r'^newimages/(?P<propertyid>.*)/$', 'michael_site.views.loadallimages', name='loadallimages'),
    
    url(r'^proplist/', 'michael_site.views.getinitialpagedata', name='getinitialpagedata'),
    url(r'^sendemail/', 'michael_site.views.sendemail', name='sendemail'),

    url(r'^sitemap/', 'michael_site.views.sitemap', name='sitemap'),    
    url(r'^robots.txt', 'michael_site.views.robots', name='forbots'),


    url(r'^test/', 'michael_site.views.testView', name='testView'),
    # url(r'^sort/', 'michael_site.views.sort', name='sort'),    
    # url(r'^percent', 'michael_site.views.percentageofattricbutes', name='percentageofattricbutes'),

    (r'^google3b84a25d4ebf8fc9.html$', TemplateView.as_view(template_name='google3b84a25d4ebf8fc9.html')),    
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )