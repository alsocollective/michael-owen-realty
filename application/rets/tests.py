print "\n\n\n\n\n\n\n start \n\n"

from rets.models import *

n = NeightbourHood.objects.all()
for na in n:
	l = na.getHousesRelated()
	for la in l:
		print "--"
		print la.community
		print la.status
		print "--"

print "\n\n\n\n\n\n\n end \n\n"