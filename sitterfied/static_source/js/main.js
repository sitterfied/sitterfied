require({
    paths: {
        "cs": "require/cs",
        "ember": "lib/ember",
        "data": "lib/ember-data-latest",
        "handlebars" : "lib/handlebars",
        "_": "lib/underscore-min",
        "jquery": "lib/jquery-1.9.1",
        "jqueryui": "lib/jquery-ui-1.10.0.custom.min",
        "chosen": "lib/chosen.jquery.min",
        "djangoRestAdapter": "lib/adapter",
    },
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
        jqueryui: {
            deps: ['jquery']
        },
        _: {
            exports: "_",
        },
        chosen: {
            deps: ['jquery']
        }
    },
        urlArgs: "bust=" +  (new Date()).getTime(),
},
        ["jquery", 'ember', "cs!sitterfied", "csrf", "cs!routes", "cs!models", "cs!controllers", "vasilli"], function($, Em, Sitterfied){
            // using jQuery
            Sitterfied.runInitializers()
            Sitterfied.advanceReadiness()
            window.Sitterfied = Sitterfied //take out when finished developing
            $(function(){
            })
        });
