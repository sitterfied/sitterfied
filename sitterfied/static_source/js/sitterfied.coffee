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

    Sitterfied.Educations = [
        "Some High Scool"
        "High Scool Degree"
        "Some College"
        "College Degree"
    ]
    Sitterfied.onDeckAvatar = ''


    Sitterfied.Years = (num for num in [2013..1995])
    Sitterfied.Days = (num for num in [1..31])
    Sitterfied.Months = [
        {value:0, name: "January"}
        {value:1, name: "February"}
        {value:2, name: "March"}
        {value:3, name: "April"}
        {value:4, name: "May"}
        {value:5, name: "June"}
        {value:6, name: "July"}
        {value:7, name: "August"}
        {value:8, name: "September"}
        {value:9, name: "October"}
        {value:10, name: "November"}
        {value:11, name: "December"}
    ]

    Sitterfied.States = [
            'AL',
            'AK',
            'AZ',
            'AR',
            'CA',
            'CO',
            'CT',
            'DE',
            'DC',
            'FL',
            'GA',
            'HI',
            'ID',
            'IL',
            'IN',
            'IA',
            'KS',
            'KY',
            'LA',
            'ME',
            'MD',
            'MA',
            'MI',
            'MN',
            'MS',
            'MO',
            'MT',
            'NE',
            'NV',
            'NH',
            'NJ',
            'NM',
            'NY',
            'NC',
            'ND',
            'OH',
            'OK',
            'OR',
            'PA',
            'RI',
            'SC',
            'SD',
            'TN',
            'TX',
            'UT',
            'VT',
            'VA',
            'WA',
            'WV',
            'WI',
            'WY',
        ]








    return Sitterfied