from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import Http404  

def home(request):
	return render_to_response('about.html',{"MEDIA_URL":settings.MEDIA_URL})

def sell(request):
	return render_to_response('sell.html',{"MEDIA_URL":settings.MEDIA_URL})

def buy(request):
	return render_to_response('buy.html',{"MEDIA_URL":settings.MEDIA_URL})
	
def search(request):
	return render_to_response('search.html',{"MEDIA_URL":settings.MEDIA_URL})
