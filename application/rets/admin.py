from django.db import models
from django.contrib import admin
from rets.models import *

# Register your models here.

# Ml num:

class residentail(admin.ModelAdmin):
	list_display = ('ml_num','status' ,'addr','admin_image','municipality','municipality_district','s_r','featured','rltr')
	list_filter = ('status','s_r','firstphoto','style','type_own1_out','area','rltr')
	list_editable = ('featured',)
	search_fields = ['ml_num','community']

admin.site.register(ResidentialProperty,residentail)

class filteropt(admin.ModelAdmin):
	list_filter = ('ward',)
	
admin.site.register(FilterOptions)
admin.site.register(Area,filteropt)