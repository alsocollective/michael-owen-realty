var app = {
	options: {
		loadingpage: false,
		pagetransitiontime: 1000
	},
	init: function() {

		//ajax load pages
		$("nav a").click(app.nav.navmenueclick);

		//location on page tracking
		app.url.gotohashlocation();

		//google analytics

		//if of size use the mobile dropdown menue
		$("#navbutton").click(app.nav.togglemenue);
		app.url.setupPagescroll(".mainwrapper");

		app.resize();
		$(window).resize(app.resize);

		$(window).on("hashchange", function() {
			console.log("hash changed");
		})

	},
	nav: {
		navmenueclick: function(event) {
			if (!this.href || !event.preventDefault) {
				return false;
			}
			var href = this.href,
				test = href.split(":")[0];
			if (test != "mailto" && test != "tel") {
				if (app.options.loadingpage) {
					event.preventDefault();
					return false;
				}
				app.options.loadingpage = true;
				app.nav.loadpage(this.href)
				if ($("#navbutton").hasClass("navactive")) {
					app.nav.togglemenue();
				}
				return false;
			}
		},
		loadpage: function(url) {
			app.url.seturlfromfull(url);
			url = app.url.addajax(url);
			var newMainContainer = document.createElement("div");
			newMainContainer.className = "mainwrapper offright";
			document.body.appendChild(newMainContainer);
			$(newMainContainer).load(url, function(response, status, xhr) {
				$.waypoints('destroy');
				var wrappers = $(".mainwrapper"),
					oldW = $(wrappers[0]),
					newW = $(wrappers[1]);
				oldW.addClass('offleft');
				newW.removeClass('offright');
				app.nav.deleteEl(oldW[0], app.options.pagetransitiontime);
			});
		},
		deleteEl: function(element, time) {
			setTimeout(function() {
				app.options.loadingpage = false;
				element.parentNode.removeChild(element);
				app.url.setupPagescroll(".mainwrapper")
			}, time);
		},
		togglemenue: function(event) {
			$("nav").toggleClass("offleft");
			$("#navbutton").toggleClass("navactive");
		},
		changeurl: function(link) {
			$(".currentpage").removeClass("currentpage");
			$($('a[href="' + link + '"]')[0].parentNode).addClass("currentpage")
		},
		correctSize: function() {
			$("#nav").width($($(".mainwrapper div")[0]).width());
		}
	},
	url: {
		seturlfromfull: function(location) {
			var location = location.split("/");
			location = "/" + location[location.length - 1];
			window.history.pushState("", "", location);
			app.nav.changeurl(location);
		},
		addajax: function(url) {
			var spliturl = url.split("/");
			if (spliturl[spliturl.length - 1] == "") {
				spliturl[spliturl.length - 1] = "home";
			}
			spliturl[spliturl.length - 1] = "ajax" + spliturl[spliturl.length - 1];
			return spliturl.join("/");
		},
		setupPagescroll: function(className) {
			var els = $(className + " h2");
			els.waypoint(app.url.setSectionAsHash, {
				context: '.mainwrapper'
			});
		},
		setSectionAsHash: function() {
			location.hash = app.url.slugify(this.innerHTML);
		},
		slugify: function(Text) {
			return Text
				.toLowerCase()
				.replace(/ /g, '-')
				.replace(/[^\w-]+/g, '');
		},
		gotohashlocation: function() {
			var gotoEl = $(location.hash);
		}
	},
	about: {
		init: function() {
			$('.reference').slick({
				dots: true,
				arrows: false
			});
			app.property.setup()
		}
	},
	search: {
		init: function() {
			app.search.setuppriceSlider();
			app.search.setupBedSlider();
			app.search.setupBathSlider();
			app.property.setup()
			app.search.neighbourhoodSetup();
		},
		setuppriceSlider: function() {
			var priceslider = $(".offright #priceslider");
			if (priceslider.length == 0) {
				priceslider = $("#priceslider")
			}
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
			var priceslider = $(".offright #bedslider");
			if (priceslider.length == 0) {
				priceslider = $("#bedslider")
			}
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
			var priceslider = $(".offright #bathslider");
			if (priceslider.length == 0) {
				priceslider = $("#bathslider")
			}
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
		},
		neighbourhoodSetup: function() {
			$("#neighbourhoods a").click(app.search.neighbourhoodClick) 
		},
		neighbourhoodClick: function(event) {
			console.log(this.href);
			$('#neighbourhoodajax').load(this.href);
			event.preventDefault();
			return false;
		}
	},
	sell: {
		init: function() {
			console.log("sell setting up");
		}
	},
	property: {
		init: function() {
			$('.propertyimages').slick({
				dots: true,
				arrows: false
			});
			$(".module").click(app.property.delete);
		},
		delete: function() {
			console.log(this);
			this.parentNode.removeChild(this);
		},
		setup: function() {
			$(".propertylist li").click(app.property.loadproperty);
		},
		loadproperty: function(event) {
			if (app.options.loadingpage) {
				console.log("already loading page");
				return false;
			}
			var newEl = document.createElement("div");
			newEl.className = "module";
			document.body.appendChild(newEl);
			$(newEl).load("/ajaxproperty", app.property.loadedproperty);
		},
		loadedproperty: function(response, status, xhr) {
			app.property.init();
		}
	},
	resize: function() {
		app.nav.correctSize();
	}
}