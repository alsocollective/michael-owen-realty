// Still working on the history change...

var app = {
	options: {
		loadingpage: false,
		pagetransitiontime: 1000,
		previousURL: null
		// currentPage: "home"
	},
	init: function() {
		//ajax load pages
		$("nav a").click(app.nav.navmenueclick);

		//location on page tracking
		app.url.init();

		//google analytics

		//if of size use the mobile dropdown menue
		$("#navbutton").click(app.nav.togglemenue);
		app.url.setupPagescroll(".mainwrapper");

		app.resize();
		$(window).resize(app.resize);
		// $(window).on("hashchange", app.url.gotohash);
		$(window).on("popstate", app.url.changepage);
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
				app.nav.loadpage(this.href)
				if ($("#navbutton").hasClass("navactive")) {
					app.nav.togglemenue();
				}
				return false;
			}
		},
		loadpage: function(url, donotsethistory) {
			// if (app.url.currentpage(url)) {
			// 	return false;
			// }
			app.options.loadingpage = true;
			if (!donotsethistory) {
				app.url.seturlfromfull(url);
			} else {
				var location = url.split("/"),
					name = location[location.length - 1],
					location = "/" + name;
				app.nav.changeurl(location);
			}
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
				app.url.gotohashlocation();
				app.options.previousURL = document.URL.split("#")[0];
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
		init: function() {
			// var url = document.URL.split("#")[0].split("/")
			// if (url.length < 5) {
			// 	url = "home";
			// } else {
			// 	url = url[url.length - 2]
			// }
			// app.options.currentPage = url;
			app.options.previousURL = document.URL.split("#")[0];
			app.url.gotohashlocation();
		},
		seturlfromfull: function(location) {
			var location = location.split("/"),
				name = location[location.length - 1],
				location = "/" + name;
			window.history.pushState({
				id: name,
				path: location
			}, name, location);
			app.nav.changeurl(location);
			// if (app.options.newhash && $("#" + app.options.newhash).length > 0) {
			// 	location.hash = app.options.newhash
			// 	app.options.newhash = null;
			// }
			return false;
		},
		addajax: function(url) {
			var spliturl = url.split("/");
			if (spliturl[spliturl.length - 1] == "" && spliturl.length < 5) {
				spliturl[spliturl.length - 1] = "home";
			}
			var appendstring = "ajax";
			if (spliturl.length < 5) {
				spliturl[spliturl.length - 1] = appendstring + spliturl[spliturl.length - 1];
			} else {
				spliturl[spliturl.length - 2] = appendstring + spliturl[spliturl.length - 2];
				spliturl[spliturl.length - 1] = "";
			}
			return spliturl.join("/");
		},
		setupPagescroll: function(className) {
			var els = $(className + " h2");
			els.waypoint(app.url.setSectionAsHash, {
				context: '.mainwrapper'
			});
		},
		setSectionAsHash: function() {
			console.log("new subsection");
			// location.hash = app.url.slugify(this.innerHTML);
		},
		slugify: function(Text) {
			return Text
				.toLowerCase()
				.replace(/ /g, '-')
				.replace(/[^\w-]+/g, '');
		},
		gotohashlocation: function() {
			var gotoEl = $(location.hash);
		},
		changepage: function() {
			app.nav.loadpage(document.URL, true);
		}
		// urlChange: function(event) {
		// 	console.log("=-- url change --=");
		// 	var splited = document.URL.split("#");
		// 	if (splited.length > 0) {
		// 		app.options.newhash = splited[1]
		// 	}
		// 	return false;
		// 	if (document.URL.indexOf("#") > 0) {
		// 		app.url.hashchange();
		// 	} else {
		// 		app.url.fullurlchange();
		// 	}
		// },
		// fullurlchange: function() {
		// 	console.log("page change");
		// 	app.nav.loadpage(document.URL, true);
		// },
		// hashchange: function(event) {
		// 	console.log("hash state change");
		// 	console.log(document.URL.split("#")[0], app.options.previousURL);
		// 	if (document.URL.split("#")[0] == app.options.previousURL) {
		// 		console.log("gotohash location")
		// 		app.url.gotohashlocation();
		// 	} else {
		// 		console.log("differnt URL");
		// 		app.nav.loadpage(document.URL.split("#")[0]);
		// 	}
		// 	// app.options.newhash = document.URL.split("#")[1]



		// 	// console.log("+-- hash change --+")
		// 	// console.log(event);
		// 	// console.log(document.URL);
		// 	// if (app.options.loadingpage) {
		// 	// 	event.preventDefault();
		// 	// 	return false;
		// 	// }
		// 	// app.nav.loadpage(document.URL, true);
		// },
		// currentpage: function(location) {
		// 	console.log("+-- current page --+")
		// 	if (location.split("#").length) {
		// 		console.log("true");
		// 		return true
		// 	}
		// 	console.log("false");
		// 	return false;
		// },
		// gotohash: function(event) {
		// 	var split = document.URL.split("#");
		// 	if (split.length > 0) {
		// 		$.waypoints('disable')
		// 		$('html,body').animate({
		// 			scrollTop: $("#" + split[1]).offset().top
		// 		}, 0, function() {
		// 			$.waypoints('enable')
		// 		});
		// 	}
		// }
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
			$(".module > div > div").click(app.property.stopprop);
		},
		delete: function() {
			this.parentNode.removeChild(this);
		},
		setup: function() {
			$(".propertylist li").click(app.property.loadproperty);
		},
		loadproperty: function(event) {
			if (app.options.loadingpage) {
				return false;
			}
			var newEl = document.createElement("div");
			newEl.className = "module";
			document.body.appendChild(newEl);
			$(newEl).load("/ajaxproperty", app.property.loadedproperty);
		},
		stopprop: function(event) {
			event.stopPropagation();
		},
		loadedproperty: function(response, status, xhr) {
			app.property.init();
		}
	},
	resize: function() {
		app.nav.correctSize();
	}
}