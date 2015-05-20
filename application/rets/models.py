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

class CondoProperty(models.Model):
	Address = models.TextField(max_length=1000, blank=True)	
	AirConditioning = models.TextField(max_length=1000, blank=True)
	AllInclusive = models.TextField(max_length=1000, blank=True)
	ApproxAge = models.TextField(max_length=1000, blank=True)
	ApproxSquareFootage = models.TextField(max_length=1000, blank=True)
	AptUnit = models.TextField(max_length=1000, blank=True)
	Area = models.TextField(max_length=1000, blank=True)
	AreaCode = models.FloatField(blank=True,null=True)
	Assessment = models.TextField(max_length=1000, blank=True)
	AssessmentYear = models.TextField(max_length=1000, blank=True)
	Balcony = models.TextField(max_length=1000, blank=True)
	Basement1 = models.TextField(max_length=1000, blank=True)
	Basement2 = models.TextField(max_length=1000, blank=True)
	Bedrooms = models.FloatField(blank=True,null=True)
	BedroomsPlus = models.FloatField(blank=True,null=True)
	BuildingAmenities1 = models.TextField(max_length=1000, blank=True)
	BuildingAmenities2 = models.TextField(max_length=1000, blank=True)
	BuildingAmenities4 = models.TextField(max_length=1000, blank=True)
	BuildingAmenities5 = models.TextField(max_length=1000, blank=True)
	BuildingAmenities6 = models.TextField(max_length=1000, blank=True)
	BuildingAmenties3 = models.TextField(max_length=1000, blank=True)
	BuildingInsuranceIncluded = models.TextField(max_length=1000, blank=True)
	CableTVIncluded = models.TextField(max_length=1000, blank=True)
	CacIncluded = models.TextField(max_length=1000, blank=True)
	CentralVac = models.TextField(max_length=1000, blank=True)
	CommonElementsIncluded = models.TextField(max_length=1000, blank=True)
	Community = models.TextField(max_length=1000, blank=True)
	CommunityCode = models.TextField(max_length=1000, blank=True)
	CondoCorp = models.FloatField(blank=True,null=True)
	CondoRegistryOffice = models.TextField(max_length=1000, blank=True)
	CondoTaxesIncluded = models.TextField(max_length=1000, blank=True)
	DirectionsCrossStreets = models.TextField(max_length=1000, blank=True)
	DisplayAddressOnInternet = models.TextField(max_length=1000, blank=True)
	Elevator = models.TextField(max_length=1000, blank=True)
	EnsuiteLaundry = models.TextField(max_length=1000, blank=True)
	Exposure = models.TextField(max_length=1000, blank=True)
	Exterior1 = models.TextField(max_length=1000, blank=True)
	Exterior2 = models.TextField(max_length=1000, blank=True)
	Extras = models.TextField(max_length=1000, blank=True)
	FamilyRoom = models.TextField(max_length=1000, blank=True)
	FireplaceStove = models.TextField(max_length=1000, blank=True)
	Furnished = models.TextField(max_length=1000, blank=True)
	GarageParkSpaces = models.TextField(max_length=1000, blank=True)
	GarageType = models.TextField(max_length=1000, blank=True)
	HeatIncluded = models.TextField(max_length=1000, blank=True)
	HeatSource = models.TextField(max_length=1000, blank=True)
	HeatType = models.TextField(max_length=1000, blank=True)
	HydroIncluded = models.TextField(max_length=1000, blank=True)
	IdxUpdtedDt = models.TextField(max_length=1000, blank=True)
	Kitchens = models.TextField(max_length=1000, blank=True)
	KitchensPlus = models.TextField(max_length=1000, blank=True)
	LaundryAccess = models.TextField(max_length=1000, blank=True)
	LaundryLevel = models.TextField(max_length=1000, blank=True)
	LeaseTerm = models.TextField(max_length=1000, blank=True)
	Level = models.TextField(max_length=1000, blank=True)
	Level1 = models.TextField(max_length=1000, blank=True)
	Level10 = models.TextField(max_length=1000, blank=True)
	Level11 = models.TextField(max_length=1000, blank=True)
	Level12 = models.TextField(max_length=1000, blank=True)
	Level2 = models.TextField(max_length=1000, blank=True)
	Level3 = models.TextField(max_length=1000, blank=True)
	Level4 = models.TextField(max_length=1000, blank=True)
	Level5 = models.TextField(max_length=1000, blank=True)
	Level6 = models.TextField(max_length=1000, blank=True)
	Level7 = models.TextField(max_length=1000, blank=True)
	Level8 = models.TextField(max_length=1000, blank=True)
	Level9 = models.TextField(max_length=1000, blank=True)
	ListBrokerage = models.TextField(max_length=1000, blank=True)
	ListPrice = models.FloatField(blank=True,null=True)
	Locker = models.TextField(max_length=1000, blank=True)
	LockerNum = models.TextField(max_length=1000, blank=True)
	Maintenance = models.TextField(max_length=1000, blank=True)
	Map = models.FloatField(blank=True,null=True)
	MapColumn = models.FloatField(blank=True,null=True)
	MapRow = models.TextField(max_length=1000, blank=True)
	MLS = models.TextField(max_length=1000, blank=True)
	Municipality = models.TextField(max_length=1000, blank=True)
	MunicipalityCode = models.TextField(max_length=1000, blank=True)
	MunicipalityDistrict = models.TextField(max_length=1000, blank=True)
	OutofAreaMunicipality = models.TextField(max_length=1000, blank=True)
	ParcelId = models.TextField(max_length=1000, blank=True)
	ParkCostMo = models.TextField(max_length=1000, blank=True)
	ParkingDrive = models.TextField(max_length=1000, blank=True)
	ParkingIncluded = models.TextField(max_length=1000, blank=True)
	ParkingLegalDescription = models.TextField(max_length=1000, blank=True)
	ParkingLegalDescription2 = models.TextField(max_length=1000, blank=True)
	ParkingSpaces = models.FloatField(blank=True,null=True)
	ParkingSpot1 = models.TextField(max_length=1000, blank=True)
	ParkingSpot2 = models.TextField(max_length=1000, blank=True)
	ParkingType = models.TextField(max_length=1000, blank=True)
	ParkingType2 = models.TextField(max_length=1000, blank=True)
	PetsPermitted = models.TextField(max_length=1000, blank=True)
	PixUpdtedDt = models.TextField(max_length=1000, blank=True)
	PostalCode = models.TextField(max_length=1000, blank=True)
	PrivateEntrance = models.TextField(max_length=1000, blank=True)
	PropertyFeatures1 = models.TextField(max_length=1000, blank=True)
	PropertyFeatures2 = models.TextField(max_length=1000, blank=True)
	PropertyFeatures3 = models.TextField(max_length=1000, blank=True)
	PropertyFeatures4 = models.TextField(max_length=1000, blank=True)
	PropertyFeatures5 = models.TextField(max_length=1000, blank=True)
	PropertyFeatures6 = models.TextField(max_length=1000, blank=True)
	Province = models.TextField(max_length=1000, blank=True)
	RemarksForClients = models.TextField(max_length=1000, blank=True)
	Retirement = models.TextField(max_length=1000, blank=True)
	Room1 = models.TextField(max_length=1000, blank=True)
	Room10 = models.TextField(max_length=1000, blank=True)
	Room10Desc1 = models.TextField(max_length=1000, blank=True)
	Room10Desc2 = models.TextField(max_length=1000, blank=True)
	Room10Desc3 = models.TextField(max_length=1000, blank=True)
	Room10Length = models.TextField(max_length=1000, blank=True)
	Room10Width = models.TextField(max_length=1000, blank=True)
	Room11 = models.TextField(max_length=1000, blank=True)
	Room11Desc1 = models.TextField(max_length=1000, blank=True)
	Room11Desc2 = models.TextField(max_length=1000, blank=True)
	Room11Desc3 = models.TextField(max_length=1000, blank=True)
	Room11Length = models.TextField(max_length=1000, blank=True)
	Room11Width = models.TextField(max_length=1000, blank=True)
	Room12 = models.TextField(max_length=1000, blank=True)
	Room12Desc1 = models.TextField(max_length=1000, blank=True)
	Room12Desc2 = models.TextField(max_length=1000, blank=True)
	Room12Desc3 = models.TextField(max_length=1000, blank=True)
	Room12Length = models.TextField(max_length=1000, blank=True)
	Room12Width = models.TextField(max_length=1000, blank=True)
	Room1Desc1 = models.TextField(max_length=1000, blank=True)
	Room1Desc2 = models.TextField(max_length=1000, blank=True)
	Room1Desc3 = models.TextField(max_length=1000, blank=True)
	Room1Length = models.TextField(max_length=1000, blank=True)
	Room1Width = models.TextField(max_length=1000, blank=True)
	Room2 = models.TextField(max_length=1000, blank=True)
	Room2Desc1 = models.TextField(max_length=1000, blank=True)
	Room2Desc2 = models.TextField(max_length=1000, blank=True)
	Room2Desc3 = models.TextField(max_length=1000, blank=True)
	Room2Length = models.TextField(max_length=1000, blank=True)
	Room2Width = models.TextField(max_length=1000, blank=True)
	Room3 = models.TextField(max_length=1000, blank=True)
	Room3Desc1 = models.TextField(max_length=1000, blank=True)
	Room3Desc2 = models.TextField(max_length=1000, blank=True)
	Room3Desc3 = models.TextField(max_length=1000, blank=True)
	Room3Length = models.TextField(max_length=1000, blank=True)
	Room3Width = models.TextField(max_length=1000, blank=True)
	Room4 = models.TextField(max_length=1000, blank=True)
	Room4Desc1 = models.TextField(max_length=1000, blank=True)
	Room4Desc2 = models.TextField(max_length=1000, blank=True)
	Room4Desc3 = models.TextField(max_length=1000, blank=True)
	Room4Length = models.TextField(max_length=1000, blank=True)
	Room4Width = models.TextField(max_length=1000, blank=True)
	Room5 = models.TextField(max_length=1000, blank=True)
	Room5Desc1 = models.TextField(max_length=1000, blank=True)
	Room5Desc2 = models.TextField(max_length=1000, blank=True)
	Room5Desc3 = models.TextField(max_length=1000, blank=True)
	Room5Length = models.TextField(max_length=1000, blank=True)
	Room5Width = models.TextField(max_length=1000, blank=True)
	Room6 = models.TextField(max_length=1000, blank=True)
	Room6Desc1 = models.TextField(max_length=1000, blank=True)
	Room6Desc2 = models.TextField(max_length=1000, blank=True)
	Room6Desc3 = models.TextField(max_length=1000, blank=True)
	Room6Length = models.TextField(max_length=1000, blank=True)
	Room6Width = models.TextField(max_length=1000, blank=True)
	Room7 = models.TextField(max_length=1000, blank=True)
	Room7Desc1 = models.TextField(max_length=1000, blank=True)
	Room7Desc2 = models.TextField(max_length=1000, blank=True)
	Room7Desc3 = models.TextField(max_length=1000, blank=True)
	Room7Length = models.TextField(max_length=1000, blank=True)
	Room7Width = models.TextField(max_length=1000, blank=True)
	Room8 = models.TextField(max_length=1000, blank=True)
	Room8Desc1 = models.TextField(max_length=1000, blank=True)
	Room8Desc2 = models.TextField(max_length=1000, blank=True)
	Room8Desc3 = models.TextField(max_length=1000, blank=True)
	Room8Length = models.TextField(max_length=1000, blank=True)
	Room8Width = models.TextField(max_length=1000, blank=True)
	Room9 = models.TextField(max_length=1000, blank=True)
	Room9Desc1 = models.TextField(max_length=1000, blank=True)
	Room9Desc2 = models.TextField(max_length=1000, blank=True)
	Room9Desc3 = models.TextField(max_length=1000, blank=True)
	Room9Length = models.TextField(max_length=1000, blank=True)
	Room9Width = models.TextField(max_length=1000, blank=True)
	Rooms = models.FloatField(blank=True,null=True)
	RoomsPlus = models.TextField(max_length=1000, blank=True)
	SaleLease = models.TextField(max_length=1000, blank=True)
	SharesPer = models.TextField(max_length=1000, blank=True)
	SpecialDesignation1 = models.TextField(max_length=1000, blank=True)
	SpecialDesignation2 = models.TextField(max_length=1000, blank=True)
	SpecialDesignation3 = models.TextField(max_length=1000, blank=True)
	SpecialDesignation4 = models.TextField(max_length=1000, blank=True)
	SpecialDesignation5 = models.TextField(max_length=1000, blank=True)
	SpecialDesignation6 = models.TextField(max_length=1000, blank=True)
	Status = models.TextField(max_length=1000, blank=True)
	Street = models.TextField(max_length=1000, blank=True)
	StreetAbbreviation = models.TextField(max_length=1000, blank=True)
	StreetDirection = models.TextField(max_length=1000, blank=True)
	StreetName = models.TextField(max_length=1000, blank=True)
	Style = models.TextField(max_length=1000, blank=True)
	Taxes = models.FloatField(blank=True,null=True)
	TaxYear = models.FloatField(blank=True,null=True)
	TimestampSql = models.TextField(max_length=1000, blank=True)
	TypeOwn1Out = models.TextField(max_length=1000, blank=True)
	TypeOwnSrch = models.TextField(max_length=1000, blank=True)
	Uffi = models.TextField(max_length=1000, blank=True)
	Unit = models.TextField(max_length=1000, blank=True)
	VirtualTourUploadDate = models.TextField(max_length=1000, blank=True)
	VirtualTourURL = models.TextField(max_length=1000, blank=True)
	Washrooms = models.FloatField(blank=True,null=True)
	WashroomsType1 = models.TextField(max_length=1000, blank=True)
	WashroomsType1Level = models.TextField(max_length=1000, blank=True)
	WashroomsType1Pcs = models.TextField(max_length=1000, blank=True)
	WashroomsType2 = models.TextField(max_length=1000, blank=True)
	WashroomsType2Level = models.TextField(max_length=1000, blank=True)
	WashroomsType2Pcs = models.TextField(max_length=1000, blank=True)
	WashroomsType3 = models.TextField(max_length=1000, blank=True)
	WashroomsType3Level = models.TextField(max_length=1000, blank=True)
	WashroomsType3Pcs = models.TextField(max_length=1000, blank=True)
	WashroomsType4 = models.TextField(max_length=1000, blank=True)
	WashroomsType4Level = models.TextField(max_length=1000, blank=True)
	WashroomsType4Pcs = models.TextField(max_length=1000, blank=True)
	WashroomsType5 = models.TextField(max_length=1000, blank=True)
	WashroomsType5Level = models.TextField(max_length=1000, blank=True)
	WashroomsType5Pcs = models.TextField(max_length=1000, blank=True)
	WaterIncluded = models.TextField(max_length=1000, blank=True)
	Zoning = models.TextField(max_length=1000, blank=True)

	numofphotos = models.IntegerField(blank=True,null=True)
	firstphoto = models.BooleanField(default=False)
	featured = 	models.DateTimeField(auto_now=False,blank=True,null=True)


	def admin_image(self):
		if self.firstphoto == False:
			if(os.path.isfile("%simages/%s-1.jpg"%(MEDIA_ROOT,self.MLS))):
				self.firstphoto = True
				self.save()
				
		if self.firstphoto:
			return '<img style="width:200px;height:auto;" src="/static/images/%s-1.jpg"/>' % self.MLS
		else:
			return '%s - has no image'%self.MLS
		# return '<img style="width:200px;height:auto;" src="http://www.also-static.com/alsocollective/uploaded/%s"/>' % self.title
	admin_image.allow_tags = True

	def __unicode__(self):
		return self.MLS

	def save(self,*args, **kwargs):
		# self.slug = slugify(self.title)
		if(os.path.isfile("%simages/%s-1.jpg"%(MEDIA_ROOT,self.MLS))):
			self.firstphoto = True
		else:
			self.firstphoto = False
		super(CondoProperty, self).save(*args, **kwargs)









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

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(NeightbourHood, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.title


class SearchPage(models.Model):
	locations = models.ManyToManyField(NeightbourHood,blank=True,null=True)
	footer = models.TextField(max_length=1000,blank=True,null=True)
	created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.created.strftime('%Y/%m/%d %H:%M:%S')





