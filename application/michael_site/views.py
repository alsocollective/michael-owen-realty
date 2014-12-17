from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import Http404  
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
import time
import os.path
from settings import MEDIA_URL, ALLOWED_HOSTS
from rets.views import *
from michael_site.settings import googlecred

#	returns the template needed, if it's ajax, sends ajax, else sends full html
def templateType(request):
	template = "index.html"
	if(request.is_ajax()):
		template = "ajax.html"
	return template

#	example case...
# 	emailBoutPorp({"sender":"bohdananderson@gmail.com","body":"WHY hello there!"})
def emailBoutPorp(data):
	title = "%s %s, from my website" %(data["firstname"],data["lastname"])
	message = "Message: %s From:%s%s %s %s"%(data["message"],data["firstname"],data["lastname"],data["email"],data["phone"])
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

def getCssClass(request):
	out = "desktop"
	if(request.is_tablet):
		out = "mobile tablet"
	if(request.is_phone):
		out = "mobile phone"
	return out

def getFeatured():
	return ResidentialProperty.objects.all().order_by('-featured')[:3]

def home(request):
	out = AboutPage.objects.all().order_by("created")[0]
	pageReq = request
	return render_to_response('about.html',{"pagecontent":out,"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request),"featured":getFeatured(),'pageType':getCssClass(request), 'pageTitle':pageReq})

def sell(request):	
	out = SellPage.objects.all().order_by("created")[0]	
	return render_to_response('sell.html',{"pagecontent":out,"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request),'pageType':getCssClass(request)})

def buy(request):
	out = BuyPage.objects.all().order_by("created")[0]		
	return render_to_response('buy.html',{"pagecontent":out,"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request),'pageType':getCssClass(request)})
	
def search(request):
	template = templateType(request)
	properties = ResidentialProperty.objects.all().order_by('timestamp_sql').filter(area="Toronto",pix_updt__isnull=False,s_r='Sale')[:6]
	out = {"MEDIA_URL":MEDIA_URL,'basetemplate':template,'data':properties,'filter':getPeram(),"featured":getFeatured(),'pageType':getCssClass(request)}
	out.update(csrf(request))
	out["pagecontent"] = SearchPage.objects.all().order_by("created")[0]			
	out["desscrrrippttiion"] = NeightbourHood.objects.get(slug="little-italy")

	return render_to_response('search.html',out)

def fourofour(request):
	return render_to_response('404.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html",'pageType':getCssClass(request)})
def fivehun(request):
	return render_to_response('500.html',{"MEDIA_URL":settings.MEDIA_URL,'basetemplate':"index.html",'pageType':getCssClass(request)})

def sitemap(request):
	buy = str(BuyPage.objects.all().order_by("created")[0]).split()[0].replace("/","-")
	sell = str(SellPage.objects.all().order_by("created")[0]).split()[0].replace("/","-")
	about = str(AboutPage.objects.all().order_by("created")[0]).split()[0].replace("/","-")
	search = str(SearchPage.objects.all().order_by("created")[0]).split()[0].replace("/","-")
	return render(request,'sitemap.xml',{"BuyPage":buy, "SellPage":sell, "AboutPage":about, "SearchPage":search},content_type="application/xhtml+xml")



def ajaxproperty(request):
	out = {"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html"}
	out.update(csrf(request))
	return render_to_response('property.html',out)

def ajaxneighbourhood(request, urlneighbourhood):
	try:
		out = NeightbourHood.objects.get(slug=urlneighbourhood)
		pass
	except Exception, e:
		print e
		out = {"title":"Nothing Found"}
		pass
	# out = {"title":urlneighbourhood,"content":"blah blah"}
	return render_to_response('neighbourhood.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html", "location":out})

def property(request,propertyid):
	template = templateType(request)
	properties = ResidentialProperty.objects.get(ml_num = propertyid)
	out = {"MEDIA_URL":MEDIA_URL,'basetemplate':template,'pageid':propertyid,'data':properties,'reslist':ResidentialRelations}
	out.update(csrf(request))
	# percentages = getPercentages(True)
	return render_to_response('property.html',out)

def loadallimages(request,propertyid):
	count = getAllImages(propertyid)
	data = {"request":"was a success","id":propertyid,"count":count}
	return HttpResponse(json.dumps(data), content_type='application/json')



def testView(request):
	print "=== testView ==="
	try:
		print "== loading data =="
		datain = loadData()
		print "== data loaded =="
		try:
			if(len(datain) == 0):
				return HttpResponse("data length returned was zero", content_type='application/json')			
			pass
		except Exception, e:
			return HttpResponse("data went wrong: ", content_type='application/json')
		
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
	print "|||||||||||||||||"
	for pop in request.POST:
		poporigin = pop
		print pop
		if "onlyjandd" in pop:
			kwargs["rltr__in"] = ["ROYAL LEPAGE/J & D DIVISION, BROKERAGE"]
			continue
		elif "community" in pop:
			try:
				kwargs["community__in"].append(pop[9:])		
			except Exception, e:
				print e
				kwargs["community__in"] = [pop[9:]]
				pass
			continue
		elif "notuse" in pop:
			continue
		elif "style" in pop:
			print pop[5:]
			try:
				kwargs["style__in"].append(pop[5:])		
			except Exception, e:
				print e
				kwargs["style__in"] = [pop[5:]]
				pass
			continue			
		elif "bed" in pop:
			pop = "br%s"%addminmax(pop)
		elif "bath" in pop:
			pop = "bath_tot%s"%addminmax(pop)
		elif "price" in pop:
			pop = "lp_dol%s"%addminmax(pop)

		print "bottom"
		if pop == 'csrfmiddlewaretoken' or pop == 'from':
			pass
		else :
			try:
				kwargs[pop] = int(request.POST[poporigin].replace("$","").replace(",","").replace(" ",""))
			except Exception, e:
				print e
				try:
					kwargs[pop] = float(request.POST[poporigin].replace("$","").replace(",","").replace(" ",""))
				except Exception, e:
					print e
					kwargs[pop] =request.POST[poporigin]
		print "done loop\n----------------"
	

	fromcounter = int(request.POST["from"])
	print "trying the queiry"
	properties = ResidentialProperty.objects.all().order_by('timestamp_sql').filter(**kwargs)
	# properties = [ResidentialProperty.objects.get(ml_num='E3019520')]
	print "number of properties: %d" %len(properties)
	return render_to_response('properties.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':templateType(request),'data':properties[fromcounter:(fromcounter+6)],'thiscount':fromcounter,'totalcount':len(properties)})


def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip



from datetime import datetime, timedelta
@csrf_protect
def sendemail(request):
	ip = get_client_ip(request)

	ipexists = EmailRmark.objects.filter(ipaddress = ip).order_by('-date')
	try:
		ipexists = ipexists[0]
	except Exception, e:
		ipexists = None
		pass
	now = datetime.now()

	if (ipexists == None) or (now-ipexists.date > timedelta(seconds = 30)):
		ipinstance = EmailRmark(ipaddress = ip)
		ipinstance.save()				
		emailBoutPorp(request.POST)
		return HttpResponse(json.dumps({'message':'Email Sent','status':'sent'}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'message':'Error, Please Wait Before Sending Another Email','status':'error'}), content_type='application/json')




import requests
import time
def sort(request):
	lists = ResidentialProperty.objects.all().filter(area="Toronto")
	print lists
	print "|||||||||||||||||||||||||||||||"
	print "|||||||||||||||||||||||||||||||"
	urlbase = 'https://maps.googleapis.com/maps/api/geocode/json?'
	out = ""
	counter = 0
	for el in lists:
		try:
			# out += "%s\n"%
			counter += 1
			if counter%10 == 0:
				time.sleep(1)
			

			print "given area name: %s" %el.community

			url = '%saddress=%s,+%s,+Canada'%(urlbase,el.addr.replace(" ","+"),el.area.replace(" ","+"))
			r = requests.get(url, auth=(googlecred.user,googlecred.password))
			json = r.json()['results'][0]
			try:
				out+= "%s,%s,%s\n"%(el.community,json['address_components'][2]['short_name'],el.municipality_district)
				pass	
			except Exception, e:
				print "too many calls where called at once. %s" %e
				pass	
		except Exception, e:
			print "has no community name..."
			pass			
		# for el in json['address_components']:
		# 	print el
	print "|||||||||||||||||||||||||||||||"
	print "|||||||||||||||||||||||||||||||"			


	


	return HttpResponse(out, content_type='application/json')

	out = filloutlists()
	value = getFullListOfMLS()
	sqlRemoveElements(ResidentialProperty.objects.all().filter(status="A"),value)
	return HttpResponse(out, content_type='application/json')
