from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import Http404  

def home(request):
	return render_to_response('about.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})

def sell(request):
	return render_to_response('sell.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})

def buy(request):
	return render_to_response('buy.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})
	
def search(request):
	return render_to_response('search.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})

def ajaxhome(request):
	return render_to_response('about.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxsell(request):
	return render_to_response('sell.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxbuy(request):
	return render_to_response('buy.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxsearch(request):
	return render_to_response('search.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxproperty(request):
	return render_to_response('property.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxneighbourhood(request):
	return render_to_response('neighbourhood.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"ajax.html"})

