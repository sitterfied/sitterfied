require({
    paths: {
        "require": "require/require",
        "cs": "require/cs",
        "ember": "lib/ember",
        "handlebars" : "lib/handlebars",
		"model": "lib/ember-model-latest",
        //"data": "lib/ember-data-latest",
        //"djangoRestAdapter": "lib/adapter",
		'waypoints': 'lib/waypoints',
        "ajaxfileupload": 'lib/ajaxfileupload.js',
        "_": "lib/underscore-min",
        "jquery": "lib/jquery-1.9.1",
        "jqueryui": "lib/jquery-ui-1.10.0.custom.min",
        "chosen": "lib/chosen.jquery.min",
        "select2": "lib/select2",
        'fancybox':'lib/jquery.fancybox.pack',
        'moment': 'lib/moment.min',
        'scrollto': 'lib/jquery.scrollTo-1.4.3.1-min',
		'imgareaselect': 'lib/jquery.imgareaselect.pack',
		'phoneformat': 'lib/PhoneFormat',
		'ucare': 'lib/uploadcare-1.0.0rc2.min',
        'purl': 'lib/purl',
        'subtab': 'sub-tab_active',
	'iemodal': 'lib/ie-popup'
    },
    waitSeconds: 0,

    shim:{
        data: {
            exports: 'DS',
            deps: ['ember'],
        },
        model: {
            deps: ['ember'],
        },

        jquery: {
            exports: "$",
        },
        ember: {
            exports: "Ember",
            deps: ['jquery']
        },
        handlebars: {
			deps: ['jquery'],
            exports: "Handlebars",
        },
        djangoRestAdapter: {
            deps: ['data'],
        },
        fancybox: {
            deps: ['jquery'],
        },
        scrollto: {
            deps: ['jquery'],
        },
        jqueryui: {
            deps: ['jquery']
        },
        _: {
            exports: "_",
        },
        moment: {
            exports: "moment",
        },
        chosen: {
            deps: ['jquery']
        },
        select2: {
            deps: ['jquery']
        },
		imgareaselect: {
            deps: ['jquery']
        },
		phoneformat: {
            deps: ['jquery']
        },
		ucare: {
            deps: ['jquery']
        },
        purl: {
            deps: ['jquery']
        },
        csrf: {
            deps: ['jquery']
        },
        subtab: {
            deps: ['jquery']
        },
	iemodal: {
	    deps: ['jquery']
	}
    },
    urlArgs: "bust=" +  (new Date()).getTime(),
},
        ['require', "jquery", 'ember',
         "cs!sitterfied", "csrf",
         "cs!routes", "cs!models",
         "cs!injections", "cs!controllers",
         "cs!views",'facebook', 'scrollto',
         "vasilli",'subtab', 'iemodal'], function(require, $,  Em, Sitterfied){
             // using jQuery
             Sitterfied.runInitializers();
             Sitterfied.advanceReadiness();
             window.Sitterfied = Sitterfied; //take out when finished developing
         })
