from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import Http404  

def templateType(request):
	template = "index.html"
	if(request.is_ajax()):
		template = "ajax.html"
	return template

def home(request):
	return render_to_response('about.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})

def sell(request):
	return render_to_response('sell.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})

def buy(request):
	return render_to_response('buy.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})
	
def search(request):
	return render_to_response('search.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})

def fourofour(request):
	return render_to_response('404.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})
def fivehun(request):
	return render_to_response('500.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html"})


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

def ajaxneighbourhood(request, urlneighbourhood):
	out = {"title":urlneighbourhood,"content":"blah blah"}
	return render_to_response('neighbourhood.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"ajax.html", "location":out})

def property(request,propertyid):
	print propertyid
	template = templateType(request)
	return render_to_response('property.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':template,'pageid':propertyid})

