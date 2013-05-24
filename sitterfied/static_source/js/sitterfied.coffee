define ['jquery'
        'ember'
        '_'
        ], ($, Em, _) ->

    Sitterfied = Em.Application.create(
        location: 'history'
        LOG_TRANSITIONS: true
    )
    Sitterfied.ApplicationController = Ember.Controller.extend();
    Sitterfied.deferReadiness()
    return Sitterfied