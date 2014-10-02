from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import Http404  
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
import librets
import time
import os.path
from settings import rets_connection, MEDIA_URL, ALLOWED_HOSTS
from rets.views import *

#	returns the template needed, if it's ajax, sends ajax, else sends full html
def templateType(request):
	template = "index.html"
	if(request.is_ajax()):
		template = "ajax.html"
	return template

#	example case...
# 	emailBoutPorp({"sender":"bohdananderson@gmail.com","body":"WHY hello there!"})
def emailBoutPorp(data):
	print "sent Message"
	title = "email from %s" %data["sender"]
	message = "Message: %s From: %s"%(data["body"],data["sender"])
	send_mail(title,message,"websitemicheal@gmail.com" ,["bohdan@alsocollective.com"], fail_silently=False)

#	load test data
def loadTestData():
	try:
		json_data = open('data.json')
		return json.load(json_data)
	except Exception, e:
		print "load faied ", e
		return {"no":"data"}

	# for column in columns:
	# 		print column + ": " + results.GetString(column)

def getFeatured():
	return ResidentialProperty.objects.all().order_by('-featured')[:3]

def home(request):
	
	return render_to_response('about.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request),"featured":getFeatured()})

def sell(request):	
	return render_to_response('sell.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request)})

def buy(request):
	return render_to_response('buy.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request)})
	
def search(request):
	template = templateType(request)
	properties = ResidentialProperty.objects.all().order_by('timestamp_sql').filter(area="Toronto",pix_updt__isnull=False,s_r='Sale')[:9]

	out = {"MEDIA_URL":MEDIA_URL,'basetemplate':template,'data':properties,'filter':getPeram(),"featured":getFeatured()}
	out.update(csrf(request))	
	return render_to_response('search.html',out)


def ajaxproperty(request):
	return render_to_response('property.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxneighbourhood(request, urlneighbourhood):
	out = {"title":urlneighbourhood,"content":"blah blah"}
	return render_to_response('neighbourhood.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html", "location":out})

@csrf_exempt
def property(request,propertyid):
	template = templateType(request)
	properties = ResidentialProperty.objects.get(ml_num = propertyid)
	# percentages = getPercentages(True)
	return render_to_response('property.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':template,'pageid':propertyid,'data':properties,'reslist':ResidentialRelations})

def loadallimages(request,propertyid):
	count = getAllImages(propertyid)
	data = {"request":"was a success","id":propertyid,"count":count}
	return HttpResponse(json.dumps(data), content_type='application/json')



def testView(request):
	try:
		datain = loadData()
		print "loaded data: %d,\nbout to itterate" %len(datain)
		filteroptions = FilterOptions.objects.all()
		for data in datain:	
			possibleobject = ResidentialProperty.objects.filter(ml_num=data["MLS"])
			if(possibleobject.exists()):
				filteroptions = updateResidentialPropertyAttributes(data,possibleobject[0],filteroptions)			
			else:
				filteroptions = saveResidentialPropertyAttributes(data,filteroptions)
		
		value = getFullListOfMLS()
		sqlRemoveElements(ResidentialProperty.objects.all().filter(status="A"),value)
		filloutlists()# checkFilters()
		return HttpResponse("update the treb with %d entreis"%len(datain), content_type='application/json')	

	except Exception, e:
		print "Could not acceses the TREB DB"
		print e
		return HttpResponse("Could not acceses the TREB DB", content_type='application/json')	


def percentageofattricbutes(request):
	smalllist = getPercentages(False)
	return render_to_response('viz.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request),"data":json.dumps(smalllist)})
	return HttpResponse(json.dumps(smalllist), content_type='application/json')

def addminmax(value):
	if "upper" in value:
		return "__lt"
	elif "lower" in value:
		return "__gt"
	return ""

@csrf_protect
def getinitialpagedata(request):
	kwargs = {
		'area':"Toronto",
		'pix_updt__isnull':False,
		's_r':'Sale',
		'status':'A'
	}
	for pop in request.POST:
		poporigin = pop
		if "bed" in pop:
			pop = "br%s"%addminmax(pop)
		elif "bath" in pop:
			pop = "bath_tot%s"%addminmax(pop)
		elif "price" in pop:
			pop = "lp_dol%s"%addminmax(pop)

		if pop == 'csrfmiddlewaretoken' or pop == 'from':
			pass
		else :
			try:
				kwargs[pop] = int(request.POST[poporigin].replace("$","").replace(",","").replace(" ",""))
			except Exception, e:
				try:
					kwargs[pop] = float(request.POST[poporigin].replace("$","").replace(",","").replace(" ",""))
				except Exception, e:
					kwargs[pop] =request.POST[poporigin]	
	
	fromcounter = int(request.POST["from"])
	# print kwargs
	properties = ResidentialProperty.objects.all().order_by('timestamp_sql').filter(**kwargs)
	# print properties

	return render_to_response('properties.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request),'data':properties[fromcounter:(fromcounter+12)],'totalcount':len(properties)})


@csrf_protect
def sendemail(request):
	for pop in request.POST:
		print pop
	return HttpResponse("yesssssppp", content_type='application/json')
	emailBoutPorp("DATA")

def sort(request):
	out = filloutlists()
	value = getFullListOfMLS()
	sqlRemoveElements(ResidentialProperty.objects.all().filter(status="A"),value)
	return HttpResponse(out, content_type='application/json')


