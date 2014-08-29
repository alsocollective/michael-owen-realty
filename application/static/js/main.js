var app = {
	options: {

	},

	about: {
		init: function() {
			$('.reference').slick({dots: true, arrows:false});
			
		}

	},

	search: {
		init: function() {
			console.log("search setting up");
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
		callbohdan: function() {
			console.log("bohdan")
		}
	},

	sell: {
		init: function() {
			console.log("sell setting up");
		}
	}
}