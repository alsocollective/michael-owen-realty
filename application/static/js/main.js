// alert("it worked!")

$("#priceslider").noUiSlider({
	start: [40, 50],
	connect: true,
	behaviour: 'drag',
	range: {
		'min': [0],
		'max': [100]
	}
});