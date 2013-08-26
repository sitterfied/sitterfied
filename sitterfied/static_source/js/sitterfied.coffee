define ['jquery'
        'ember'
        '_'
        'model'
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

    Sitterfied.Educations = Em.A [
        "Some High Scool"
        "High Scool Degree"
        "Some College"
        "College Degree"
    ]

    Sitterfied.SitterTimeRanges = Em.A [
        Em.Object.create({value:0, name: "Early Morning"})
        Em.Object.create({value:1, name: "Late Morning"})
        Em.Object.create({value:2, name: "Early Afternoon"})
        Em.Object.create({value:3, name: "Late Afternoon"})
        Em.Object.create({value:4, name: "Early Evening"})
        Em.Object.create({value:5, name: "Late Evening"})
    ]
    Sitterfied.Kids = Em.A [
        Em.Object.create({value:1, name: "1 Kid"})
        Em.Object.create({value:2, name: "2 Kids"})
        Em.Object.create({value:3, name: "3 Kids"})
        Em.Object.create({value:4, name: "4 Kids"})
        Em.Object.create({value:5, name: "5 Kids"})
        Em.Object.create({value:6, name: "6 Kids"})
        Em.Object.create({value:7, name: "7 Kids"})
        Em.Object.create({value:8, name: "8 Kids"})
        Em.Object.create({value:9, name: "9 Kids"})
        Em.Object.create({value:10, name: "10 Kids"})
    ]


    Sitterfied.onDeckAvatar = ''


    Sitterfied.Years = (num for num in [2013..1995])
    Sitterfied.Days = (num for num in [1..31])
    Sitterfied.Months = Em.A [
        Em.Object.create({value:0, name: "January"})
        Em.Object.create({value:1, name: "February"})
        Em.Object.create({value:2, name: "March"})
        Em.Object.create({value:3, name: "April"})
        Em.Object.create({value:4, name: "May"})
        Em.Object.create({value:5, name: "June"})
        Em.Object.create({value:6, name: "July"})
        Em.Object.create({value:7, name: "August"})
        Em.Object.create({value:8, name: "September"})
        Em.Object.create({value:9, name: "October"})
        Em.Object.create({value:10, name: "November"})
        Em.Object.create({value:11, name: "December"})
    ]

    Sitterfied.States = Em.A [
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

    Sitterfied.HourBlocks = Em.A [
            Em.Object.create({value:0, name:"12:00 AM"})
            Em.Object.create({value:1, name:"1:00 AM"})
            Em.Object.create({value:2, name:"2:00 AM"})
            Em.Object.create({value:3, name:"3:00 AM"})
            Em.Object.create({value:4, name:"4:00 AM"})
            Em.Object.create({value:5, name:"5:00 AM"})
            Em.Object.create({value:6, name:"6:00 AM"})
            Em.Object.create({value:7, name:"7:00 AM"})
            Em.Object.create({value:8, name:"8:00 AM"})
            Em.Object.create({value:9, name:"9:00 AM"})
            Em.Object.create({value:10, name:"10:00 AM"})
            Em.Object.create({value:11, name:"11:00 AM"})
            Em.Object.create({value:12, name:"12:00 PM"})
            Em.Object.create({value:13, name:"1:00 PM"})
            Em.Object.create({value:14, name:"2:00 PM"})
            Em.Object.create({value:15, name:"3:00 PM"})
            Em.Object.create({value:16, name:"4:00 PM"})
            Em.Object.create({value:17, name:"5:00 PM"})
            Em.Object.create({value:18, name:"6:00 PM"})
            Em.Object.create({value:19, name:"7:00 PM"})
            Em.Object.create({value:20, name:"8:00 PM"})
            Em.Object.create({value:21, name:"9:00 PM"})
            Em.Object.create({value:22, name:"10:00 PM"})
            Em.Object.create({value:23, name:"11:00 PM"})
    ]

    Sitterfied.OnDeckBooking = null
    Sitterfied.typeIsArray = Array.isArray || ( value ) -> return {}.toString.call( value ) is '[object Array]'

    return Sitterfied