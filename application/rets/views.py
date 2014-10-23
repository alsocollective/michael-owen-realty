try:

	from django.http import HttpResponse
	from django.shortcuts import render_to_response, get_object_or_404, render
	from django.conf import settings
	from django.http import Http404  
	from django.core.mail import send_mail
	from datetime import datetime, timedelta
	from rets.relat import ResidentialRelations, ResidentialRelations_rev
	from django.template.defaultfilters import slugify
	from rets.models import *
	import thread
	import json
	import librets
	import time
	import os.path
	import re
	from michael_site.settings import rets_connection,MEDIA_ROOT


	#	example case...
	# 	emailBoutPorp({"sender":"bohdananderson@gmail.com","body":"WHY hello there!"})
	def emailBoutPorp(data):
		print "sent Message"
		title = "email from %s" %data["sender"]
		message = "Message: %s From: %s"%(data["body"],data["sender"])
		send_mail(title,message,"websitemicheal@gmail.com" ,["bohdan@alsocollective.com"], fail_silently=False)
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

	def loadData():
		session = librets.RetsSession(rets_connection.login_url)
		# session.SetHttpLogName("log.1.txt");

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
			# file_ = open('data.json', 'w')
			data = []
			imagelist = []
			while results.HasNext():
				out = {}
				for column in columns:
					if(column == "MLS"):
						imagelist.append(results.GetString(column))
					out[column] = results.GetString(column)
				data.append(out)

			for mls in imagelist:
				thread.start_new_thread(getfirstimage, (mls,))
			session.Logout();			
			return data
		session.Logout();
		return None;

	def getFullListOfMLS():
		session = librets.RetsSession(rets_connection.login_url)

		session.SetHttpLogName("log.txt");

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

	def getfirstimage(imageid):
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
	def getAllImages(imageid):
		print "load images for: %s"%imageid
		imageid = imageid
		imageid = imageid.encode('ascii', "ignore")
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
				return "center-north"
			else:
				return "center"
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

		communities = ResidentialProperty.objects.filter(area='Toronto').values('community','municipality_district').distinct()
		wards = ResidentialProperty.objects.filter(area='Toronto').values('municipality_district').distinct()

		newArea = Area(text="torontoCon")
		newArea.save()

		warddic = {
			'west':'',
			'east':'',
			'center':'',
			'center-north':''
		}
		
		for ward in warddic:
			warddic[ward] = Area(text=ward,ward=True)
			warddic[ward].save()

		for com in communities:
			li = listitem(text=com['community'])
			li.save()
			warddic[actualward(com['municipality_district'])].community.add(li)

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
		torontoCon = {"west":[],"east":[],"center":[],"center-north":[]}
		for ward in cityList[area.index("Toronto")]["wardobject"]:
			if "W" in ward["ward"]:
				torontoCon["west"] += ward["community"]
			elif "C" in ward["ward"]:
				digit = int(re.search(r'\d+', ward["ward"]).group())
				if(digit in [3,4,6,7,10,12,13,14,15]):
					torontoCon["center-north"] += ward["community"]
				else:
					torontoCon["center"] += ward["community"]
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


	def getPeram():
		myFilter = FilterOptions.objects.all().prefetch_related('type_own1_out', 'gar_type')[0]
		location = Area.objects.get(text="torontoCon").subsections.all().prefetch_related('community')
		return {"main":myFilter,"location":location}

except Exception, e:
	print "||||||||||||||||||||"
	print "librest was probably not installed"
	print "but:"
	print e
	print "||||||||||||||||||||"
	def getPeram():
		myFilter = FilterOptions.objects.all().prefetch_related('type_own1_out', 'gar_type')[0]
		location = Area.objects.get(text="torontoCon").subsections.all().prefetch_related('community')
		return {"main":myFilter,"location":location}
	pass