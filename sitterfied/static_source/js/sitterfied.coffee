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

        rootElement: $('#application')
        
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
        isAuthenticated: ((key, value) ->
            return authenticated
        ).property('authenticated')

        loadUserJson:(user_json) ->
            user_data = JSON.parse(user_json)
            user = Sitterfied[user_data.parent_or_sitter].create()
            user.load(user_data['id'], user_data)
            Sitterfied.set('currentUser', user)
            return user

        ready: () ->
            # Show the footer once the application has loaded
            $('.footer').css('visibility', 'visible')

            $(document).on 'click', '.rusitterfied', (e) ->
                e.preventDefault()
    )

    Sitterfied.Router.reopen(
      location: 'history'
    )

    Sitterfied.Educations = Em.A [
        "Some High School"
        "High School Degree"
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


    Sitterfied.Years = (num for num in [new Date().getFullYear()..1995])
    Sitterfied.SitterYears = (num for num in [new Date().getFullYear()..1900])

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
            Em.Object.create({value:"0000", name:"12:00 AM"})
            Em.Object.create({value:"0030", name:"12:30 AM"})
            Em.Object.create({value:"0100", name:"1:00 AM"})
            Em.Object.create({value:"0130", name:"1:30 AM"})
            Em.Object.create({value:"0200", name:"2:00 AM"})
            Em.Object.create({value:"0230", name:"2:30 AM"})
            Em.Object.create({value:"0300", name:"3:00 AM"})
            Em.Object.create({value:"0330", name:"3:30 AM"})
            Em.Object.create({value:"0400", name:"4:00 AM"})
            Em.Object.create({value:"0430", name:"4:30 AM"})
            Em.Object.create({value:"0500", name:"5:00 AM"})
            Em.Object.create({value:"0530", name:"5:30 AM"})
            Em.Object.create({value:"0600", name:"6:00 AM"})
            Em.Object.create({value:"0630", name:"6:30 AM"})
            Em.Object.create({value:"0700", name:"7:00 AM"})
            Em.Object.create({value:"0730", name:"7:30 AM"})
            Em.Object.create({value:"0800", name:"8:00 AM"})
            Em.Object.create({value:"0830", name:"8:30 AM"})
            Em.Object.create({value:"0900", name:"9:00 AM"})
            Em.Object.create({value:"0930", name:"9:30 AM"})
            Em.Object.create({value:"1000", name:"10:00 AM"})
            Em.Object.create({value:"1030", name:"10:30 AM"})
            Em.Object.create({value:"1100", name:"11:00 AM"})
            Em.Object.create({value:"1130", name:"11:30 AM"})
            Em.Object.create({value:"1200", name:"12:00 PM"})
            Em.Object.create({value:"1230", name:"12:30 PM"})
            Em.Object.create({value:"1300", name:"1:00 PM"})
            Em.Object.create({value:"1330", name:"1:30 PM"})
            Em.Object.create({value:"1400", name:"2:00 PM"})
            Em.Object.create({value:"1430", name:"2:30 PM"})
            Em.Object.create({value:"1500", name:"3:00 PM"})
            Em.Object.create({value:"1530", name:"3:30 PM"})
            Em.Object.create({value:"1600", name:"4:00 PM"})
            Em.Object.create({value:"1630", name:"4:30 PM"})
            Em.Object.create({value:"1700", name:"5:00 PM"})
            Em.Object.create({value:"1730", name:"5:30 PM"})
            Em.Object.create({value:"1800", name:"6:00 PM"})
            Em.Object.create({value:"1830", name:"6:30 PM"})
            Em.Object.create({value:"1900", name:"7:00 PM"})
            Em.Object.create({value:"1930", name:"7:30 PM"})
            Em.Object.create({value:"2000", name:"8:00 PM"})
            Em.Object.create({value:"2030", name:"8:30 PM"})
            Em.Object.create({value:"2100", name:"9:00 PM"})
            Em.Object.create({value:"2130", name:"9:30 PM"})
            Em.Object.create({value:"2200", name:"10:00 PM"})
            Em.Object.create({value:"2230", name:"10:30 PM"})
            Em.Object.create({value:"2300", name:"11:00 PM"})
            Em.Object.create({value:"2330", name:"11:30 PM"})
            Em.Object.create({value:"0000", name:"12:00 AM"})
    ]

    Sitterfied.OnDeckBooking = null
    Sitterfied.typeIsArray = Array.isArray || ( value ) -> return {}.toString.call( value ) is '[object Array]'
    
    return Sitterfied
