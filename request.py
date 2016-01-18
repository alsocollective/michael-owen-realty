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

testView("something")
filloutlists()
condos(False)
# condos_first_image()
print "\n\n=== done ===\n\n"
