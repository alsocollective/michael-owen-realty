var app = {
	options: {

	},

	init: function() {
		//ajax load pages
		//location on page tracking
		//google analytics
		//if of size use the mobile dropdown menue
		$("#navbutton").click(app.togglemenue);
	},
	togglemenue: function(event) {
		$("nav").toggleClass("medium-hide");
		console.log("toggleClass");
	},
	about: {
		init: function() {
			$('.reference').slick({
				dots: true,
				arrows: false
			});
		}
	},

	search: {
		init: function() {
			app.search.setuppriceSlider();
			app.search.setupBedSlider();
			app.search.setupBathSlider();
		},
		setuppriceSlider: function() {
			var priceslider = $("#priceslider");
			priceslider.noUiSlider({
				start: [0, 400000],
				connect: true,
				behaviour: 'drag',
				range: {
					'min': [0],
					'max': [1500000]
				},
				format: wNumb({
					mark: '.',
					decimals: 0,
					thousand: ',',
					prefix: '$ '
				}),
				step: 10000
			});
			priceslider.Link("lower").to($("#lowerprice"));
			priceslider.Link("upper").to($("#upperprice"));
		},
		setupBedSlider: function() {
			var priceslider = $("#bedslider");
			priceslider.noUiSlider({
				start: [1, 3],
				connect: true,
				behaviour: 'drag',
				range: {
					'min': [1],
					'max': [10]
				},
				format: wNumb({
					mark: '.',
					decimals: 0,
				}),
				step: 1
			});
			priceslider.Link("lower").to($("#lowerbed"));
			priceslider.Link("upper").to($("#upperbed"));
		},
		setupBathSlider: function() {
			var priceslider = $("#bathslider");
			priceslider.noUiSlider({
				start: [1, 3],
				connect: true,
				behaviour: 'drag',
				range: {
					'min': [1],
					'max': [10]
				},
				format: wNumb({
					mark: '.',
					decimals: 1,
				}),
				step: 0.5
			});
			priceslider.Link("lower").to($("#lowerbath"));
			priceslider.Link("upper").to($("#upperbath"));
		}
	},

	sell: {
		init: function() {
			console.log("sell setting up");
		}
	},



}