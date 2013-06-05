define ['jquery'
        'ember'
        '_'
        ], ($, Em, _) ->

    Sitterfied = Em.Application.createWithMixins(
        LOG_TRANSITIONS: true
        LOG_VIEW_LOOKUPS: true
        init:  () ->
            this.deferReadiness()
            this._super()
    )

    Sitterfied.Router.reopen(
      location: 'history'
    )

    Sitterfied.ApplicationController = Ember.Controller.extend();

    return Sitterfied