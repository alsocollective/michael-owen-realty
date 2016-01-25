from michael_site.views import *
import time

# testView("soemthing")

from rets.views import *
print "\n\n=== awesome ===\n\n"
try:
	#condos(False)
	pass
except Exception, e:
	print "condos failed to load"
	print e
	pass

print "condos finished"

#time.sleep(120) 

print "houses start"

try:
	testView("something")
except Exception, e:
	pass

try:
	filloutlists()
except Exception, e:
	pass

try:
	condos(False)
except Exception, e:
	pass


# condos_first_image()
print "\n\n=== done ===\n\n"
