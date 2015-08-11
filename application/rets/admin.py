from django.db import models
from django.contrib import admin
from rets.models import *

# Register your models here.

# Ml num:

class residentail(admin.ModelAdmin):
	list_display = ('admin_image','ml_num','lp_dol','pix_updt','status' ,'addr','featured')
	list_filter = ('pix_updt','status','style','type_own1_out','area','rltr')
	list_editable = ('featured',)
	search_fields = ['ml_num','community','rltr']

admin.site.register(ResidentialProperty,residentail)

class filteropt(admin.ModelAdmin):
	list_filter = ('ward',)
	
admin.site.register(FilterOptions)
admin.site.register(Area,filteropt)
admin.site.register(EmailRmark)

class AboutPageAdmin(admin.ModelAdmin):
	filter_horizontal = ('section_one','pullquotes_one','section_two','pullquotes_two','section_three')

class condo(admin.ModelAdmin):
	list_display = ('admin_image','MLS','ListPrice','PixUpdtedDt','Status' ,'Address','featured','TimestampSql')
	# list_filter = ('PixUpdtedDt','status','style','type_own1_out','area','rltr')
	list_editable = ('featured',)
	search_fields = ['MLS','Community','ListBrokerage']

admin.site.register(TextField)
admin.site.register(AboutPage,AboutPageAdmin)
admin.site.register(CaseStudy)
admin.site.register(SellPage)
admin.site.register(BuyPage)
admin.site.register(NeightbourHood)
admin.site.register(SearchPage)
admin.site.register(listitem)
admin.site.register(CondoProperty,condo)