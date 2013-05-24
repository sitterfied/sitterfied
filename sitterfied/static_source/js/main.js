require({
    paths: {
        "cs": "require/cs",
        "ember": "lib/ember-1.0.0-rc.3",
        "ember_data": "lib/ember-data-latest",
        "handlebars" : "lib/handlebars-1.0.0-rc.3",
        "_": "lib/underscore-min",
        "jquery": "lib/jquery-1.9.1",
        "jqueryui": "lib/jquery-ui-1.10.0.custom.min",
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
        ember_data: {
            deps: ['ember'],
            exports: "DS"
        },

        jqueryui: {
            deps: ['jquery']
        },
        _: {
            exports: "_",
        }
    },
        urlArgs: "bust=" +  (new Date()).getTime(),
},
        ["jquery", "cs!sitterfied", "cs!routes", "cs!models"], function($, Sitterfied){
            Sitterfied.advanceReadiness()
            $(function(){
            })
        });
