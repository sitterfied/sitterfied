require({
    paths: {
        "cs": "require/cs",
        "ember": "lib/ember",
        "data": "lib/ember-data-latest",
        "handlebars" : "lib/handlebars",
        "ajaxfileupload": 'lib/ajaxfileupload.js',
        "_": "lib/underscore-min",
        "jquery": "lib/jquery-1.9.1",
        "jqueryui": "lib/jquery-ui-1.10.0.custom.min",
        "chosen": "lib/chosen.jquery.min",
        "select2": "lib/select2",
        "djangoRestAdapter": "lib/adapter",
        'fancybox':'lib/jquery.fancybox.pack',
        'moment': 'lib/moment.min',
        'scrollto': 'lib/jquery.scrollTo-1.4.3.1-min'
    },
    waitSeconds: 0,
    shim:{
        data: {
            exports: 'DS',
            deps: ['ember'],
        },
        jquery: {
            exports: "$",
        },
        ember: {
            exports: "Ember",
            deps: ['jquery', 'handlebars']
        },
        handlebars: {
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
        }

    },
        urlArgs: "bust=" +  (new Date()).getTime(),
},
        ["jquery", 'ember',
         "cs!sitterfied", "csrf",
         "cs!routes", "cs!models",
         "cs!injections", "cs!controllers",
         "cs!views",
         'scrollto',
         "vasilli",  'facebook',], function($, Em, Sitterfied){
            // using jQuery
            Sitterfied.runInitializers()
            Sitterfied.advanceReadiness()
            window.Sitterfied = Sitterfied //take out when finished developing
            $(function(){
            })
        });
