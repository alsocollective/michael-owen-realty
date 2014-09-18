from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import Http404  
from django.core.mail import send_mail
import json
import librets
from rets.models import *
import time
import os.path
from datetime import datetime, timedelta
from settings import rets_connection, MEDIA_URL

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

def home(request):
	return render_to_response('about.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"index.html"})

def sell(request):	
	return render_to_response('sell.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"index.html"})

def buy(request):
	return render_to_response('buy.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"index.html"})
	
def search(request):
	return render_to_response('search.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"index.html"})

def ajaxhome(request):
	return render_to_response('about.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxsell(request):
	return render_to_response('sell.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxbuy(request):
	return render_to_response('buy.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxsearch(request):
	return render_to_response('search.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxproperty(request):
	return render_to_response('property.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html"})

def ajaxneighbourhood(request, urlneighbourhood):
	out = {"title":urlneighbourhood,"content":"blah blah"}
	return render_to_response('neighbourhood.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':"ajax.html", "location":out})

def property(request,propertyid):
	template = templateType(request)
	return render_to_response('property.html',{"MEDIA_URL":MEDIA_URL,'basetemplate':template,'pageid':propertyid})

from rets.relat import ResidentialRelations

def correctkey(badkey):
	mystring = badkey

	try:
		goodkey = ResidentialRelations[mystring]
		return goodkey
	except Exception, e:
		print "was a bad key:"
		return badkey








def dump_all_classes(metadata, resource):
	resource_name = resource.GetResourceID()
	for aClass in metadata.GetAllClasses(resource_name):
		if(aClass.GetClassName() == 'ResidentialProperty'):
			print "Resource name: " + resource_name + " [" + resource.GetStandardName() + "]"
			print "Class name: " + aClass.GetClassName() + " ["  + aClass.GetStandardName() + "]"
			dump_all_tables(metadata, aClass)
			print	
def dump_all_tables(metadata, aClass):
	for table in metadata.GetAllTables(aClass):
		print "'%s':{'type':'%d', 'persion':'%s', 'units':'%s', 'systemName':'%s', 'standardName':'%s'}," %(table.GetSystemName(),table.GetDataType(),table.GetPrecision(),table.GetUnits(),table.GetSystemName(),table.GetStandardName())
def printoutbasics(session):
	metadata = session.GetMetadata()
	systemdata = metadata.GetSystem()

	print "System ID: " + systemdata.GetSystemID()
	print "Description: " + systemdata.GetSystemDescription()
	print "Comments: " + systemdata.GetComments()

	for attribute in systemdata.GetAttributeNames():
		print "%s ||| %s" %(attribute, systemdata.GetStringAttribute(attribute))

	# print "|||||||||||||||||||||"
	# for resource in metadata.GetAllResources():
	# 	dump_all_classes(metadata, resource)



def loadData():
	session = librets.RetsSession(rets_connection.login_url)
	if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
		print "Error logging in"
	else:
		lastHourDateTime = datetime.today() - timedelta(hours = 0.5)
		lastHourDateTime = lastHourDateTime.strftime('%Y-%m-%dT%H:%M:%S')
		request = session.CreateSearchRequest( "Property", "ResidentialProperty", "(TimestampSql=%s+)"%(lastHourDateTime,))
		request.SetStandardNames(True)
		request.SetSelect("")
		request.SetLimit(0)
		request.SetOffset(1)	
		request.SetFormatType(librets.SearchRequest.COMPACT_DECODED)
		request.SetCountType(librets.SearchRequest.RECORD_COUNT_AND_RESULTS)	
		results = session.Search(request)		
		# print "Record count: " + `results.GetCount()`
		columns = results.GetColumns()
		file_ = open('data.json', 'w')
		data = []
		while results.HasNext():
			out = {}
			for column in columns:
				if(column == "MLS"):
					getfirstimage(results.GetString(column))
				out[column] = results.GetString(column)
			data.append(out)
		return data
	session.Logout();



def getfirstimage(imageid):
	if(os.path.isfile("static/images/%s-1.jpg"%imageid)):
		print "image already loaded"
		return "image already exists"
	session = librets.RetsSession(rets_connection.login_url)
	if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
		print "Error logging in"
	else:
		# printoutbasics(session)
		request = librets.GetObjectRequest("Property", "Photo")
		request.AddAllObjects(imageid)
		response = session.GetObject(request)
		object_descriptor = response.NextObject()
		object_key = object_descriptor.GetObjectKey()
		object_id = object_descriptor.GetObjectId()
		# content_type = object_descriptor.GetContentType()
		# description = object_descriptor.GetDescription()
		output_file_name = object_key + "-" + str(object_id) + ".jpg"
		file = open("static/images/%s" %output_file_name, 'wb')
		file.write(object_descriptor.GetDataAsString())
		file.close()
		return "Got first image"
	return "Failed to load images"
	session.Logout();

def getAllImages(imageid):
	session = librets.RetsSession(rets_connection.login_url)
	if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
		print "Error logging in"
	else:
		request = librets.GetObjectRequest("Property", "Photo")
		request.AddAllObjects(imageid)
		response = session.GetObject(request)
		object_descriptor = response.NextObject()
		while (object_descriptor != None):
			object_key = object_descriptor.GetObjectKey()
			object_id = object_descriptor.GetObjectId()
			# content_type = object_descriptor.GetContentType()
			# description = object_descriptor.GetDescription()
			output_file_name = object_key + "-" + str(object_id) + ".jpg"
			file = open("static/images/%s" %output_file_name, 'wb')
			file.write(object_descriptor.GetDataAsString())
			file.close()
			print object_id
			object_descriptor = response.NextObject()
		return "Got all images"
	return "Failed to load images"
	session.Logout();	

# print changetoactual("someword")
	# print changetoactual("234")
	# print changetoactual("2.34")
	# print changetoactual("2013-01-09 05:31:58")
def changetoactual(valin):
	try:
		digit = int(valin)
		return digit
	except Exception, e:
		pass

	try:
		digit = float(valin)
		return digit		
	except Exception, e:
		pass

	try:
		 timestamp = time.mktime(time.strptime(valin,'%Y-%m-%d %H:%M:%S'))
		 return timestamp
	except Exception, e:
		pass

	if(valin == ""):
		return None

	return valin
def saveResidentialPropertyAttributes(data):
	print "creating: %s" %data["MLS"]	
	prop = ResidentialProperty()		
	for key in data:		
		attr = correctkey(key)
		if hasattr(prop, attr):
			val = changetoactual(data[key])
			if(val):
				setattr(prop, attr, val)
	prop.save()	
def updateResidentialPropertyAttributes(data,dbinstance):
	print "updating: %s" %data["MLS"]
	for key in data:		
		attr = correctkey(key)
		if hasattr(dbinstance, attr):
			val = changetoactual(data[key])
			if(val):
				setattr(dbinstance, attr, val)
	dbinstance.save()	


def testView(request):

	# N3010326
	# res = getfirstimage('X3022277')
	# res = getAllImages('E3020561')
	
	# res = "yep"
	# loadData()

	# data = loadData();
	# for key in data[0]:
	# 	print key

	# res = "nothing"

	# return HttpResponse(res, content_type='application/json')



	try:
		datain = loadData()
		# to_json = loadTestData()
		for data in datain:	
			possibleobject = ResidentialProperty.objects.filter(ml_num=data["MLS"])
			if(possibleobject.exists()):
				updateResidentialPropertyAttributes(data,possibleobject[0])			
			else:
				saveResidentialPropertyAttributes(data)
		return HttpResponse("update the treb with %d entreis"%len(datain), content_type='application/json')	

	except Exception, e:
		print "Could not acceses the TREB DB"
		print e
		return HttpResponse("Could not acceses the TREB DB", content_type='application/json')	






