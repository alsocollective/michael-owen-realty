from django import template
from django.template.defaultfilters import stringfilter
import math
import urllib
register = template.Library()


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

@register.filter(name='nicemoney')
def nicemoney(value):
	return '${:,.0f}'.format(value)

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