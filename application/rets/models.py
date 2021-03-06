from django.db import models
from django.template.defaultfilters import slugify
from easy_thumbnails.fields import ThumbnailerImageField
import re,os, os.path
from michael_site.settings import rets_connection,MEDIA_ROOT

class ResidentialProperty(models.Model):
	acres = models.TextField(max_length=800, blank=True)
	addl_mo_fee = models.IntegerField(blank=True,null=True) 
	addr = models.TextField(max_length=1000, blank=True)
	a_c = models.TextField(max_length=100, blank=True)
	all_inc = models.TextField(max_length=100, blank=True)
	yr_built = models.TextField(max_length=500, blank=True)
	sqft = models.TextField(max_length=900, blank=True)
	apt_num = models.TextField(max_length=500, blank=True)
	area = models.TextField(max_length=1000, blank=True)
	area_code = models.TextField(max_length=400, blank=True)
	tv = models.IntegerField(blank=True,null=True) 
	ass_year = models.IntegerField(blank=True,null=True) 
	bsmt1_out = models.TextField(max_length=1000, blank=True)
	bsmt2_out = models.TextField(max_length=1000, blank=True)
	br = models.IntegerField(blank=True,null=True) 
	br_plus = models.IntegerField(blank=True,null=True) 
	cable = models.TextField(max_length=100, blank=True)
	cac_inc = models.TextField(max_length=100, blank=True)
	central_vac = models.TextField(max_length=100, blank=True)
	comel_inc = models.TextField(max_length=100, blank=True)
	community = models.TextField(max_length=1000, blank=True)
	community_code = models.TextField(max_length=1000, blank=True)
	cross_st = models.TextField(max_length=1000, blank=True)
	disp_addr = models.TextField(max_length=100, blank=True)
	drive = models.TextField(max_length=1000, blank=True)
	elevator = models.TextField(max_length=700, blank=True)
	constr1_out = models.TextField(max_length=600, blank=True)
	constr2_out = models.TextField(max_length=700, blank=True)
	extras = models.TextField(max_length=1000, blank=True)
	den_fr = models.TextField(max_length=100, blank=True)
	farm_agri = models.TextField(max_length=200, blank=True)
	fpl_num = models.TextField(max_length=100, blank=True)
	comp_pts = models.TextField(max_length=100, blank=True)
	furnished = models.TextField(max_length=400, blank=True)
	gar_spaces = models.IntegerField(blank=True,null=True) 
	gar_type = models.TextField(max_length=1000, blank=True)
	heat_inc = models.TextField(max_length=100, blank=True)
	fuel = models.TextField(max_length=900, blank=True)
	heating = models.TextField(max_length=1000, blank=True)
	hydro_inc = models.TextField(max_length=100, blank=True)
	idx_dt = models.DateTimeField(auto_now=False,blank=True,null=True) 
	num_kit = models.IntegerField(blank=True,null=True) 
	kit_plus = models.IntegerField(blank=True,null=True) 
	laundry = models.TextField(max_length=300, blank=True)
	laundry_lev = models.TextField(max_length=500, blank=True)
	lease_term = models.TextField(max_length=1000, blank=True)
	legal_desc = models.TextField(max_length=1000, blank=True)
	level1 = models.TextField(max_length=800, blank=True)
	level10 = models.TextField(max_length=800, blank=True)
	level11 = models.TextField(max_length=800, blank=True)
	level12 = models.TextField(max_length=800, blank=True)
	level2 = models.TextField(max_length=800, blank=True)
	level3 = models.TextField(max_length=800, blank=True)
	level4 = models.TextField(max_length=800, blank=True)
	level5 = models.TextField(max_length=800, blank=True)
	level6 = models.TextField(max_length=800, blank=True)
	level7 = models.TextField(max_length=800, blank=True)
	level8 = models.TextField(max_length=800, blank=True)
	level9 = models.TextField(max_length=800, blank=True)
	rltr = models.TextField(max_length=1000, blank=True)
	lp_dol = models.IntegerField(blank=True,null=True) 
	depth = models.FloatField(blank=True,null=True)
	front_ft = models.FloatField(blank=True,null=True)
	irreg = models.TextField(max_length=100, blank=True)
	lotsz_code = models.TextField(max_length=800, blank=True)
	mmap_page = models.IntegerField(blank=True,null=True) 
	mmap_col = models.IntegerField(blank=True,null=True) 
	mmap_row = models.TextField(max_length=100, blank=True)
	ml_num = models.TextField(max_length=800, blank=True)
	municipality = models.TextField(max_length=1000, blank=True)
	municipality_district = models.TextField(max_length=1000, blank=True)
	municipality_code = models.TextField(max_length=1000, blank=True)
	oth_struc1_out = models.TextField(max_length=1000, blank=True)
	oth_struc2_out = models.TextField(max_length=1000, blank=True)
	outof_area = models.TextField(max_length=600, blank=True)
	park_chgs = models.FloatField(blank=True,null=True)
	prkg_inc = models.TextField(max_length=100, blank=True)
	park_spcs = models.IntegerField(blank=True,null=True) 
	parcel_id = models.TextField(max_length=900, blank=True)
	pix_updt = models.DateTimeField(auto_now=False,blank=True,null=True) 
	pool = models.TextField(max_length=800, blank=True)
	zip = models.TextField(max_length=700, blank=True)
	pvt_ent = models.TextField(max_length=100, blank=True)
	prop_feat1_out = models.TextField(max_length=1000, blank=True)
	prop_feat2_out = models.TextField(max_length=1000, blank=True)
	prop_feat3_out = models.TextField(max_length=1000, blank=True)
	prop_feat4_out = models.TextField(max_length=1000, blank=True)
	prop_feat5_out = models.TextField(max_length=1000, blank=True)
	prop_feat6_out = models.TextField(max_length=1000, blank=True)
	county = models.TextField(max_length=1000, blank=True)
	ad = models.TextField(max_length=500, blank=True)
	retirement = models.TextField(max_length=100, blank=True)
	rm1_out = models.TextField(max_length=900, blank=True)
	rm1_dc1_out = models.TextField(max_length=1000, blank=True)
	rm1_dc2_out = models.TextField(max_length=1000, blank=True)
	rm1_dc3_out = models.TextField(max_length=1000, blank=True)
	rm1_len = models.FloatField(blank=True,null=True)
	rm1_wth = models.FloatField(blank=True,null=True)
	rm10_out = models.TextField(max_length=900, blank=True)
	rm10_dc1_out = models.TextField(max_length=1000, blank=True)
	rm10_dc2_out = models.TextField(max_length=1000, blank=True)
	rm10_dc3_out = models.TextField(max_length=1000, blank=True)
	rm10_len = models.FloatField(blank=True,null=True)
	rm10_wth = models.FloatField(blank=True,null=True)
	rm11_out = models.TextField(max_length=900, blank=True)
	rm11_dc1_out = models.TextField(max_length=1000, blank=True)
	rm11_dc2_out = models.TextField(max_length=1000, blank=True)
	rm11_dc3_out = models.TextField(max_length=1000, blank=True)
	rm11_len = models.FloatField(blank=True,null=True)
	rm11_wth = models.FloatField(blank=True,null=True)
	rm12_out = models.TextField(max_length=900, blank=True)
	rm12_dc1_out = models.TextField(max_length=1000, blank=True)
	rm12_dc2_out = models.TextField(max_length=1000, blank=True)
	rm12_dc3_out = models.TextField(max_length=1000, blank=True)
	rm12_len = models.FloatField(blank=True,null=True)
	rm12_wth = models.FloatField(blank=True,null=True)
	rm2_out = models.TextField(max_length=900, blank=True)
	rm2_dc1_out = models.TextField(max_length=1000, blank=True)
	rm2_dc2_out = models.TextField(max_length=1000, blank=True)
	rm2_dc3_out = models.TextField(max_length=1000, blank=True)
	rm2_len = models.FloatField(blank=True,null=True)
	rm2_wth = models.FloatField(blank=True,null=True)
	rm3_out = models.TextField(max_length=900, blank=True)
	rm3_dc1_out = models.TextField(max_length=1000, blank=True)
	rm3_dc2_out = models.TextField(max_length=1000, blank=True)
	rm3_dc3_out = models.TextField(max_length=1000, blank=True)
	rm3_len = models.FloatField(blank=True,null=True)
	rm3_wth = models.FloatField(blank=True,null=True)
	rm4_out = models.TextField(max_length=900, blank=True)
	rm4_dc1_out = models.TextField(max_length=1000, blank=True)
	rm4_dc2_out = models.TextField(max_length=1000, blank=True)
	rm4_dc3_out = models.TextField(max_length=1000, blank=True)
	rm4_len = models.FloatField(blank=True,null=True)
	rm4_wth = models.FloatField(blank=True,null=True)
	rm5_out = models.TextField(max_length=900, blank=True)
	rm5_dc1_out = models.TextField(max_length=1000, blank=True)
	rm5_dc2_out = models.TextField(max_length=1000, blank=True)
	rm5_dc3_out = models.TextField(max_length=1000, blank=True)
	rm5_len = models.FloatField(blank=True,null=True)
	rm5_wth = models.FloatField(blank=True,null=True)
	rm6_out = models.TextField(max_length=900, blank=True)
	rm6_dc1_out = models.TextField(max_length=1000, blank=True)
	rm6_dc2_out = models.TextField(max_length=1000, blank=True)
	rm6_dc3_out = models.TextField(max_length=1000, blank=True)
	rm6_len = models.FloatField(blank=True,null=True)
	rm6_wth = models.FloatField(blank=True,null=True)
	rm7_out = models.TextField(max_length=900, blank=True)
	rm7_dc1_out = models.TextField(max_length=1000, blank=True)
	rm7_dc2_out = models.TextField(max_length=1000, blank=True)
	rm7_dc3_out = models.TextField(max_length=1000, blank=True)
	rm7_len = models.FloatField(blank=True,null=True)
	rm7_wth = models.FloatField(blank=True,null=True)
	rm8_out = models.TextField(max_length=900, blank=True)
	rm8_dc1_out = models.TextField(max_length=1000, blank=True)
	rm8_dc2_out = models.TextField(max_length=1000, blank=True)
	rm8_dc3_out = models.TextField(max_length=1000, blank=True)
	rm8_len = models.FloatField(blank=True,null=True)
	rm8_wth = models.FloatField(blank=True,null=True)
	rm9_out = models.TextField(max_length=900, blank=True)
	rm9_dc1_out = models.TextField(max_length=1000, blank=True)
	rm9_dc2_out = models.TextField(max_length=1000, blank=True)
	rm9_dc3_out = models.TextField(max_length=1000, blank=True)
	rm9_len = models.FloatField(blank=True,null=True)
	rm9_wth = models.FloatField(blank=True,null=True)
	rms = models.IntegerField(blank=True,null=True) 
	rooms_plus = models.IntegerField(blank=True,null=True) 
	s_r = models.TextField(max_length=900, blank=True)
	vend_pis = models.TextField(max_length=1000, blank=True)
	sewer = models.TextField(max_length=1000, blank=True)
	spec_des1_out = models.TextField(max_length=900, blank=True)
	spec_des2_out = models.TextField(max_length=900, blank=True)
	spec_des3_out = models.TextField(max_length=900, blank=True)
	spec_des4_out = models.TextField(max_length=900, blank=True)
	spec_des5_out = models.TextField(max_length=900, blank=True)
	spec_des6_out = models.TextField(max_length=900, blank=True)
	status = models.TextField(max_length=100, blank=True)
	st_num = models.TextField(max_length=700, blank=True)
	st_sfx = models.TextField(max_length=400, blank=True)
	st_dir = models.TextField(max_length=100, blank=True)
	st = models.TextField(max_length=1000, blank=True)
	style = models.TextField(max_length=1000, blank=True)
	yr = models.IntegerField(blank=True,null=True) 
	taxes = models.FloatField(blank=True,null=True)
	type_own_srch = models.TextField(max_length=700, blank=True)
	type_own1_out = models.TextField(max_length=800, blank=True)
	uffi = models.TextField(max_length=200, blank=True)
	timestamp_sql = models.DateTimeField(auto_now=False,blank=True,null=True) 
	util_cable = models.TextField(max_length=100, blank=True)
	gas = models.TextField(max_length=100, blank=True)
	elec = models.TextField(max_length=100, blank=True)
	util_tel = models.TextField(max_length=100, blank=True)
	vtour_updt = models.URLField(max_length=1000,blank=True)
	tour_url = models.URLField(max_length=1000,blank=True)
	bath_tot = models.IntegerField(blank=True,null=True) 
	wcloset_t1 = models.IntegerField(blank=True,null=True) 
	wcloset_p1 = models.IntegerField(blank=True,null=True) 
	wcloset_t1lvl = models.TextField(max_length=800, blank=True)
	wcloset_t2 = models.IntegerField(blank=True,null=True) 
	wcloset_p2 = models.IntegerField(blank=True,null=True) 
	wcloset_t2lvl = models.TextField(max_length=800, blank=True)
	wcloset_t3 = models.IntegerField(blank=True,null=True) 
	wcloset_p3 = models.IntegerField(blank=True,null=True) 
	wcloset_t3lvl = models.TextField(max_length=800, blank=True)
	wcloset_t4 = models.IntegerField(blank=True,null=True) 
	wcloset_p4 = models.IntegerField(blank=True,null=True) 
	wcloset_t4lvl = models.TextField(max_length=800, blank=True)
	wcloset_t5 = models.IntegerField(blank=True,null=True) 
	wcloset_p5 = models.IntegerField(blank=True,null=True) 
	wcloset_t5lvl = models.TextField(max_length=800, blank=True)
	water = models.TextField(max_length=900, blank=True)
	water_inc = models.TextField(max_length=100, blank=True)
	wtr_suptyp = models.TextField(max_length=200, blank=True)
	waterfront = models.TextField(max_length=800, blank=True)
	zoning = models.TextField(max_length=1000, blank=True)
	numofphotos = models.IntegerField(blank=True,null=True)
	firstphoto = models.BooleanField(default=False)
	featured = 	models.DateTimeField(auto_now=False,blank=True,null=True) 
	ad_text = models.TextField(max_length=1000, blank=True,null=True)

	def admin_image(self):
		return '<img style="width:200px;height:auto;" src="/static/images/%s-1.jpg"/>' % self.ml_num
		# return '<img style="width:200px;height:auto;" src="http://www.also-static.com/alsocollective/uploaded/%s"/>' % self.title
	admin_image.allow_tags = True

	def __unicode__(self):
		return self.ml_num

	def get_or_none(self, **kwargs):
		try:
			return self.get(**kwargs)
		except self.model.DoesNotExist:
			return None

	def save(self,*args, **kwargs):
		# self.slug = slugify(self.title)
		if(os.path.isfile("%simages/%s-1.jpg"%(MEDIA_ROOT,self.ml_num))):
			self.firstphoto = True
		else:
			self.firstphoto = False
		super(ResidentialProperty, self).save(*args, **kwargs)

class listitem(models.Model):
	text = models.TextField(max_length=1000)
	subText = models.TextField(max_length=1000, blank=True, null=True)
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		stringToAdd = (re.sub('[-]','',slugify(self.text)))
		if "storey" in stringToAdd:
			stringToAdd = "storey" + stringToAdd[:-6]		
		self.slug = stringToAdd
		super(listitem, self).save(*args, **kwargs)

	class Meta:
		ordering = ['text']

	def __unicode__(self):
		return self.text


class minmax(models.Model):
	num_min = models.FloatField()
	num_max = models.FloatField()
	def __unicode__(self):
		return "%d - %d" %(self.num_min,self.num_max)

class FilterOptions(models.Model):
	area = models.ManyToManyField('Area', blank=True,null=True)
	community = models.ManyToManyField('listitem',related_name='community', blank=True,null=True)
	style = models.ManyToManyField('listitem',related_name='style', blank=True,null=True)
	type_own1_out = models.ManyToManyField('listitem',related_name='type_own1_out', blank=True,null=True)
	br  = models.ForeignKey('minmax',related_name='br', blank=True,null=True)
	bath_tot = models.ForeignKey('minmax',related_name='bath_tot', blank=True,null=True)
	gar_type = models.ManyToManyField('listitem',related_name='gar_type', blank=True,null=True)
	gar_spaces = models.ForeignKey('minmax',related_name='gar_spaces', blank=True,null=True)

class Area(models.Model):
	text = models.TextField(max_length=1000)
	community = models.ManyToManyField('listitem',related_name='community_area', blank=True,null=True)
	subsections = models.ManyToManyField('Area',related_name='area-thing', blank=True,null=True)
	ward = models.BooleanField(default=False)
	# payloadText = models.TextField(max_length=10000)
	def __unicode__(self):
		return self.text

class EmailRmark(models.Model):
	ipaddress = models.IPAddressField()
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s %s"%(self.ipaddress, self.date.strftime('%H:%M:%S %m/%d/%Y'))





class TextField(models.Model):
	title = models.CharField(max_length=255,blank=True,null=True)
	text = models.TextField(max_length=1000,blank=True,null=True)
	order = models.IntegerField(default=99,blank=True,null=True)

	def __unicode__(self):
		return slugify(self.title)


class AboutPage(models.Model):
	image = ThumbnailerImageField(upload_to='selfimage',blank=True,null=True)#models.ImageField("michealsimage",upload_to=settings.STATIC_ROOT, blank=True, null=True)
	biography = models.TextField(max_length=1000,blank=True,null=True)
	section_one = models.ManyToManyField(TextField,blank=True,null=True,related_name='AboutPage_section_one')
	pullquotes_one = models.ManyToManyField(TextField,blank=True,null=True,related_name='AboutPage_quote_one')
	section_two = models.ManyToManyField(TextField,blank=True,null=True,related_name='AboutPage_section_two')
	pullquotes_two = models.ManyToManyField(TextField,blank=True,null=True,related_name='AboutPage_quote_two')
	section_three = models.ManyToManyField(TextField,blank=True,null=True,related_name='AboutPage_section_three')
	footer = models.TextField(max_length=1000,blank=True,null=True)
	created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.created.strftime('%Y/%m/%d %H:%M:%S')

class CaseStudy(models.Model):
	title = models.CharField(max_length=255,blank=True,null=True)
	clientNeeds = models.ManyToManyField(TextField,blank=True,null=True,related_name='caseStudy_client')
	sellingProcess = models.ManyToManyField(TextField,blank=True,null=True,related_name='caseStudy_selling')
	outcomes = models.ManyToManyField(TextField,blank=True,null=True,related_name='caseStudy_outcome')
	def __unicode__(self):
		return self.title	

class SellPage(models.Model):
	caseStudy = models.ManyToManyField(CaseStudy,blank=True,null=True)
	section = models.ManyToManyField(TextField,blank=True,null=True)
	footer = models.TextField(max_length=1000,blank=True,null=True)
	created = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.created.strftime('%Y/%m/%d %H:%M:%S')

class BuyPage(models.Model):
	caseStudy = models.ManyToManyField(CaseStudy,blank=True,null=True)
	section_one = models.ManyToManyField(TextField,blank=True,null=True,related_name='buypage_sec_one')
	pullquotes = models.ManyToManyField(TextField,blank=True,null=True,related_name='buypage_quote')
	section_two = models.ManyToManyField(TextField,blank=True,null=True,related_name='buypage_sec_two')
	footer = models.TextField(max_length=1000,blank=True,null=True)
	created = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.created.strftime('%Y/%m/%d %H:%M:%S')

LOCATIONS = (('west','west'),('east','east'),('center','center'),('center north','center north'))
class NeightbourHood(models.Model):
	title = models.CharField(max_length=500,blank=True,null=True)
	description = models.TextField(max_length=1000,blank=True,null=True)
	image = ThumbnailerImageField(upload_to='neighbourhood',blank=True,null=True)
	location = models.CharField(max_length=99, choices=LOCATIONS)
	slug = models.SlugField(blank=True)
	db_names = models.CharField(max_length=500,blank=True,null=True)

	class Meta:
		verbose_name = "Neighbourhood"

	def getHousesRelated(self):
		if(self.db_names):
			return ResidentialProperty.objects.all().filter(status="A",community__in = self.db_names.split(" "))
		return []

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(NeightbourHood, self).save(*args, **kwargs)
	
	def showNeighbourhoods(self):
		com = ResidentialProperty.objects.values('community').distinct().order_by('community')
		out = "<ul style='-webkit-column-count: 3; -moz-column-count: 3; column-count: 3;'>"
		for c in com:
			out += "<li>"
			out += c["community"]
			out += "</li>"
		out += "</ul>"
		return out
	showNeighbourhoods.allow_tags = True

	def __unicode__(self):
		return self.title


class SearchPage(models.Model):
	locations = models.ManyToManyField(NeightbourHood,blank=True,null=True)
	footer = models.TextField(max_length=1000,blank=True,null=True)
	created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.created.strftime('%Y/%m/%d %H:%M:%S')





