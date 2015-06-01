# most important thing ever... for rets
# http://www.dis.com/NAR/libRETS_Dev_Guide.html

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import Http404  
from django.core.mail import send_mail
from datetime import datetime, timedelta
from rets.relat import ResidentialRelations, ResidentialRelations_rev
from django.template.defaultfilters import slugify
from rets.models import *
import thread, json, librets, time, os.path, re, logging
from michael_site.settings import rets_connection,MEDIA_ROOT
from itertools import chain


logger = logging.getLogger(__name__)

#	example case...
# 	emailBoutPorp({"sender":"bohdananderson@gmail.com","body":"WHY hello there!"})
def emailBoutPorp(data):
	print "sent Message"
	title = "email from %s" %data["sender"]
	message = "Message: %s From: %s"%(data["body"],data["sender"])
	send_mail(title,message,"websitemicheal@gmail.com" ,["michaelowenrealestate@gmail.com"], fail_silently=False)
# Create your views here.








def correctkey(badkey):
	mystring = badkey
	try:
		goodkey = ResidentialRelations[mystring]
		return goodkey
	except Exception, e:
		print "was a bad key:"
		return badkey
def badkey(badkey):	
	mystring = badkey
	try:
		goodkey = ResidentialRelations_rev[mystring]
		return goodkey
	except Exception, e:
		print "was a bad key:"
		return badkey






def dump_all_lookup_types(metadata, lookup):
	for lookup_type in metadata.GetAllLookupTypes(lookup):
		print "Lookup value: " + lookup_type.GetValue() + " (" + lookup_type.GetShortValue() + ", " + lookup_type.GetLongValue() + ")"
def dump_all_lookups(metadata, resource):
	resource_name = resource.GetResourceID()
	for lookup in metadata.GetAllLookups(resource_name):
		print "Resource name: " + resource_name + " [" + resource.GetStandardName() + "]"
		print "Lookup name: " + lookup.GetLookupName() + " ("  + lookup.GetVisibleName() + ")"
		dump_all_lookup_types(metadata, lookup)
		print

def dump_all_classes(metadata, resource):
	resource_name = resource.GetResourceID()
	for aClass in metadata.GetAllClasses(resource_name):
		print "Resource name: " + resource_name + " [" + resource.GetStandardName() + "]"
		print "Class name: " + aClass.GetClassName() + " ["  + aClass.GetStandardName() + "]"
	dump_all_tables(metadata, aClass)
	print
	return False	
	resource_name = resource.GetResourceID()
	for aClass in metadata.GetAllClasses(resource_name):
		if(aClass.GetClassName() == 'ResidentialProperty'):
			print "Resource name: " + resource_name + " [" + resource.GetStandardName() + "]"
			print "Class name: " + aClass.GetClassName() + " ["  + aClass.GetStandardName() + "]"
			dump_all_tables(metadata, aClass)
			print	
def dump_all_tables(metadata, aClass):
	for table in metadata.GetAllTables(aClass):
		print "Table name: " + table.GetSystemName()  + " [" + table.GetStandardName() + "]"

	# for table in metadata.GetAllTables(aClass):
	# 	print "'%s':{'type':'%d', 'persion':'%s', 'units':'%s', 'systemName':'%s', 'standardName':'%s'}," %(table.GetSystemName(),table.GetDataType(),table.GetPrecision(),table.GetUnits(),table.GetSystemName(),table.GetStandardName())
def printoutbasics(session):
	metadata = session.GetMetadata()
	systemdata = metadata.GetSystem()

	print "System ID: " + systemdata.GetSystemID()
	print "Description: " + systemdata.GetSystemDescription()
	print "Comments: " + systemdata.GetComments()

	for attribute in systemdata.GetAttributeNames():
		print "%s ||| %s" %(attribute, systemdata.GetStringAttribute(attribute))

	print "|||||||||||||||||||||"
	for resource in metadata.GetAllResources():
		dump_all_classes(metadata, resource)

import subprocess
def loadData():
	try:
		session = librets.RetsSession(rets_connection.login_url)
		print "connected to librets"
		# session.SetHttpLogName("log.1.txt");
		print session.Login(rets_connection.user_id, rets_connection.passwd)
		if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
			print "Error logging in"
		else:
			print "connection"
			lastHourDateTime = datetime.today() - timedelta(hours = 24)
			lastHourDateTime = lastHourDateTime.strftime('%Y-%m-%dT%H:%M:%S')
			print "making request"
			request = session.CreateSearchRequest( "Property", "ResidentialProperty", "(TimestampSql=%s+)"%(lastHourDateTime,))
			request.SetStandardNames(True)
			request.SetSelect("")
			request.SetLimit(0)
			request.SetOffset(1)	
			request.SetFormatType(librets.SearchRequest.COMPACT_DECODED)
			request.SetCountType(librets.SearchRequest.RECORD_COUNT_AND_RESULTS)	
			print "sending request"
			results = session.Search(request)		
			# print "Record count: " + `results.GetCount()`
			columns = results.GetColumns()
			# file_ = open('data.json', 'w')
			print "going through all the results"			
			data = []
			imagelist = []
			while results.HasNext():
				out = {}				
				if(results.GetString("Area")=="Toronto" and results.GetString("SaleLease")=="Sale"):
					for column in columns:
						out[column] = results.GetString(column)						
						if(column == "MLS"):
							imagelist.append(results.GetString(column))
					data.append(out)

			print "loading images"			
			for mls in imagelist:
				# thread.start_new_thread(getfirstimage, (mls,))
				# getfirstimage(mls)
				pass
			print "returning the data"
			session.Logout()		
			return data
		session.Logout()
		return [];
	except Exception, e:
		return [];
		# return []HttpResponse("Could not acceses the TREB DB in some way", content_type='application/json')	


# if(results.GetString("Area") == "Toronto"):
# 	imagelist.append(results.GetString("MLS")
# 	for column in columns:
# 		out[column] = results.GetString(column)
# 	data.append(out)

def getFullListOfMLS():
	session = librets.RetsSession(rets_connection.login_url)

	# session.SetHttpLogName("log.txt");

	if (not session.Login(rets_connection.user_id_photo, rets_connection.passwd)):
		print "Error logging in"
	else:
		# printoutbasics(session)
		# return False
		request = session.CreateSearchRequest( "Property", "ResidentialProperty", "(Status=A)")
		request.SetStandardNames(True)
		request.SetSelect("")
		request.SetLimit(0)
		request.SetOffset(1)	
		request.SetFormatType(librets.SearchRequest.COMPACT_DECODED)
		request.SetCountType(librets.SearchRequest.RECORD_COUNT_AND_RESULTS)
		try:
			results = session.Search(request)	

			print "Record count: " + `results.GetCount()`
			columns = results.GetColumns()

			listOFAll = []
			while results.HasNext():
				for column in columns:
					if(column == "MLS"):
						listOFAll.append(results.GetString(column))
			session.Logout();
			return listOFAll
		except Exception, e:
			print "Result failed"
			pass
			

	session.Logout();

def SingleUpdate():
	print "doing a full pull from the server"
	session = librets.RetsSession(rets_connection.login_url)

	# session.SetHttpLogName("log.txt");

	if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
		print "Error logging in"
	else:
		# printoutbasics(session)
		# return False
		request = session.CreateSearchRequest( "Property", "ResidentialProperty", "(Status=A)")
		request.SetStandardNames(True)
		request.SetSelect("")
		request.SetLimit(0)
		request.SetOffset(1)	
		request.SetFormatType(librets.SearchRequest.COMPACT_DECODED)
		request.SetCountType(librets.SearchRequest.RECORD_COUNT_AND_RESULTS)
		results = session.Search(request)	

		print "Record count: " + `results.GetCount()`
		columns = results.GetColumns()

		datain = []
		imagelist = []
		while results.HasNext():
			out = {}				
			if(results.GetString("Area")=="Toronto" and results.GetString("SaleLease")=="Sale"):
				for column in columns:
					out[column] = results.GetString(column)						
					if(column == "MLS"):
						imagelist.append(results.GetString(column))
				datain.append(out)

		print "loading images"			
		for mls in imagelist:
			# thread.start_new_thread(getfirstimage, (mls,))
			getfirstimage(mls)
			pass
		print "returning the data"
		session.Logout()		


		print "got something"
		filteroptions = FilterOptions.objects.all()
		for data in datain:	
			possibleobject = ResidentialProperty.objects.filter(ml_num=data["MLS"])
			if(possibleobject.exists()):
				filteroptions = updateResidentialPropertyAttributes(data,possibleobject[0],filteroptions)			
			else:
				filteroptions = saveResidentialPropertyAttributes(data,filteroptions)

		return data


def getfirstimage(imageid):
	try:	
		if(os.path.isfile("%simages/%s-1.jpg"%(MEDIA_ROOT,imageid))):
			print "image already loaded"
			return "image already exists"
		print "new image %s" %imageid
		session = librets.RetsSession(rets_connection.login_url)
		if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
			print "Error logging in"
		else:
			print "\tloading"		
			# printoutbasics(session)
			request = librets.GetObjectRequest("Property", "Photo")
			request.AddAllObjects(imageid)
			response = session.GetObject(request)
			object_descriptor = response.NextObject()
			if(object_descriptor != None):
				object_key = object_descriptor.GetObjectKey()
				object_id = object_descriptor.GetObjectId()
				# content_type = object_descriptor.GetContentType()
				# description = object_descriptor.GetDescription()
				output_file_name = object_key + "-" + str(object_id) + ".jpg"
				file = open("%simages/%s" %(MEDIA_ROOT,output_file_name), 'wb')
				file.write(object_descriptor.GetDataAsString())
				file.close()
				print "\tloaded"
			else:
				print "no image to be loaded"
				prop = ResidentialProperty(ml_num=imageid,getfirstimage=False)
				prop.save()
			return "Got first image"
		return "Failed to load images"
		session.Logout();
	except Exception, e:
		print "failed"
		return "Failed to load Image, this post might not have an image..."
		pass






def getfirstimageNoRefresh(session,imageid):
	if(os.path.isfile("%simages/%s-1.jpg"%(MEDIA_ROOT,imageid))):
			print "image already loaded"
			return "image already exists"
	try:
		print "new image %s" %imageid
		request = librets.GetObjectRequest("Property", "Photo")
		request.AddAllObjects(imageid)
		response = session.GetObject(request)
		object_descriptor = response.NextObject()
		if(object_descriptor != None):
			object_key = object_descriptor.GetObjectKey()
			object_id = object_descriptor.GetObjectId()
			output_file_name = object_key + "-" + str(object_id) + ".jpg"
			file = open("%simages/%s" %(MEDIA_ROOT,output_file_name), 'wb')
			file.write(object_descriptor.GetDataAsString())
			file.close()
			print "\tloaded"
		else:
			print "no image to be loaded"
			prop = ResidentialProperty(ml_num=imageid,getfirstimage=False)
			prop.save()
		return "Got first image"
	except Exception, e:
		print "failed"
		print e
		pass

def  getAllImagesNoRefresh(session,imageid):
	print "load images for: %s"%imageid
	imageid = imageid
	imageid = imageid.encode('ascii', "ignore")
	# try:
	# 	prop = CondoProperty.objects.get(MLS = imageid)
	# except Exception, e:
	# 	prop = ResidentialProperty.objects.get(ml_num=imageid)
	
	try:
		request = librets.GetObjectRequest("Property", "Photo")
		request.AddAllObjects(imageid)
		response = session.GetObject(request)
		object_descriptor = response.NextObject()
		count = 0
		while (object_descriptor != None):
			object_key = object_descriptor.GetObjectKey()
			object_id = object_descriptor.GetObjectId()
			output_file_name = object_key + "-" + str(object_id) + ".jpg"
			file = open("%simages/%s" %(MEDIA_ROOT,output_file_name), 'wb')
			file.write(object_descriptor.GetDataAsString())
			file.close()
			return "Got first %s"%imageid
			# print count
			# object_descriptor = response.NextObject()
		# prop.numofphotos = count
		# prop.save()
	except Exception, e:
		print "failed to download %s"%imageid
		print e
		return False	
	return count


def getAllImages(imageid):
	print "load images for: %s"%imageid
	imageid = imageid
	imageid = imageid.encode('ascii', "ignore")
	try:
		prop = CondoProperty.objects.get(MLS = imageid)
	except Exception, e:
		prop = ResidentialProperty.objects.get(ml_num=imageid)
	
	session = librets.RetsSession(rets_connection.login_url)
	if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
		print "Error logging in"
	else:
		print "\tloading"
		request = librets.GetObjectRequest("Property", "Photo")

		request.AddAllObjects(imageid)
		response = session.GetObject(request)
		object_descriptor = response.NextObject()
		count = 0
		while (object_descriptor != None):
			object_key = object_descriptor.GetObjectKey()
			object_id = object_descriptor.GetObjectId()
			# content_type = object_descriptor.GetContentType()
			# description = object_descriptor.GetDescription()
			output_file_name = object_key + "-" + str(object_id) + ".jpg"
			file = open("%simages/%s" %(MEDIA_ROOT,output_file_name), 'wb')
			file.write(object_descriptor.GetDataAsString())
			file.close()
			count += 1;
			print count
			object_descriptor = response.NextObject()
		prop.numofphotos = count
		prop.save()
		return count
	return 0
	session.Logout();	


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
def saveResidentialPropertyAttributes(data,filteroptions):
	print "creating: %s" %data["MLS"]	
	prop = ResidentialProperty()		
	for key in data:		
		attr = correctkey(key)
		if hasattr(prop, attr):
			val = changetoactual(data[key])
			if(val):
				if attr is "style":
					setattr(prop, attr, cattegoriesStyle(val))
				elif attr is "community":
					setattr(prop, attr,slugify(val))
				else:
					setattr(prop, attr, val)
	prop.save()	
	return filteroptions

def cattegoriesStyle(styleIn):
	styleIn = styleIn.lower()
	if "unga" in styleIn:
		return "bungalow"
	if "sidesplit" in styleIn:
		return "sidesplit"
	if "backsplit" in styleIn:
		return "backsplit"		
	return styleIn

def updateResidentialPropertyAttributes(data,dbinstance,filteroptions):
	print "updating: %s" %data["MLS"]
	for key in data:		
		attr = correctkey(key)
		if hasattr(dbinstance, attr):
			val = changetoactual(data[key])
			if(val):
				if attr is "style":
					setattr(dbinstance, attr, cattegoriesStyle(val))
				elif attr is "community":
					setattr(dbinstance, attr,slugify(val))
				else:
					setattr(dbinstance, attr, val)				
	dbinstance.save()	
	return filteroptions

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def sqlRemoveElements(quiery,elementstoremove):
	sold = 0
	for index,el in enumerate(quiery):
		if el.ml_num in elementstoremove:
			# quiery[index].status = "A"
			# quiery[index].save()
			pass
		else:
			quiery[index].status = "S"
			quiery[index].save()
			++sold
	print "sold: %d"%sold
	return quiery



def getPercentages(nosort):
	properties = ResidentialProperty.objects.all()
	listofFieldNames = ResidentialProperty._meta.get_all_field_names()
	dicCounter = {'total':len(properties)}
	for field in listofFieldNames:
		dicCounter[field] = 0

	for prop in properties:
		for field in listofFieldNames:
			value =  getattr(prop,field)
			if(value):
				dicCounter[field] += 1

	for field in listofFieldNames:
		dicCounter[field] = float(dicCounter[field])/dicCounter["total"]

	smalllist = []
	for field in listofFieldNames:
		if dicCounter[field] > 0.1:
			smalllist.append({"id":badkey(field),"value":dicCounter[field]})
	smalllist = sorted(smalllist, key=lambda k: k['value'], reverse=True)	
	if(nosort):
		return dicCounter
	return smalllist

def replaceWithZero(valuein):
	if not valuein:
		valuein = 0;
	return valuein

def actualward(valuein):
	if "W" in valuein:
		return "west"
	elif "C" in valuein:
		digit = int(re.search(r'\d+', valuein).group())
		if(digit in [3,4,6,7,10,12,13,14,15]):
			return "centre-north"
		else:
			return "centre"
	else:
		return "east"

def filloutlists():
	FilterOptions.objects.all().delete()
	minmax.objects.all().delete()
	items = listitem.objects.all()
	Area.objects.all().delete()		
	for item in items:
		item.delete()

	style = ResidentialProperty.objects.order_by('style').filter(status="A").values('style').distinct()
	type_own1_out = ResidentialProperty.objects.order_by('type_own1_out').filter(status="A").values('type_own1_out').distinct()
	br = ResidentialProperty.objects.order_by('br').filter(status="A").values('br').distinct()
	bath_tot = ResidentialProperty.objects.order_by('bath_tot').filter(status="A").values('bath_tot').distinct()
	gar_spaces = ResidentialProperty.objects.order_by('gar_spaces').filter(status="A").values('gar_spaces').distinct()
	area = ResidentialProperty.objects.order_by('area').values('area').filter(status="A").distinct()
	style = ResidentialProperty.objects.order_by('style').values('style').filter(status="A").distinct()
	type_own1_out = ResidentialProperty.objects.order_by('type_own1_out').filter(status="A").values('type_own1_out').distinct()
	gar_type = ResidentialProperty.objects.order_by('gar_type').filter(status="A").values('gar_type').distinct()

	brminmax = minmax(num_min=replaceWithZero(br[0]['br']),num_max=br[len(br)-1]['br'])
	brminmax.save()
	bath_totmax = minmax(num_min=replaceWithZero(bath_tot[0]['bath_tot']),num_max=bath_tot[len(bath_tot)-1]['bath_tot'])
	bath_totmax.save()
	gar_spacesmax = minmax(num_min=replaceWithZero(gar_spaces[0]['gar_spaces']),num_max=gar_spaces[len(gar_spaces)-1]['gar_spaces'])
	gar_spacesmax.save()

	myFilter = FilterOptions(br=brminmax, bath_tot=bath_totmax, gar_spaces=gar_spacesmax)
	myFilter.save()

	for sty in style:
		if len(sty['style']) > 1:
			item = listitem(text=sty['style'])
			item.save()
			myFilter.style.add(item)
	for sty in type_own1_out:
		if len(sty['type_own1_out']) > 1:
			item = listitem(text=sty['type_own1_out'])
			item.save()			
			myFilter.type_own1_out.add(item)
	for sty in gar_type:
		if len(sty['gar_type']) > 1 and sty['gar_type'] != "None":
			item = listitem(text=sty['gar_type'])
			item.save()			
			myFilter.gar_type.add(item)

	communities = ResidentialProperty.objects.filter(area='Toronto',s_r="Sale",status="A").values('community','municipality_district').distinct()
	Comcomm = CondoProperty.objects.filter(Area="Toronto",SaleLease="Sale",Status="A").values('Community','MunicipalityDistrict').distinct()
	# communities = list(chain(communities,Comcomm))
	wards = ResidentialProperty.objects.filter(area='Toronto',s_r="Sale",status="A").values('municipality_district').distinct()
	newArea = Area(text="torontoCon")
	newArea.save()

	warddic = {
		'west':'',
		'east':'',
		'centre':'',
		'centre-north':''
	}
	
	for ward in warddic:
		warddic[ward] = Area(text=ward,ward=True)
		warddic[ward].save()

	for com in communities:
		unique_housingtypes = ResidentialProperty.objects.filter(community=com['community'],s_r="Sale",status="A").values('style').distinct()#.values('area').filter(status="A").distinct()
		housetypesString = ""
		for ht in unique_housingtypes:
			stringToAdd = (re.sub('[-]','',slugify(ht["style"])))
			if "storey" in stringToAdd:
				stringToAdd = "storey" + stringToAdd[:-6]
			housetypesString += (" "+stringToAdd)
		li = listitem(text=com['community'],subText=housetypesString)
		li.save()
		warddic[actualward(com['municipality_district'])].community.add(li)

	for com in Comcomm:
		unique_housingtypes = CondoProperty.objects.filter(Community=com['Community'],SaleLease="Sale",Status="A").values('Style').distinct()#.values('area').filter(status="A").distinct()
		housetypesString = ""
		for ht in unique_housingtypes:
			stringToAdd = (re.sub('[-]','',slugify(ht["Style"])))
			if "storey" in stringToAdd:
				stringToAdd = "storey" + stringToAdd[:-6]
			housetypesString += (" "+stringToAdd)
		li = listitem(text=com['Community'],subText=housetypesString)
		li.save()
		warddic[actualward(com['MunicipalityDistrict'])].community.add(li)

	for ward in warddic:
		newArea.subsections.add(warddic[ward])
		warddic[ward].save()
	newArea.save()
	myFilter.area.add(newArea)
	myFilter.save()

	return "yes"

def checkFilters():
	properties = ResidentialProperty.objects.all()
	area = []
	area_sub = []
 	community = []
	style = []
	type_own1_out = []
	br = []
	bath_tot = []
	gar_type = []
	gar_spaces = []
	municipality_district = []
	cityList = []
	for prop in properties:
		# if not any(d.get('city', None) == prop.area for d in cityList):
		if prop.area not in area:
			area.append(prop.area)
			cityList.append({"city":prop.area,"ward":[prop.municipality_district],"wardobject":[{"ward":prop.municipality_district,"community":[slugify(prop.community)]}]})
		else :
			index = area.index(prop.area)
			if prop.municipality_district not in cityList[index]["ward"]: 
				cityList[index]["ward"].append(prop.municipality_district)
				cityList[index]["wardobject"].append({"ward":prop.municipality_district,"community":[slugify(prop.community)]})
			else:
				wardindex = cityList[index]["ward"].index(prop.municipality_district)
				if slugify(prop.community) not in cityList[index]["wardobject"][wardindex]["community"]:
					cityList[index]["wardobject"][wardindex]["community"].append(slugify(prop.community))
				pass

		if prop.municipality_district not in municipality_district:
			municipality_district.append(prop.gar_spaces)		

		if prop.community not in community:
			community.append(prop.community)
		if prop.style not in style:
			style.append(prop.style)
		if prop.type_own1_out not in type_own1_out:
			type_own1_out.append(prop.type_own1_out)
		if prop.br not in br:
			br.append(prop.br)
		if prop.bath_tot not in bath_tot:
			bath_tot.append(prop.bath_tot)
		if prop.gar_type not in gar_type:
			gar_type.append(prop.gar_type)
		if prop.gar_spaces not in gar_spaces:
			gar_spaces.append(prop.gar_spaces)

	# print cityList[area.index("Toronto")]
	torontoCon = {"west":[],"east":[],"centre":[],"centre-north":[]}
	for ward in cityList[area.index("Toronto")]["wardobject"]:
		if "W" in ward["ward"]:
			torontoCon["west"] += ward["community"]
		elif "C" in ward["ward"]:
			digit = int(re.search(r'\d+', ward["ward"]).group())
			if(digit in [3,4,6,7,10,12,13,14,15]):
				torontoCon["centre-north"] += ward["community"]
			else:
				torontoCon["centre"] += ward["community"]
		else:
			torontoCon["east"] += ward["community"]

	FilterOptions.objects.all().delete()
	listitem.objects.all().delete()
	minmax.objects.all().delete()
	Area.objects.all().delete()



	br = replaceWithZero(sorted(br))
	brminmax = minmax(num_min=br[0],num_max=br[len(br)-1])
	brminmax.save()
	bath_tot = replaceWithZero(sorted(bath_tot))
	bath_totmax = minmax(num_min=bath_tot[0],num_max=bath_tot[len(bath_tot)-1])
	bath_totmax.save()
	gar_spaces = replaceWithZero(sorted(gar_spaces))
	gar_spacesmax = minmax(num_min=gar_spaces[0],num_max=gar_spaces[len(gar_spaces)-1])
	gar_spacesmax.save()

	myFilter = FilterOptions(br=brminmax, bath_tot=bath_totmax, gar_spaces=gar_spacesmax)
	myFilter.save()

	for sty in style:
		if len(sty) > 1:
			styLI = listitem(text=sty)
			styLI.save()			
			myFilter.style.add(styLI)
	for sty in community:
		if len(sty) > 1:
			styLI = listitem(text=sty)
			styLI.save()			
			myFilter.community.add(styLI)
	for sty in type_own1_out:
		if len(sty) > 1:
			styLI = listitem(text=sty)
			styLI.save()			
			myFilter.type_own1_out.add(styLI)
	for sty in gar_spaces:
		if type(sty) is str:
			if len(sty) > 1:
				styLI = listitem(text=sty)
				styLI.save()			
				myFilter.gar_spaces.add(styLI)

	myFilter.save()

	for city in cityList:
		newArea = Area(text=city["city"])
		newArea.save()
		for ward in city["wardobject"]:
			newWard = Area(text=ward["ward"],ward=True)
			newWard.save()
			for community in ward['community']:
				if len(community) > 1:
					li = listitem(text=community)
					li.save()
					newWard.community.add(li)
			newWard.save()
			newArea.subsections.add(newWard)
		newArea.save()

	newArea = Area(text="torontoCon")
	newArea.save()
	for ward in torontoCon:
		newWard = Area(text=ward,ward=True)
		newWard.save()
		for community in torontoCon[ward]:
			if len(community) > 1:
				li = listitem(text=community)
				li.save()
				newWard.community.add(li)
		newWard.save()
		newArea.subsections.add(newWard)
	newArea.save()			





	# for sub in area_sub:
	# 	newArea = Area(text=area[area_sub.index(sub)])
	# 	newArea.save()
	# 	for sty in sub:
	# 		if len(sty) > 1:
	# 			styLI = listitem(text=sty)
	# 			styLI.save()
	# 			newArea.community.add(styLI)		
	# 	newArea.save()
	# 	myFilter.area.add(newArea)

	myFilter.save()

def checkIfAllPropsHaveOnePhoto():
	properties = ResidentialProperty.objects.filter(s_r="Sale",status="A")
	for prop in properties:
		getfirstimage(prop.ml_num)

def saveAllProp():
	session = librets.RetsSession(rets_connection.login_url)
	if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
		print "Error logging in"
	else:
		properties = ResidentialProperty.objects.filter(s_r="Sale",status="A")
		for prop in properties:
			prop.save()
			if(not prop.firstphoto):
				getAllImagesNoRefresh(session,prop.ml_num)
				prop.save()



def getPeram():
	myFilter = FilterOptions.objects.all().prefetch_related('type_own1_out', 'gar_type')[0]
	location = Area.objects.get(text="torontoCon").subsections.all().prefetch_related('community')
	return {"main":myFilter,"location":location}

commercial_list_of_attributes = [
	'Address',
	'AirConditioning',
	'Amps',
	'ApproxAge',
	'AptUnit',
	'Area',
	'AreaCode',
	'AreaInfluences1',
	'AreaInfluences2',
	'Assessment',
	'AssessmentYear',
	'Basement1',
	'BaySizeLengthFeet',
	'BaySizeLengthInches',
	'BaySizeWidthFeet',
	'BaySizeWidthInches',
	'BusinessBuildingName',
	'Category',
	'Chattels',
	'ClearHeightFeet',
	'ClearHeightInches',
	'CommercialCondoFees',
	'CommonAreaUpcharge',
	'Community',
	'CommunityCode',
	'Crane',
	'DaysOpen',
	'DirectionsCrossStreets',
	'DisplayAddressOnInternet',
	'DoubleManShippingDoors',
	'DoubleManShippingDoorsHeightFeet',
	'DoubleManShippingDoorsHeightInches',
	'DoubleManShippingDoorsWidthFeet',
	'DoubleManShippingDoorsWidthInches',
	'DriveInLevelShippingDoors',
	'DriveInLevelShippingDoorsHeightFeet',
	'DriveInLevelShippingDoorsHeightInches',
	'DriveInLevelShippingDoorsWidthFeet',
	'DriveInLevelShippingDoorsWidthInches',
	'Elevator',
	'Employees',
	'EstimInventoryValuesAtCost',
	'ExpensesActualEstimated',
	'Extras',
	'FinancialStatement',
	'Franchise',
	'Freestanding',
	'GarageType',
	'GradeLevelShippingDoors',
	'GradeLevelShippingDoorsHeightFeet',
	'GradeLevelShippingDoorsHeightInches',
	'GradeLevelShippingDoorsWidthFeet',
	'GradeLevelShippingDoorsWidthInches',
	'GrossIncomeSales',
	'HeatExpenses',
	'HeatType',
	'HoursOpen',
	'HydroExpense',
	'IdxUpdtedDt',
	'IndustrialArea',
	'IndustrialAreaCode',
	'InsuranceExpense',
	'LegalDescription',
	'ListBrokerage',
	'ListPrice',
	'ListPriceCode',
	'LLBO',
	'LotBldgUnitCode',
	'LotDepth',
	'LotFront',
	'LotIrregularities',
	'LotSizeCode',
	'Maintenance',
	'ManagementExpense',
	'Map',
	'MapColumn',
	'MapRow',
	'MaximumRentalTerm',
	'MinimumRentalTerm',
	'MLS',
	'Municipality',
	'MunicipalityCode',
	'MunicipalityDistrict',
	'NetIncomeBeforeDebt',
	'Occupancy',
	'OfficeAptArea',
	'OfficeAptAreaCode',
	'OperatingExpenses',
	'OtherExpenses',
	'OutofAreaMunicipality',
	'OutsideStorage',
	'ParcelId',
	'ParkingSpaces',
	'PerBuilding',
	'PercentageRent',
	'PixUpdtedDt',
	'PostalCode',
	'Province',
	'Rail',
	'RemarksForClients',
	'RetailArea',
	'RetailAreaCode',
	'SaleLease',
	'Seats',
	'SellerPropertyInfoStatement',
	'Sewers',
	'SoilTest',
	'Sprinklers',
	'Status',
	'Street',
	'StreetAbbreviation',
	'StreetDirection',
	'StreetName',
	'Survey',
	'Taxes',
	'TaxesExpense',
	'TaxYear',
	'TimestampSql',
	'TotalArea',
	'TotalAreaCode',
	'TrailerParkingSpots',
	'TruckLevelShippingDoors',
	'TruckLevelShippingDoorsHeightFeet',
	'TruckLevelShippingDoorsHeightInches',
	'TruckLevelShippingDoorsWidthFeet',
	'TruckLevelShippingDoorsWidthInches',
	'TypeOwn1Out',
	'TypeOwnSrch',
	'TypeTaxes',
	'Uffi',
	'Use',
	'Utilities',
	'VacancyAllowance',
	'VirtualTourUploadDate',
	'VirtualTourURL',
	'Volts',
	'Washrooms',
	'Water',
	'WaterExpense',
	'WaterSupplyTypes',
	'YearExpenses',
	'Zoning'
]

condo_list_of_attributes = [
	'Address',
	'AirConditioning',
	'AllInclusive',
	'ApproxAge',
	'ApproxSquareFootage',
	'AptUnit',
	'Area',
	'AreaCode',
	'Assessment',
	'AssessmentYear',
	'Balcony',
	'Basement1',
	'Basement2',
	'Bedrooms',
	'BedroomsPlus',
	'BuildingAmenities1',
	'BuildingAmenities2',
	'BuildingAmenities4',
	'BuildingAmenities5',
	'BuildingAmenities6',
	'BuildingAmenties3',
	'BuildingInsuranceIncluded',
	'CableTVIncluded',
	'CacIncluded',
	'CentralVac',
	'CommonElementsIncluded',
	'Community',
	'CommunityCode',
	'CondoCorp',
	'CondoRegistryOffice',
	'CondoTaxesIncluded',
	'DirectionsCrossStreets',
	'DisplayAddressOnInternet',
	'Elevator',
	'EnsuiteLaundry',
	'Exposure',
	'Exterior1',
	'Exterior2',
	'Extras',
	'FamilyRoom',
	'FireplaceStove',
	'Furnished',
	'GarageParkSpaces',
	'GarageType',
	'HeatIncluded',
	'HeatSource',
	'HeatType',
	'HydroIncluded',
	'IdxUpdtedDt',
	'Kitchens',
	'KitchensPlus',
	'LaundryAccess',
	'LaundryLevel',
	'LeaseTerm',
	'Level',
	'Level1',
	'Level10',
	'Level11',
	'Level12',
	'Level2',
	'Level3',
	'Level4',
	'Level5',
	'Level6',
	'Level7',
	'Level8',
	'Level9',
	'ListBrokerage',
	'ListPrice',
	'Locker',
	'LockerNum',
	'Maintenance',
	'Map',
	'MapColumn',
	'MapRow',
	'MLS',
	'Municipality',
	'MunicipalityCode',
	'MunicipalityDistrict',
	'OutofAreaMunicipality',
	'ParcelId',
	'ParkCostMo',
	'ParkingDrive',
	'ParkingIncluded',
	'ParkingLegalDescription',
	'ParkingLegalDescription2',
	'ParkingSpaces',
	'ParkingSpot1',
	'ParkingSpot2',
	'ParkingType',
	'ParkingType2',
	'PetsPermitted',
	'PixUpdtedDt',
	'PostalCode',
	'PrivateEntrance',
	'PropertyFeatures1',
	'PropertyFeatures2',
	'PropertyFeatures3',
	'PropertyFeatures4',
	'PropertyFeatures5',
	'PropertyFeatures6',
	'Province',
	'RemarksForClients',
	'Retirement',
	'Room1',
	'Room10',
	'Room10Desc1',
	'Room10Desc2',
	'Room10Desc3',
	'Room10Length',
	'Room10Width',
	'Room11',
	'Room11Desc1',
	'Room11Desc2',
	'Room11Desc3',
	'Room11Length',
	'Room11Width',
	'Room12',
	'Room12Desc1',
	'Room12Desc2',
	'Room12Desc3',
	'Room12Length',
	'Room12Width',
	'Room1Desc1',
	'Room1Desc2',
	'Room1Desc3',
	'Room1Length',
	'Room1Width',
	'Room2',
	'Room2Desc1',
	'Room2Desc2',
	'Room2Desc3',
	'Room2Length',
	'Room2Width',
	'Room3',
	'Room3Desc1',
	'Room3Desc2',
	'Room3Desc3',
	'Room3Length',
	'Room3Width',
	'Room4',
	'Room4Desc1',
	'Room4Desc2',
	'Room4Desc3',
	'Room4Length',
	'Room4Width',
	'Room5',
	'Room5Desc1',
	'Room5Desc2',
	'Room5Desc3',
	'Room5Length',
	'Room5Width',
	'Room6',
	'Room6Desc1',
	'Room6Desc2',
	'Room6Desc3',
	'Room6Length',
	'Room6Width',
	'Room7',
	'Room7Desc1',
	'Room7Desc2',
	'Room7Desc3',
	'Room7Length',
	'Room7Width',
	'Room8',
	'Room8Desc1',
	'Room8Desc2',
	'Room8Desc3',
	'Room8Length',
	'Room8Width',
	'Room9',
	'Room9Desc1',
	'Room9Desc2',
	'Room9Desc3',
	'Room9Length',
	'Room9Width',
	'Rooms',
	'RoomsPlus',
	'SaleLease',
	'SharesPer',
	'SpecialDesignation1',
	'SpecialDesignation2',
	'SpecialDesignation3',
	'SpecialDesignation4',
	'SpecialDesignation5',
	'SpecialDesignation6',
	'Status',
	'Street',
	'StreetAbbreviation',
	'StreetDirection',
	'StreetName',
	'Style',
	'Taxes',
	'TaxYear',
	'TimestampSql',
	'TypeOwn1Out',
	'TypeOwnSrch',
	'Uffi',
	'Unit',
	'VirtualTourUploadDate',
	'VirtualTourURL',
	'Washrooms',
	'WashroomsType1',
	'WashroomsType1Level',
	'WashroomsType1Pcs',
	'WashroomsType2',
	'WashroomsType2Level',
	'WashroomsType2Pcs',
	'WashroomsType3',
	'WashroomsType3Level',
	'WashroomsType3Pcs',
	'WashroomsType4',
	'WashroomsType4Level',
	'WashroomsType4Pcs',
	'WashroomsType5',
	'WashroomsType5Level',
	'WashroomsType5Pcs',
	'WaterIncluded',
	'Zoning'
]

condo_list_floats = [
	"AreaCode",
	"Bedrooms",
	"BedroomsPlus",
	"CondoCorp",
	"ListPrice",
	"Map",
	"MapColumn",
	"ParkingSpaces",
	"Rooms",
	"Taxes",
	"TaxYear",
	"Washrooms"
]

residentail_list_of_attributes = [
	'Acreage',
	'AddlMonthlyFees',
	'Address',
	'AirConditioning',
	'AllInclusive',
	'ApproxAge',
	'ApproxSquareFootage',
	'AptUnit',
	'Area',
	'AreaCode',
	'Assessment',
	'AssessmentYear',
	'Basement1',
	'Basement2',
	'Bedrooms',
	'BedroomsPlus',
	'CableTVIncluded',
	'CacIncluded',
	'CentralVac',
	'CommonElementsIncluded',
	'Community',
	'CommunityCode',
	'DirectionsCrossStreets',
	'DisplayAddressOnInternet',
	'Drive',
	'Elevator',
	'Exterior1',
	'Exterior2',
	'Extras',
	'FamilyRoom',
	'FarmAgriculture',
	'FireplaceStove',
	'FrontingOnNSEW',
	'Furnished',
	'GarageSpaces',
	'GarageType',
	'HeatIncluded',
	'HeatSource',
	'HeatType',
	'HydroIncluded',
	'IdxUpdtedDt',
	'Kitchens',
	'KitchensPlus',
	'LaundryAccess',
	'LaundryLevel',
	'LeasedTerms',
	'LegalDescription',
	'Level1',
	'Level10',
	'Level11',
	'Level12',
	'Level2',
	'Level3',
	'Level4',
	'Level5',
	'Level6',
	'Level7',
	'Level8',
	'Level9',
	'ListBrokerage',
	'ListPrice',
	'LotDepth',
	'LotFront',
	'LotIrregularities',
	'LotSizeCode',
	'Map',
	'MapColumn',
	'MapRow',
	'MLS',
	'Municipality',
	'MunicipalityCode',
	'MunicipalityDistrict',
	'OtherStructures1',
	'OtherStructures2',
	'OutofAreaMunicipality',
	'ParcelId',
	'ParkCostMo',
	'ParkingIncluded',
	'ParkingSpaces',
	'PixUpdtedDt',
	'Pool',
	'PostalCode',
	'PrivateEntrance',
	'PropertyFeatures1',
	'PropertyFeatures2',
	'PropertyFeatures3',
	'PropertyFeatures4',
	'PropertyFeatures5',
	'PropertyFeatures6',
	'Province',
	'RemarksForClients',
	'Retirement',
	'Room1',
	'Room10',
	'Room10Desc1',
	'Room10Desc2',
	'Room10Desc3',
	'Room10Length',
	'Room10Width',
	'Room11',
	'Room11Desc1',
	'Room11Desc2',
	'Room11Desc3',
	'Room11Length',
	'Room11Width',
	'Room12',
	'Room12Desc1',
	'Room12Desc2',
	'Room12Desc3',
	'Room12Length',
	'Room12Width',
	'Room1Desc1',
	'Room1Desc2',
	'Room1Desc3',
	'Room1Length',
	'Room1Width',
	'Room2',
	'Room2Desc1',
	'Room2Desc2',
	'Room2Desc3',
	'Room2Length',
	'Room2Width',
	'Room3',
	'Room3Desc1',
	'Room3Desc2',
	'Room3Desc3',
	'Room3Length',
	'Room3Width',
	'Room4',
	'Room4Desc1',
	'Room4Desc2',
	'Room4Desc3',
	'Room4Length',
	'Room4Width',
	'Room5',
	'Room5Desc1',
	'Room5Desc2',
	'Room5Desc3',
	'Room5Length',
	'Room5Width',
	'Room6',
	'Room6Desc1',
	'Room6Desc2',
	'Room6Desc3',
	'Room6Length',
	'Room6Width',
	'Room7',
	'Room7Desc1',
	'Room7Desc2',
	'Room7Desc3',
	'Room7Length',
	'Room7Width',
	'Room8',
	'Room8Desc1',
	'Room8Desc2',
	'Room8Desc3',
	'Room8Length',
	'Room8Width',
	'Room9',
	'Room9Desc1',
	'Room9Desc2',
	'Room9Desc3',
	'Room9Length',
	'Room9Width',
	'Rooms',
	'RoomsPlus',
	'SaleLease',
	'SellerPropertyInfoStatement',
	'Sewers',
	'SpecialDesignation1',
	'SpecialDesignation2',
	'SpecialDesignation3',
	'SpecialDesignation4',
	'SpecialDesignation5',
	'SpecialDesignation6',
	'Status',
	'Street',
	'StreetAbbreviation',
	'StreetDirection',
	'StreetName',
	'Style',
	'Taxes',
	'TaxYear',
	'TimestampSql',
	'TypeOwn1Out',
	'TypeOwnSrch',
	'Uffi',
	'UtilitiesCable',
	'UtilitiesGas',
	'UtilitiesHydro',
	'UtilitiesTelephone',
	'VirtualTourUploadDate',
	'VirtualTourURL',
	'Washrooms',
	'WashroomsType1',
	'WashroomsType1Level',
	'WashroomsType1Pcs',
	'WashroomsType2',
	'WashroomsType2Level',
	'WashroomsType2Pcs',
	'WashroomsType3',
	'WashroomsType3Level',
	'WashroomsType3Pcs',
	'WashroomsType4',
	'WashroomsType4Level',
	'WashroomsType4Pcs',
	'WashroomsType5',
	'WashroomsType5Level',
	'WashroomsType5Pcs',
	'Water',
	'Waterfront',
	'WaterIncluded',
	'WaterSupplyTypes',
	'Zoning'
]

def getCondoImage(imageid,prop):
	try:	
		if(os.path.isfile("%simages/%s-1.jpg"%(MEDIA_ROOT,imageid))):
			print "image already loaded"
			return "image already exists"
		if(prop.PixUpdtedDt == ""):
			print "no Pix Update DT"
			return "no image to be uploaded"
		print "new image %s" %imageid
		session = librets.RetsSession(rets_connection.login_url)
		print "\tloading"		
		if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
			print "Error logging in"
		else:
			request = librets.GetObjectRequest("Property", "Photo")
			print "\t\t%d"%1
			request.AddAllObjects(imageid)
			print "\t\t%d"%2
			response = session.GetObject(request)
			print "\t\t%d"%3
			object_descriptor = response.NextObject()
			print "\t\t%d"%4
			if(object_descriptor != None):
				print "\t\t%d"%5
				# output_file_name = object_descriptor.GetObjectKey() + "-" + str(object_descriptor.GetObjectId()) + ".jpg"
				file = open("%simages/%s-1.jpg" %(MEDIA_ROOT,imageid), 'wb')
				file.write(object_descriptor.GetDataAsString())
				file.close()
				prop.firstphoto = True
				prop.save()
				print "\t\t%d"%6
				print "\tloaded"
		return "Failed to load images"
		session.Logout();
	except Exception, e:
		print "\t%s"%e;
		print "\tfailed %s"%imageid
		return "Failed to load Image, this post might not have an image..."
		pass

def getCondoImagePassSession(imageid,prop,session):
	try:
		if(os.path.isfile("%simages/%s-1.jpg"%(MEDIA_ROOT,imageid))):
			print "image already loaded"
			return "image already exists"
		if(prop.PixUpdtedDt == ""):
			print "no Pix Update DT"
			return "no image to be uploaded"
		print "new image %s" %imageid

		request = librets.GetObjectRequest("Property", "Photo")
		print "\t\t%d"%1
		request.AddAllObjects(imageid)
		print "\t\t%d"%2
		response = session.GetObject(request)
		print "\t\t%d"%3
		object_descriptor = response.NextObject()
		print "\t\t%d"%4
		if(object_descriptor != None):
			print "\t\t%d"%5
			# output_file_name = object_descriptor.GetObjectKey() + "-" + str(object_descriptor.GetObjectId()) + ".jpg"
			file = open("%simages/%s-1.jpg" %(MEDIA_ROOT,imageid), 'wb')
			file.write(object_descriptor.GetDataAsString())
			file.close()
			prop.firstphoto = True
			prop.save()
			print "\t\t%d"%6
			print "\tloaded"
	except Exception, e:
		print "Error on %s"%imageid
		print e

def condos_first_image():
	all_condos = CondoProperty.objects.all().filter(Status="A",PixUpdtedDt__isnull=False,firstphoto=False)
	for condo in all_condos:
		if condo.firstphoto == False:
			# thread.start_new_thread(getCondoImage, (condo.MLS,condo))
			getCondoImage(condo.MLS,condo)


def condos(Full):
	session = librets.RetsSession(rets_connection.login_url)
	print "connected to librets"
	if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
		print "Error logging in"
	else:
		print "connection"
		lastHourDateTime = datetime.today() - timedelta(hours = 24)
		lastHourDateTime = lastHourDateTime.strftime('%Y-%m-%dT%H:%M:%S')
		print "making request"
		if(Full):
			request = session.CreateSearchRequest( "Property", "CondoProperty", "(Status=A)") #ResidentialProperty #CondoProperty #CommercialProperty
		else:
			request = session.CreateSearchRequest( "Property", "CondoProperty", "(TimestampSql=%s+)"%(lastHourDateTime,))
		request.SetStandardNames(True)
		request.SetSelect("")
		request.SetLimit(0)
		request.SetOffset(1)	
		request.SetFormatType(librets.SearchRequest.COMPACT_DECODED)
		request.SetCountType(librets.SearchRequest.RECORD_COUNT_AND_RESULTS)	
		print "sending request"
		results = session.Search(request)		
		columns = results.GetColumns()

		forPhotos = []
		now = datetime.now()
		yesterday = now - timedelta(hours=24)
		while results.HasNext():
			MLS = results.GetString("MLS")
			print "\n%s"%MLS
			# we test to see if it already exists, if not we create a new property
			try:
				prop = CondoProperty.objects.get(MLS = MLS)
				print "update"
				prop.edited = now;
			except Exception, e:
				print "new"
				prop = CondoProperty(MLS = MLS,edited = now)

			# we then go through all the variables adding them
			for attribute in condo_list_of_attributes:
				try:			
					value = results.GetString(attribute)

					# check if it has an image, 
					if attribute == "PixUpdtedDt":
						if (value and prop.firstphoto != True):
							forPhotos.append([MLS,prop])
						setattr(prop, attribute, value)
					elif any(x == attribute for x in condo_list_floats):
						if(value):
							try:
								setattr(prop, attribute, float(value))
							except Exception, e:
								print e
					else:
						setattr(prop, attribute, value)
				except Exception, e:
					print "Error on: %s"%attribute
					print e
			prop.save()

		print "total condoProp: %d"%len(forPhotos)
		old = CondoProperty.objects.all().filter(edited__lt=now)
		for prop in old:
			prop.Status = "S"
			prop.save()
		# session.Logout();
		time.sleep(2)

		print "getting photos"
		session = librets.RetsSession(rets_connection.login_url)
		if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
			print "Error logging in"
		else:
			print "\tloading"
		for val in forPhotos:
			getCondoImagePassSession(val[0],val[1],session)





