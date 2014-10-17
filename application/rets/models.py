from django.db import models
from django.template.defaultfilters import slugify

class ResidentialProperty(models.Model):
	acres = models.CharField(max_length=800, blank=True)
	addl_mo_fee = models.IntegerField(blank=True,null=True) 
	addr = models.CharField(max_length=5000, blank=True)
	a_c = models.CharField(max_length=3000, blank=True)
	all_inc = models.CharField(max_length=100, blank=True)
	yr_built = models.CharField(max_length=500, blank=True)
	sqft = models.CharField(max_length=900, blank=True)
	apt_num = models.CharField(max_length=500, blank=True)
	area = models.CharField(max_length=4000, blank=True)
	area_code = models.CharField(max_length=400, blank=True)
	tv = models.IntegerField(blank=True,null=True) 
	ass_year = models.IntegerField(blank=True,null=True) 
	bsmt1_out = models.CharField(max_length=3000, blank=True)
	bsmt2_out = models.CharField(max_length=3000, blank=True)
	br = models.IntegerField(blank=True,null=True) 
	br_plus = models.IntegerField(blank=True,null=True) 
	cable = models.CharField(max_length=100, blank=True)
	cac_inc = models.CharField(max_length=100, blank=True)
	central_vac = models.CharField(max_length=100, blank=True)
	comel_inc = models.CharField(max_length=100, blank=True)
	community = models.CharField(max_length=10000, blank=True)
	community_code = models.CharField(max_length=4000, blank=True)
	cross_st = models.CharField(max_length=4000, blank=True)
	disp_addr = models.CharField(max_length=100, blank=True)
	drive = models.CharField(max_length=4000, blank=True)
	elevator = models.CharField(max_length=700, blank=True)
	constr1_out = models.CharField(max_length=600, blank=True)
	constr2_out = models.CharField(max_length=700, blank=True)
	extras = models.CharField(max_length=50000, blank=True)
	den_fr = models.CharField(max_length=100, blank=True)
	farm_agri = models.CharField(max_length=200, blank=True)
	fpl_num = models.CharField(max_length=100, blank=True)
	comp_pts = models.CharField(max_length=100, blank=True)
	furnished = models.CharField(max_length=400, blank=True)
	gar_spaces = models.IntegerField(blank=True,null=True) 
	gar_type = models.CharField(max_length=2000, blank=True)
	heat_inc = models.CharField(max_length=100, blank=True)
	fuel = models.CharField(max_length=900, blank=True)
	heating = models.CharField(max_length=4000, blank=True)
	hydro_inc = models.CharField(max_length=100, blank=True)
	idx_dt = models.DateTimeField(auto_now=False,blank=True,null=True) 
	num_kit = models.IntegerField(blank=True,null=True) 
	kit_plus = models.IntegerField(blank=True,null=True) 
	laundry = models.CharField(max_length=300, blank=True)
	laundry_lev = models.CharField(max_length=500, blank=True)
	lease_term = models.CharField(max_length=4000, blank=True)
	legal_desc = models.CharField(max_length=10000, blank=True)
	level1 = models.CharField(max_length=800, blank=True)
	level10 = models.CharField(max_length=800, blank=True)
	level11 = models.CharField(max_length=800, blank=True)
	level12 = models.CharField(max_length=800, blank=True)
	level2 = models.CharField(max_length=800, blank=True)
	level3 = models.CharField(max_length=800, blank=True)
	level4 = models.CharField(max_length=800, blank=True)
	level5 = models.CharField(max_length=800, blank=True)
	level6 = models.CharField(max_length=800, blank=True)
	level7 = models.CharField(max_length=800, blank=True)
	level8 = models.CharField(max_length=800, blank=True)
	level9 = models.CharField(max_length=800, blank=True)
	rltr = models.CharField(max_length=4000, blank=True)
	lp_dol = models.IntegerField(blank=True,null=True) 
	depth = models.DecimalField(max_digits=6, decimal_places=2, blank=True,null=True)
	front_ft = models.DecimalField(max_digits=8, decimal_places=2, blank=True,null=True)
	irreg = models.CharField(max_length=100, blank=True)
	lotsz_code = models.CharField(max_length=800, blank=True)
	mmap_page = models.IntegerField(blank=True,null=True) 
	mmap_col = models.IntegerField(blank=True,null=True) 
	mmap_row = models.CharField(max_length=100, blank=True)
	ml_num = models.CharField(max_length=800, blank=True)
	municipality = models.CharField(max_length=4000, blank=True)
	municipality_district = models.CharField(max_length=2000, blank=True)
	municipality_code = models.CharField(max_length=4000, blank=True)
	oth_struc1_out = models.CharField(max_length=20000, blank=True)
	oth_struc2_out = models.CharField(max_length=20000, blank=True)
	outof_area = models.CharField(max_length=600, blank=True)
	park_chgs = models.DecimalField(max_digits=6, decimal_places=2, blank=True,null=True)
	prkg_inc = models.CharField(max_length=100, blank=True)
	park_spcs = models.IntegerField(blank=True,null=True) 
	parcel_id = models.CharField(max_length=900, blank=True)
	pix_updt = models.DateTimeField(auto_now=False,blank=True,null=True) 
	pool = models.CharField(max_length=800, blank=True)
	zip = models.CharField(max_length=700, blank=True)
	pvt_ent = models.CharField(max_length=100, blank=True)
	prop_feat1_out = models.CharField(max_length=2000, blank=True)
	prop_feat2_out = models.CharField(max_length=2000, blank=True)
	prop_feat3_out = models.CharField(max_length=2000, blank=True)
	prop_feat4_out = models.CharField(max_length=2000, blank=True)
	prop_feat5_out = models.CharField(max_length=2000, blank=True)
	prop_feat6_out = models.CharField(max_length=2000, blank=True)
	county = models.CharField(max_length=3000, blank=True)
	ad = models.CharField(max_length=500, blank=True)
	retirement = models.CharField(max_length=100, blank=True)
	rm1_out = models.CharField(max_length=900, blank=True)
	rm1_dc1_out = models.CharField(max_length=4000, blank=True)
	rm1_dc2_out = models.CharField(max_length=4000, blank=True)
	rm1_dc3_out = models.CharField(max_length=4000, blank=True)
	rm1_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm1_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm10_out = models.CharField(max_length=900, blank=True)
	rm10_dc1_out = models.CharField(max_length=4000, blank=True)
	rm10_dc2_out = models.CharField(max_length=4000, blank=True)
	rm10_dc3_out = models.CharField(max_length=4000, blank=True)
	rm10_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm10_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm11_out = models.CharField(max_length=900, blank=True)
	rm11_dc1_out = models.CharField(max_length=4000, blank=True)
	rm11_dc2_out = models.CharField(max_length=4000, blank=True)
	rm11_dc3_out = models.CharField(max_length=4000, blank=True)
	rm11_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm11_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm12_out = models.CharField(max_length=900, blank=True)
	rm12_dc1_out = models.CharField(max_length=4000, blank=True)
	rm12_dc2_out = models.CharField(max_length=4000, blank=True)
	rm12_dc3_out = models.CharField(max_length=4000, blank=True)
	rm12_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm12_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm2_out = models.CharField(max_length=900, blank=True)
	rm2_dc1_out = models.CharField(max_length=4000, blank=True)
	rm2_dc2_out = models.CharField(max_length=4000, blank=True)
	rm2_dc3_out = models.CharField(max_length=4000, blank=True)
	rm2_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm2_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm3_out = models.CharField(max_length=900, blank=True)
	rm3_dc1_out = models.CharField(max_length=4000, blank=True)
	rm3_dc2_out = models.CharField(max_length=4000, blank=True)
	rm3_dc3_out = models.CharField(max_length=4000, blank=True)
	rm3_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm3_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm4_out = models.CharField(max_length=900, blank=True)
	rm4_dc1_out = models.CharField(max_length=4000, blank=True)
	rm4_dc2_out = models.CharField(max_length=4000, blank=True)
	rm4_dc3_out = models.CharField(max_length=4000, blank=True)
	rm4_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm4_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm5_out = models.CharField(max_length=900, blank=True)
	rm5_dc1_out = models.CharField(max_length=4000, blank=True)
	rm5_dc2_out = models.CharField(max_length=4000, blank=True)
	rm5_dc3_out = models.CharField(max_length=4000, blank=True)
	rm5_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm5_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm6_out = models.CharField(max_length=900, blank=True)
	rm6_dc1_out = models.CharField(max_length=4000, blank=True)
	rm6_dc2_out = models.CharField(max_length=4000, blank=True)
	rm6_dc3_out = models.CharField(max_length=4000, blank=True)
	rm6_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm6_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm7_out = models.CharField(max_length=900, blank=True)
	rm7_dc1_out = models.CharField(max_length=4000, blank=True)
	rm7_dc2_out = models.CharField(max_length=4000, blank=True)
	rm7_dc3_out = models.CharField(max_length=4000, blank=True)
	rm7_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm7_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm8_out = models.CharField(max_length=900, blank=True)
	rm8_dc1_out = models.CharField(max_length=4000, blank=True)
	rm8_dc2_out = models.CharField(max_length=4000, blank=True)
	rm8_dc3_out = models.CharField(max_length=4000, blank=True)
	rm8_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm8_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm9_out = models.CharField(max_length=900, blank=True)
	rm9_dc1_out = models.CharField(max_length=4000, blank=True)
	rm9_dc2_out = models.CharField(max_length=4000, blank=True)
	rm9_dc3_out = models.CharField(max_length=4000, blank=True)
	rm9_len = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rm9_wth = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
	rms = models.IntegerField(blank=True,null=True) 
	rooms_plus = models.IntegerField(blank=True,null=True) 
	s_r = models.CharField(max_length=900, blank=True)
	vend_pis = models.CharField(max_length=4000, blank=True)
	sewer = models.CharField(max_length=2000, blank=True)
	spec_des1_out = models.CharField(max_length=900, blank=True)
	spec_des2_out = models.CharField(max_length=900, blank=True)
	spec_des3_out = models.CharField(max_length=900, blank=True)
	spec_des4_out = models.CharField(max_length=900, blank=True)
	spec_des5_out = models.CharField(max_length=900, blank=True)
	spec_des6_out = models.CharField(max_length=900, blank=True)
	status = models.CharField(max_length=100, blank=True)
	st_num = models.CharField(max_length=700, blank=True)
	st_sfx = models.CharField(max_length=400, blank=True)
	st_dir = models.CharField(max_length=100, blank=True)
	st = models.CharField(max_length=4000, blank=True)
	style = models.CharField(max_length=4000, blank=True)
	yr = models.IntegerField(blank=True,null=True) 
	taxes = models.DecimalField(max_digits=8, decimal_places=2, blank=True,null=True)
	type_own_srch = models.CharField(max_length=700, blank=True)
	type_own1_out = models.CharField(max_length=800, blank=True)
	uffi = models.CharField(max_length=200, blank=True)
	timestamp_sql = models.DateTimeField(auto_now=False,blank=True,null=True) 
	util_cable = models.CharField(max_length=100, blank=True)
	gas = models.CharField(max_length=100, blank=True)
	elec = models.CharField(max_length=100, blank=True)
	util_tel = models.CharField(max_length=100, blank=True)
	vtour_updt = models.URLField(max_length=300000,blank=True)
	tour_url = models.URLField(max_length=300000,blank=True)
	bath_tot = models.IntegerField(blank=True,null=True) 
	wcloset_t1 = models.IntegerField(blank=True,null=True) 
	wcloset_p1 = models.IntegerField(blank=True,null=True) 
	wcloset_t1lvl = models.CharField(max_length=800, blank=True)
	wcloset_t2 = models.IntegerField(blank=True,null=True) 
	wcloset_p2 = models.IntegerField(blank=True,null=True) 
	wcloset_t2lvl = models.CharField(max_length=800, blank=True)
	wcloset_t3 = models.IntegerField(blank=True,null=True) 
	wcloset_p3 = models.IntegerField(blank=True,null=True) 
	wcloset_t3lvl = models.CharField(max_length=800, blank=True)
	wcloset_t4 = models.IntegerField(blank=True,null=True) 
	wcloset_p4 = models.IntegerField(blank=True,null=True) 
	wcloset_t4lvl = models.CharField(max_length=800, blank=True)
	wcloset_t5 = models.IntegerField(blank=True,null=True) 
	wcloset_p5 = models.IntegerField(blank=True,null=True) 
	wcloset_t5lvl = models.CharField(max_length=800, blank=True)
	water = models.CharField(max_length=900, blank=True)
	water_inc = models.CharField(max_length=100, blank=True)
	wtr_suptyp = models.CharField(max_length=200, blank=True)
	waterfront = models.CharField(max_length=800, blank=True)
	zoning = models.CharField(max_length=1600, blank=True)
	numofphotos = models.IntegerField(blank=True,null=True)
	firstphoto = models.BooleanField(default=True)
	featured = 	models.DateTimeField(auto_now=False,blank=True,null=True) 


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

class listitem(models.Model):
	text = models.CharField(max_length=20000)
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
	text = models.CharField(max_length=20000)
	community = models.ManyToManyField('listitem',related_name='community_area', blank=True,null=True)
	subsections = models.ManyToManyField('Area',related_name='area-thing', blank=True,null=True)
	ward = models.BooleanField(default=False)
	# payloadText = models.CharField(max_length=20000)
	def __unicode__(self):
		return self.text

class EmailRmark(models.Model):
	ipaddress = models.IPAddressField()
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s %s"%(self.ipaddress, self.date.strftime('%H:%M:%S %m/%d/%Y'))