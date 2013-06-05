require({
    paths: {
        "cs": "require/cs",
        "ember": "lib/ember",
        "emberData": "lib/ember-data-latest",
        "handlebars" : "lib/handlebars",
        "_": "lib/underscore-min",
        "jquery": "lib/jquery-1.9.1",
        "jqueryui": "lib/jquery-ui-1.10.0.custom.min",
        "chosen": "lib/chosen.jquery.min",
        "djangoRestAdapter": "lib/adapter",
    },
    shim:{
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
        emberData: {
            deps: ['ember'],
            exports: "DS"
        },
        djangoRestAdapter: {
            deps: ['emberData'],
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
        ["jquery", "cs!sitterfied", "cs!routes", "cs!models", "vasilli"], function($, Sitterfied){
            Sitterfied.runInitializers()
            Sitterfied.advanceReadiness()
            window.Sitterfied = Sitterfied //take out when finished developing
            $(function(){
            })
        });
