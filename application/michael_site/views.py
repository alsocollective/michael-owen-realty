from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import Http404  

def home(request):
	return render_to_response('about.html',{"MEDIA_URL":settings.MEDIA_URL})
