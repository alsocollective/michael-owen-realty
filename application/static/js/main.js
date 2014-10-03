// Still working on the history change...

var app = {
	options: {
		loadingpage: false,
		pagetransitiontime: 1000,
		previousURL: null
	},
	init: function() {
		app.social.init();
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
				setTimeout(function() {
					newW.removeClass('offright');
				}, app.options.pagetransitiontime);
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
	social: {
		init: function() {
			$(".twitterlink").click(app.social.twitterLink);
		},
		twitterLink: function(event) {
			event.preventDefault();
			event.stopPropagation();
			var w = window.open(this.href, this.target || "_blank", 'menubar=no,toolbar=no,location=no,directories=no,status=no,scrollbars=no,resizable=no,dependent,width=475,height=248,left=0,top=0');
			// return w ? false : true;
			return false;
		}
	},
	url: {
		init: function() {
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
			app.options.previousURL = document.URL;
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
		setSectionAsHash: function(event) {
			if (event == "down") {
				if ($(this).hasClass("whitenav")) {
					$("#navbutton").addClass("white");
				} else {
					$("#navbutton").removeClass("white");
				}
			} else {
				if (!$(this).hasClass("whitenav")) {
					$("#navbutton").addClass("white");
				} else {
					$("#navbutton").removeClass("white");
				}
			}
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
		//returns the last element in a url
		//>>> "http://localhost:8000/buy/"
		//<<< "buy"
		findPage: function(baseurl) {
			var pagesplit = baseurl.split("/"),
				page = "",
				count = 1;
			while (page.length <= 0) {
				page = pagesplit[pagesplit.length - count]
				++count;
			}
			return page
		},
		currentPage: function() {
			if ($("#searchfield").length > 0) {
				return "search"
			} else if ($("#about").length > 0) {
				return "about"
			} else if ($(".sellingpage").length > 0) {
				return "sell"
			} else if ($(".buyingpage")) {
				return "buy"
			}
			return "Unknown"
		},
		changepage: function() {
			var url = document.URL.split("#"),
				newpage = app.url.findPage(url[0]),
				currentpage = app.url.currentPage();
			if (newpage.length > 8) {
				newpage = "about";
			}
			if (url.length > 1 && url[1].length > 1) {
				if (!$(".module")[0]) {
					app.property.loadproperty(null, url[1]);
				}
			} else if (currentpage != newpage) {
				console.log(currentpage, newpage)
				app.nav.loadpage(document.URL, true);
			} else {
				var el = $(".module");
				if (el.length > 0) {
					el = el[0]
					el.parentNode.removeChild(el);
				}
			}
			return false;
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
			app.search.initajax();
			app.search.setupCheckAllButtons();
		},
		initajax: function() {
			$("#searchlistings button").click(app.search.loadInitialContent);
			$("#morelistings").click(app.search.loadmorelistings);
		},
		loadmorelistings: function(value) {
			var data = $(this).find("input")[0].value;
			app.search.updatefrom(data);
			data['csrfmiddlewaretoken'] = propertySettings.csrftoken;
			$.ajax({
				type: "POST",
				url: '/proplist/',
				data: data,
				success: app.search.loadsuccessappend
			});
		},
		updatefrom: function(value) {
			var from = value.split("=");
			from = from[from.length - 1];
			value = value.substring(0, value.length - from.length);
			from = parseInt(from) + 12;
			$("#morelistings input")[0].value = value + from;
		},
		loadInitialContent: function(event) {
			var data = $(".filterform").serialize()
			app.search.updatefrom(data);
			data['csrfmiddlewaretoken'] = propertySettings.csrftoken;
			$.ajax({
				type: "POST",
				url: '/proplist/',
				data: data,
				success: app.search.loadsuccess
			});
		},
		loadsuccess: function(responce) {
			$("#searchresults ul").html(responce);
			app.property.setup()
		},
		loadsuccessappend: function(responce) {
			$("#searchresults ul").append(responce);
			app.property.setup()
		},
		responcefromInitialLoad: function(event) {
			console.log("submit was triggered")
		},
		setuppriceSlider: function() {
			var priceslider = $(".offright #priceslider a");
			if (priceslider.length == 0) {
				priceslider = $("#priceslider")
			}
			priceslider.noUiSlider({
				start: [0, 800000],
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
					'min': [propertySettings.bed.min],
					'max': [propertySettings.bed.max]
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
					'min': [propertySettings.bath.min],
					'max': [propertySettings.bath.max]
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
		},
		setupCheckAllButtons: function() {
			$(".filterform .bold").parent().find("input").change(app.search.checkAllRelatedCheckboxes);
		},
		checkAllRelatedCheckboxes: function(event) {
			if (this.checked) {
				$(this.parentNode.parentNode).find("input").each(app.search.makeCheck)
			} else {
				$(this.parentNode.parentNode).find("input").each(app.search.makeUnCheck)
			}

		},
		makeCheck: function(i, el) {
			el.checked = true;
		},
		makeUnCheck: function(i, el) {
			el.checked = false;
		}
	},
	sell: {
		init: function() {
			console.log("sell setting up");
		}
	},
	property: {
		init: function() {
			if (!$(".module").hasClass("moduleindex")) {
				$(".module").click(app.property.delete);
			}
			$(".module > div > div").click(app.property.stopprop);
			app.property.resizemap();
			app.property.coppyInit();
			app.email.init();
			app.property.exitbutton();
		},
		exitbutton: function() {
			$('#exbutton > div').click(app.property.exitbuttonexit);
		},
		exitbuttonexit: function(event) {
			this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode)
		},
		initslick: function() {
			$('.propertyimages').slick({
				dots: false,
				arrows: true,
				slidesToShow: 1,
				adaptiveHeight: true
			});
		},
		resizemap: function() {
			var iframe = $("#gmap iframe");
			iframe.height(iframe.width() * 0.8);
		},
		delete: function() {
			if (this.parentNode) {
				this.parentNode.removeChild(this);
				location.hash = "";
			}
		},
		setup: function() {
			$(".propertylist li a").click(app.property.loadproperty);
		},
		loadproperty: function(event, hash) {
			event.preventDefault();
			if ($(event.target).hasClass("twitterlink")) {
				return false;
			}
			var that = this;
			if (event) {
				event.preventDefault();
			} else {
				that.href = "/property/" + hash;
			}
			if (app.options.loadingpage) {
				return false;
			}
			var newEl = document.createElement("div");
			newEl.className = "module";
			document.body.appendChild(newEl);
			$(newEl).load(that.href, app.property.loadedproperty);
			return false;
		},
		stopprop: function(event) {
			event.stopPropagation();
		},
		loadedproperty: function(response, status, xhr) {
			app.property.init();
			location.hash = $(".module > div")[0].id;
		},
		loadrestofphotos: function(popid) {
			console.log(popid);
			$.ajax({
				dataType: "json",
				url: "/newimages/" + popid,
				success: app.property.addednewimages
			});
		},
		addednewimages: function(data, textstatus) {
			var out = "";
			for (var a = 1; a < data.count; ++a) {
				out += '<div><img src="/static/images/' + data.id + "-" + a + '.jpg"></div>';
			}
			$(".propertyimages").html(out);
			app.property.initslick();
		},
		coppyInit: function() {
			var selected = $(".coppylink");
			selected.click(app.property.coppyclicked)
			var client = new ZeroClipboard(selected);
			client.on("copy", function(event) {
				console.log(event.target);
				var clipboard = event.clipboardData;
				clipboard.setData("text/plain", event.target.href);
			})
		},
		coppyclicked: function(event) {
			event.preventDefault();
			return false;
		}
	},
	email: {
		init: function() {
			$(".emailsubmit").click(app.email.submit);
		},
		submit: function(event) {
			var data = $(this.parentNode).serialize();
			data['csrfmiddlewaretoken'] = app.email.csrftoken;
			$.ajax({
				type: "POST",
				url: '/sendemail/',
				data: data,
				success: app.email.submitsuccess,
				error: app.email.error
			});

			event.preventDefault();
			return false;
		},
		submitsuccess: function(replied) {
			console.log(replied);
		},
		error: function(message) {
			console.log(message)
		}
	},
	resize: function() {
		app.nav.correctSize();
		app.property.resizemap();
	},
	getCookie: function(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	},
	csrfSafeMethod: function(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
}