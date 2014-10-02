import librets
import sys
import json


class rets_connection:
	user_id = "D14asc"
	passwd = "An$9376"
	login_url = "http://rets.torontomls.net:6103/rets-treb3pv/server/login"

def dump_all_classes(metadata, resource):
	resource_name = resource.GetResourceID()
	for aClass in metadata.GetAllClasses(resource_name):
		print "Resource name: " + resource_name + " [" + resource.GetStandardName() + "]"
		print "Class name: " + aClass.GetClassName() + " ["  + aClass.GetStandardName() + "]"
		dump_all_tables(metadata, aClass)
		print	

def dump_all_tables(metadata, aClass):
	for table in metadata.GetAllTables(aClass):
		print "Table name: " + table.GetSystemName()  + " [" + table.GetStandardName() + "]"

def dump_all_lookups(metadata, resource):
	resource_name = resource.GetResourceID()
	for lookup in metadata.GetAllLookups(resource_name):
		print "Resource name: " + resource_name + " [" + resource.GetStandardName() + "]"
		print "Lookup name: " + lookup.GetLookupName() + " ("  + lookup.GetVisibleName() + ")"
		dump_all_lookup_types(metadata, lookup)
		print






def retriveThings(session):
	request = session.CreateSearchRequest( "Property", "ResidentialProperty", "(status=A)")
	request.SetStandardNames(True)
	request.SetSelect("")
	request.SetLimit(0)
	request.SetOffset(1)
	request.SetFormatType(librets.SearchRequest.COMPACT_DECODED)
	request.SetCountType(librets.SearchRequest.RECORD_COUNT_AND_RESULTS)

	results = session.Search(request)
	print "Record count: " + `results.GetCount()`

	columns = results.GetColumns()


	while results.HasNext():
		for column in columns:
			print column + ": " + results.GetString(column)
		print


def updates2(session):
	request = session.CreateSearchRequest( "Property", "ResidentialProperty", "(TimestampSql=2014-09-17T16:00:00+)")
	request.SetStandardNames(True)
	request.SetSelect("")
	request.SetLimit(0)
	request.SetOffset(1)	
	request.SetFormatType(librets.SearchRequest.COMPACT_DECODED)
	request.SetCountType(librets.SearchRequest.RECORD_COUNT_AND_RESULTS)	
	try:
		results = session.Search(request)		
		try:
			print "Record count: " + `results.GetCount()`
			columns = results.GetColumns()
			file_ = open('data.json', 'w')
			data = []
			while results.HasNext():
				out = {}
				for column in columns:
					out[column] = results.GetString(column)
				data.append(out)
			file_.write(json.dumps(data, ensure_ascii=False))
			file_.close()
		except Exception, e:
			print "failed inside of setCount type"
			pass


	except Exception, e:
		print "failed at getting a return"
		pass


def updates(session):
	try:
		request = session.CreateUpdateRequest( "Property", "ResidentialProperty")
		# request.SetStandardNames(True)
		request.SetUpdateType("Change");
		request.GetAllFields();
		request.SetValidateFlag(librets.UpdateRequest.UPDATE_OK);
		request.SetDelimiter("|");
		# request.SetField("MLS", "X2900171")
		# request.SetField("LotSizeCode", "Acres")
		# request.SetUpdateType("Change");
		# request.SetValidateFlag(librets.UpdateRequest.VALIDATE_ONLY);

		results = session.Update(request)
		columns = results.GetColumns()
		print columns
		while results.HasNext():
			for column in columns:
				print column + ": " + results.GetString(column)
			print

	except Exception, e:
		print "errored out in update:",e
		pass
def logout(session):
	logout = session.Logout();

	# print "Billing info: " + logout.GetBillingInfo()
	# print "Logout message: " + logout.GetLogoutMessage()
	# print "Connect time: " + str(logout.GetConnectTime())


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









print "starting"
try:
	session = librets.RetsSession(rets_connection.login_url)
	if (not session.Login(rets_connection.user_id, rets_connection.passwd)):
		print "Error logging in"
		sys.exit(2)
	print "started"
	log_file = sys.argv[1]	
	session.SetHttpLogName(log_file);
	print "logging"

	# retriveThings(session)
	updates2(session)
	# printoutbasics(session)

	logout(session)
except Exception, e:
	print "Exception: ", e



# (LIST_87=2014-09-15T00:00:00+)
# (timestamp_sql=2014-09-15T00:00:00+),(idx_dt=2014-09-15T00:00:00+)

# (IdxUpdtedDt=2014-09-15T00:00:00+) OR (TimestampSql=2014-09-15T00:00:00+)
# (ListPrice=1000-)

# IdxUpdtedDt
# TimestampSql