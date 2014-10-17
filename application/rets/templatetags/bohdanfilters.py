from django import template
from django.template.defaultfilters import stringfilter
import math
import urllib
import re
import locale
from django.utils.safestring import mark_safe
register = template.Library()
locale.setlocale(locale.LC_ALL, 'en_US')


@register.filter(name='get_key')
def get_key(value, arg):
	try:
		return getattr(value,arg)
	except Exception, e:
		pass
	try:
		return math.floor(value[arg]*100)
	except Exception, e:
		pass
	return None

@register.filter(name='nicemoney', needs_autoescape=True)
def nicemoney(value, autoescape=None):
	return mark_safe('<span itemprop="priceCurrency" content="CAD">$</span><span itemprop="price">%s</span>'%locale.format("%d", value, grouping=True))

@register.filter(name="urlify")
def urlify(value):
	return urllib.quote(value)

@register.filter(name="mapsgen")
def mapsgen(addres):
	return "https://www.google.com/maps/embed/v1/place?q=%sCanada&key=AIzaSyBdpJO3FCVQ7UyWvOkRDfVpqMX-gjBmW1k"%urllib.quote("%s,%s ON, "%(addres.addr,addres.area))

@register.filter
def get_range( value ):
	return range(1,value )

@register.filter(name="interfy")
def interfy(value):
	return int(value)

@register.filter(name="titlecase")
def titlecase(value):
	return value.title().replace("-"," ")

@register.filter(name="limilength")
def limilength(value):
	goallength = 150
	if len(value) > goallength:
		limited = value[:goallength]
		split = re.split('\s+', limited)
		out = ""
		count = len(split)-1;

		while len(out) < 3 or count < 1:
			out = split[count]
			count = count - 1
		out = out.replace(',', '').replace(' ', '').replace('.', '')
		return "%s..."%(value[:limited.rfind(split[len(split)-1])-1],)
	return value
