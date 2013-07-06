define ['jquery'
        'ember'
        '_'
        ], ($, Em, _) ->

    Sitterfied = Em.Application.createWithMixins(
        LOG_TRANSITIONS: true
        LOG_VIEW_LOOKUPS: true
        LOG_TRANSITIONS_INTERNAL: true
        LOG_BINDINGS: true
        LOG_ACTIVE_GENERATION: true
        LOG_VERSION: true
        init:  () ->
            this.deferReadiness() # important - allows requirejs to preload everything. Take out for prod perhaps
            this._super()

        accountType: parent_or_sitter
        isSitter: (() ->
            Sitterfied.accountType == "Sitter"
        ).property('parent_or_sitter')
        isParent: (() ->
            Sitterfied.accountType == "Parent"
        ).property('parent_or_sitter')
    )

    Sitterfied.Router.reopen(
      location: 'history'
    )

    Sitterfied.ApplicationController = Ember.Controller.extend();

    return Sitterfied