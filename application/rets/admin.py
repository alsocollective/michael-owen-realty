from django.db import models
from django.contrib import admin
from rets.models import *

# Register your models here.

# Ml num:

class residentail(admin.ModelAdmin):
	list_display = ('ml_num','status' ,'addr','s_r','timestamp_sql','idx_dt','pix_updt','admin_image','municipality','municipality_district','municipality_code',)
	list_filter = ('status','firstphoto','style','type_own1_out','area')
	search_fields = ['ml_num']

admin.site.register(ResidentialProperty,residentail)

class filteropt(admin.ModelAdmin):
	list_filter = ('ward',)
	
admin.site.register(FilterOptions)
admin.site.register(Area,filteropt)
