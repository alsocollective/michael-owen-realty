from michael_site.views import *
import time
from django.core.mail import send_mail

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

message = "yep so it failed."
try:
	testView("something")
except Exception, e:
	send_mail("test view faield",message,"websitemicheal@gmail.com" ,["michaelowenrealestate@gmail.com"], fail_silently=False)
	pass

try:
	filloutlists()
except Exception, e:
	send_mail("fill out list faild",message,"websitemicheal@gmail.com" ,["michaelowenrealestate@gmail.com"], fail_silently=False)
	pass

try:
	condos(False)
except Exception, e:
	send_mail("condos update failed",message,"websitemicheal@gmail.com" ,["michaelowenrealestate@gmail.com"], fail_silently=False)
	pass


# condos_first_image()
print "\n\n=== done ===\n\n"
