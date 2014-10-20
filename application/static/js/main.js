// Still working on the history change...

var app = {
	options: {
		loadingpage: false,
		pagetransitiontime: 1000,
		previousURL: null,
		slickinstance: null
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
			// url = app.url.addajax(url);
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
				}, app.options.pagetransitiontime * 2);
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
		},
		splashsize: function() {
			$("#splash, #smallsplash").height($(window).height() - 100);
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
		setupPagescroll: function(className) {
			var els = $(className + " h2");
			els.waypoint(app.url.setSectionAsHash, {
				context: '.mainwrapper'
			});
		},
		setSectionAsHash: function(event) {
			return false; //THIS IS here becuase we are no longer using this function
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
			app.nav.splashsize();
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
			app.search.setupDeletinputonselect();
			app.nav.splashsize();
			app.search.setupResultsSlick();
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
			$("#morelistings").removeClass("hide");
			$("#morelistings input")[0].value = value + from;
		},
		loadInitialContent: function(event) {
			var data = $(".filterform"),
				test = app.search.checkifinputisgood(data);
			$(".erroronsearch").removeClass("erroronsearch");
			if (test != false) {
				for (var a = 0, max = test.length; a < max; ++a) {
					$(".filterform ." + test[a]).addClass("erroronsearch");
					console.log(test[a]);
				}
				return false;
			}
			data = data.serialize();
			app.search.updatefrom(data);
			data['csrfmiddlewaretoken'] = propertySettings.csrftoken;
			$.ajax({
				type: "POST",
				url: '/proplist/',
				data: data,
				success: app.search.loadsuccess
			});
		},
		checkifinputisgood: function(datain) {
			var toreturn = false,
				price1 = parseInt(datain.find("#lowerprice").val().replace(",", "").replace(",", "").replace("$", "")),
				price2 = parseInt(datain.find("#upperprice").val().replace(",", "").replace(",", "").replace("$", "")),
				bed1 = parseInt(datain.find("#lowerbed").val()),
				bed2 = parseInt(datain.find("#upperbed").val()),
				bath1 = parseFloat(datain.find("#lowerbath").val()),
				bath2 = parseFloat(datain.find("#upperbath").val()),
				neightbourhoods = datain.find(".neighbourhoodslist :checked");

			if (price2 - price1 < 100000) {
				toreturn = app.search.addtoreturn(toreturn, "priceselector");
			}
			if (bed2 - bed1 < 1) {
				toreturn = app.search.addtoreturn(toreturn, "bedroomselector");
			}
			if (bath2 - bath1 < 1) {
				toreturn = app.search.addtoreturn(toreturn, "bathroomselector");
			}
			if (neightbourhoods.length > 0 && neightbourhoods.length < 3) {
				toreturn = app.search.addtoreturn(toreturn, "neighbourhoodslist");
			}
			return toreturn;
		},
		addtoreturn: function(out, variable) {
			if (out == false) {
				out = [variable]
			} else {
				out.push(variable)
			}
			return out
		},
		loadsuccess: function(responce) {
			// var removeel = $("#searchresults ul");
			// for (var a = 1, max = removeel.length; a < max; ++a) {
			// 	console.log(removeel)
			// 	removeel[a].parentNode.removeChild(removeel[a]);
			// }
			var count = app.search.loadedlength();

			while (count > 1) {
				app.options.searchresults.slickRemove(count - 1);
				count = app.search.loadedlength();
			}
			app.options.searchresults.slickAdd("<div><ul class='propertylist leftmargin'>" + responce + "</ul></div>");
			app.options.searchresults.slickGoTo(app.search.loadedlength() - 1);
			// $("#searchresults ul").html(responce);
			app.property.setup()
		},
		loadedlength: function() {
			return ($("#searchresults .slick-track .slick-slide").length - 2);
		},
		loadsuccessappend: function(responce, second, third) {
			if (responce.length < 100) {
				$("#morelistings").addClass("hide")
				return false;
			}
			// var newdiv = $(document.createElement("ul"));
			// newdiv.addClass("propertylist leftmargin");
			// $(newdiv).html(responce);
			// $("#searchresults > div").before(newdiv);
			app.options.searchresults.slickAdd("<div><ul class='propertylist leftmargin'>" + responce + "</ul></div>");
			app.options.searchresults.slickGoTo(app.search.loadedlength() - 1);
			app.search.gotosearchlistings();
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
				margin: 100000,
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
				margin: 1,
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
				margin: 1,
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
		},
		setupDeletinputonselect: function() {
			$('input').click(app.search.deletinputonselect);
		},
		deletinputonselect: function(event) {
			this.value = "";
		},
		setupResultsSlick: function() {
			app.options.searchresults = $("#searchresults").slick({
				adaptiveHeight: true
			});

		},
		gotosearchlistings: function() {
			$(".mainwrapper").animate({
				scrollTop: ($("#searchlistings").offset().top * -1)
			}, 1000);
		}
	},
	sell: {
		init: function() {
			console.log("sell setting up");
			app.sell.slicksetup();
			app.nav.splashsize();
		},
		slicksetup: function() {
			$(".pullquotes").slick({
				dots: true,
				arrows: false,
				slidesToShow: 1,
				adaptiveHeight: false
			});
		}
	},
	property: {
		init: function() {
			if (!$(".module").hasClass("moduleindex")) {
				$(".module").click(app.property.deleteprop);
			}
			$(".module > div > div").click(app.property.stopprop);
			app.property.resizemap();
			app.property.coppyInit();
			app.email.init();
			app.property.exitbutton();
			$(".module").addClass("loaded")
		},
		exitbutton: function() {
			$('#exbutton > div, .closebigbutton').click(app.property.exitbuttonexit);
		},
		exitbuttonexit: function(event) {
			var el = this.parentNode.parentNode.parentNode.parentNode.parentNode;
			if (el && el.parentNode) {
				el.parentNode.removeChild(el)
			}
		},
		initslick: function() {
			function resizezero() {
				app.options.slickinstance[0].slick.setPosition();
			}
			app.options.slickinstance = $('.propertyimages').slick({
				dots: false,
				arrows: true,
				slidesToShow: 1,
				adaptiveHeight: true
			});
			$('.propertyimages img').load(resizezero);
		},
		resizemap: function() {
			var iframe = $("#gmap iframe");
			iframe.height(iframe.width() * 0.8);
		},
		deleteprop: function() {
			if (this.parentNode) {
				this.parentNode.removeChild(this);
				location.hash = "";
			}
		},
		setup: function() {
			$(".propertylist li.new").click(app.property.loadproperty).each(app.property.removenewclass);
			app.property.coppyInit();
			$(".share").click(app.property.toggleclicked);
		},
		removenewclass: function() {
			$(this).removeClass("new");
		},
		toggleclicked: function(event) {
			event.preventDefault();
			$(this).toggleClass("clicked")
			return false;
		},
		loadproperty: function(event, hash) {
			if (event) {
				event.preventDefault();
				if ($(event.target).hasClass("emaillink") || $(event.target).hasClass("twitterlink") || $(event.target).hasClass("coppylink") || $(event.target).hasClass("share") || event.target.innerHTML == "share") {
					return false;
				}
			}
			var that = $(this).find("a")[0];
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
			event.stopPropagation();
			return false;
		},
		stopprop: function(event) {
			if (!$(event.target).hasClass("emaillink")) {
				event.stopPropagation();
			}
		},
		loadedproperty: function(response, status, xhr) {
			app.property.init();
			location.hash = $(".module > div")[0].id;
		},
		loadrestofphotos: function(popid) {
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
			if(selected.length==0){
				return false;
			}
			selected.click(app.property.coppyclicked);
			var client = new ZeroClipboard(selected);
			client.on("copy", function(event) {
				console.log(event.target.href)
				var clipboard = event.clipboardData;
				clipboard.setData("text/plain", event.target.href);
			})
			var cliplink = document.createElement("div");
			var linkh3 = document.createElement("h3");
		},
		coppyText: function(text) {
			var parent = document.createElement("div"),
				child = document.createElement("p");
			parent.appendChild(child);
			parent.className = "overlaycopytext";
			child.innerHTML = 'coppied to clipboard:<br>"' + text + '"';
			document.body.appendChild(parent);
			setTimeout(app.property.deleteCoppyText, app.options.pagetransitiontime);
		},
		deleteCoppyText: function() {
			var el = $(".overlaycopytext")[0];
			el.parentNode.removeChild(el);
		},
		coppyclicked: function(event) {
			event.preventDefault();
			event.stopPropagation();
			console.log($(".overlaycopytext").length)
			if ($(".overlaycopytext").length == 0) {
				app.property.coppyText(this.href)
			}
			return false;
		}
	},
	email: {
		init: function() {
			$(".emailsubmit").click(app.email.submit);
		},
		submit: function(event) {
			event.stopImmediatePropagation();
			event.preventDefault();
			var data = $(this.parentNode).serialize();
			data['csrfmiddlewaretoken'] = app.email.csrftoken;
			$(this.parentNode).addClass("hide").removeClass("requestform");
			$.ajax({
				type: "POST",
				url: '/sendemail/',
				data: data,
				success: app.email.submitsuccess,
				error: app.email.error
			});
			return false;
		},
		submitsuccess: function(replied) {
			// alert(replied.message);
			console.log(replied);
			var message = document.createElement("div");
			message.className = replied.status + " message";
			var h3 = document.createElement("h3");
			h3.innerHTML = replied.message;
			message.appendChild(h3);
			$(".request").append(message)
			$(".requestform").addClass("hideform")

		},
		error: function(message) {
			console.log("ERER")
			console.log(message)
		}
	},
	resize: function() {
		app.nav.correctSize();
		app.property.resizemap();
		app.nav.splashsize();
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