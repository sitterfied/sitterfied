define ['jquery'
    'ember', '_', 'cs!sitterfied', 'model', 'moment',
    ], ($,Em, _, Sitterfied) ->
    attr = Ember.attr
    hasMany = Ember.hasMany
    belongsTo = Ember.belongsTo
    Adapter = Ember.RESTAdapter.extend(
        buildURL: (klass, id) ->
            urlRoot = Ember.get(klass, 'url')
            if not urlRoot
                k = klass.toString().toLowerCase().slice(1)
                urlRoot =  k + "s"
            if not Ember.isEmpty(id)
                return "/api/" + urlRoot + "/" + id + "/"
            else
                return "/api/" + urlRoot + "/"

        findMany: (klass, records, ids) ->
            url = this.buildURL(klass)
            url = url + "?id=" + ids.toString()
            return this.ajax(url).then (data) ->
                records.load(klass, data)


    )

    Date = {
        serialize: (date) ->
            if date then moment(date).toISOString() else null
        deserialize: (date) ->
            if date then moment(date).toDate() else null
    }

    Boolean = {
        serialize: (bool) ->
            return bool
        deserialize: (bool) ->
            return bool
    }

    Sitterfied.User = Ember.Model.extend(
        id: attr()
        #last_login: attr(Date)
        is_superuser: attr(Boolean)
        username: attr()
        first_name: attr()
        last_name: attr()
        email: attr()
        status: attr()
        parent_or_sitter: attr()
        sitter_groups: hasMany('Sitterfied.Group',{key: "sitter_groups"})
        languages: hasMany('Sitterfied.Language',{key: "languages"})
        settings  : belongsTo('Sitterfied.Setting', {key:"settings"})
        friends: hasMany('Sitterfied.User',{key: "friends"})
        address1: attr()
        address2: attr()
        city: attr()
        state: attr()
        zip: attr()
        cell: attr()
        reviews: hasMany('Sitterfied.SitterReview',{key: "reviews"})
        avatar: attr()


        facebook_token: attr()
        facebook_id: attr(Number)

        isSitter: (() ->
            @get('parent_or_sitter') == "Sitter"
        ).property('parent_or_sitter')
        isParent: (() ->
            @get('parent_or_sitter') == "Parent"
        ).property('parent_or_sitter')
        mailTo:  (() ->
            return "mailto:" +@get('email')
        ).property('email')
        avatarUrl: (() ->
            if @get('avatar')
                return @get('avatar')
            else
                return "/static/images/WhiteHeart_Avatar.jpg"
        ).property('avatar')

        sorted_bookings: (() ->
            return this.get('bookings').toArray().sort((booking1, booking2) ->
                if booking1.get('start_date_time') > booking2.get('start_date_time')
                    return 1
                else
                    return -1
            )
        ).property('bookings.@each')
        weeks_since_last_booking: (() ->
            if this.get('sorted_bookings').length == 0
                return 0
            else
                date = this.get('sorted_bookings.firstObject.stop_date_time')
                if not date
                    return 0
                return moment().diff(date, 'weeks')
        ).property('sorted_bookings.@each')
        days_since_last_booking: (() ->
            if this.get('sorted_bookings').length == 0
                return 0
            else
                date = this.get('sorted_bookings.firstObject.stop_date_time')
                if not date
                    return 0
                return moment().diff(date, 'days')
        ).property('sorted_bookings')
        full_name: ((key, value) ->
            if arguments.length == 1
                return @get('first_name') + ' ' + @get('last_name')

            else
                [first_name, last_name] = value.trim().split(" ", 2)
                this.set('first_name', first_name)
                this.set('last_name', last_name)
                return value
        ).property('first_name', 'last_name')

        friends_in_common: (() ->
            usersFriends = Sitterfied.get('currentUser.friends')
            myFriends = @get('friends')
            return _.intersection(usersFriends, myFriends)
        ).property('friends', 'Sitterfied.currentUser.friends')
        sitter_friends_in_common: (() ->
            @get('friends_in_common').filterProperty('isSitter')
        ).property('friends_in_common')
        parent_friends_in_common: (() ->
            @get('friends_in_common').filterProperty('isParent')
        ).property('friends_in_common')

    )
    Sitterfied.User.adapter = Adapter.create()

    Sitterfied.Setting = Ember.Model.extend(
        id: attr()
        user  : belongsTo('Sitterfied.' + parent_or_sitter, {key:"user"})
        #parent specific
        mobile_booking_accepted_denied: attr(Boolean)

        #sitter specific
        mobile_new_review : attr(Boolean)
        mobile_booking_request: attr(Boolean)

        mobile_friend_joined: attr(Boolean)
        mobile_groups_added_network: attr(Boolean)
        mobile_upcoming_booking_remind: attr(Boolean)

        #parent specific
        email_booking_accepted_denied: attr(Boolean)

        #sitter specific
        email_new_review : attr(Boolean)
        email_booking_request: attr(Boolean)

        email_friend_joined: attr(Boolean)
        email_groups_added_network: attr(Boolean)
        email_upcoming_booking_remind: attr(Boolean)

        email_news: attr(Boolean)
        email_blog: attr(Boolean)
    )
    Sitterfied.Setting.adapter = Adapter.create()

    Sitterfied.Contact = Ember.Model.extend(
        id: attr()
        #flush out later
    )

    Sitterfied.Group = Ember.Model.extend(
        id: attr()
        name: attr()
    )
    Sitterfied.Group.adapter = Adapter.create()

    Sitterfied.Parent = Sitterfied.User.extend(
        emergency_contact_one_name : attr("string")
        emergency_contact_one_phone : attr("string")
        emergency_contact_two_name : attr("string")
        emergency_contact_two_phone : attr("string")
        children: hasMany("Sitterfied.Child",{key: "children"})
        sitter_teams: hasMany("Sitterfied.Sitter", {key:"sitter_teams"})
        bookmarks: hasMany("Sitterfied.Sitter",{key:"bookmarks"})
        bookings: hasMany('Sitterfied.Booking',{key:"bookings"})

    )
    Sitterfied.Parent.adapter = Adapter.create()


    Sitterfied.Schedlue = Ember.Model.extend(
        id: attr()
        sitter: belongsTo('Sitterfied.Sitter', {key:"sitter"})
        mon_early_morning: attr(Boolean)
        tues_early_morning: attr(Boolean)
        wed_early_morning: attr(Boolean)
        thurs_early_morning: attr(Boolean)
        fri_early_morning: attr(Boolean)
        sat_early_morning: attr(Boolean)
        sun_early_morning: attr(Boolean)

        mon_late_morning: attr(Boolean)
        tues_late_morning: attr(Boolean)
        wed_late_morning: attr(Boolean)
        thurs_late_morning: attr(Boolean)
        fri_late_morning: attr(Boolean)
        sat_late_morning: attr(Boolean)
        sun_late_morning: attr(Boolean)

        mon_early_afternoon: attr(Boolean)
        tues_early_afternoon: attr(Boolean)
        wed_early_afternoon: attr(Boolean)
        thurs_early_afternoon: attr(Boolean)
        fri_early_afternoon: attr(Boolean)
        sat_early_afternoon: attr(Boolean)
        sun_early_afternoon: attr(Boolean)

        mon_late_afternoon: attr(Boolean)
        tues_late_afternoon: attr(Boolean)
        wed_late_afternoon: attr(Boolean)
        thurs_late_afternoon: attr(Boolean)
        fri_late_afternoon: attr(Boolean)
        sat_late_afternoon: attr(Boolean)
        sun_late_afternoon: attr(Boolean)

        mon_early_evening: attr(Boolean)
        tues_early_evening: attr(Boolean)
        wed_early_evening: attr(Boolean)
        thurs_early_evening: attr(Boolean)
        fri_early_evening: attr(Boolean)
        sat_early_evening: attr(Boolean)
        sun_early_evening: attr(Boolean)

        mon_late_evening: attr(Boolean)
        tues_late_evening: attr(Boolean)
        wed_late_evening: attr(Boolean)
        thurs_late_evening: attr(Boolean)
        fri_late_evening: attr(Boolean)
        sat_late_evening: attr(Boolean)
        sun_late_evening: attr(Boolean)

        mon_overnight: attr(Boolean)
        tues_overnight: attr(Boolean)
        wed_overnight: attr(Boolean)
        thurs_overnight: attr(Boolean)
        fri_overnight: attr(Boolean)
        sat_overnight: attr(Boolean)
        sun_overnight: attr(Boolean)
    )
    Sitterfied.Schedlue.adapter = Adapter.create()


    Sitterfied.Sitter = Sitterfied.User.extend(
        biography: attr()
        gender:  attr()
        id_verified: attr(Boolean)
        id_scanPath: attr()
        live_zip: attr()
        work_zip: attr()
        dob: attr(Date)
        smoker: attr(Boolean)
        sick: attr(Boolean)
        will_transport: attr(Boolean)

        total_exp: attr(Number)
        infant_exp: attr(Number)
        toddler_exp: attr(Number)
        preschool_exp: attr(Number)
        school_age_exp: attr(Number)
        pre_teen_exp: attr(Number)
        teen_exp: attr(Number)

        highest_education: attr(),
        last_school: attr(),
        current_student: attr(Boolean)

        schedlue: belongsTo('Sitterfied.Schedlue', {key:"schedlue"})

        major: attr()
        occupation:  attr()

        sitter_teams: hasMany("Sitterfied.Parent",{key:"sitter_teams"})
        certifications: hasMany('Sitterfied.Certification', {key:"certifications"})
        other_services: hasMany('Sitterfied.OtherService', {key:"other_services"})
        one_child_min_rate: attr(Number)
        one_child_max_rate: attr(Number)
        two_child_min_rate: attr(Number)
        two_child_max_rate: attr(Number)
        three_child_min_rate: attr(Number)
        three_child_max_rate: attr(Number)


        special_needs_exp : attr()
        extra_exp: attr()

        smokers_ok: attr(Boolean)
        dogs_ok: attr(Boolean)
        cats_ok: attr(Boolean)
        other_animals_ok: attr(Boolean)
        travel_distance: attr(Number)
        has_drivers_licence: attr(Boolean)

        bookings: hasMany('Sitterfied.Booking',{key:"bookings"})

        in_sitter_team: attr(Boolean)


        in_friends_team: attr(Boolean)
        bookmarks: hasMany("Sitterfied.Parent",{key:" bookmarks"})
        isBookmarked: (() ->
            bookmarks = Sitterfied.currentUser.get('bookmarks')
            return bookmarks.findProperty('id', this.get('id'))?
        ).property("Sitterfied.currentUser.bookmarks.@each", "Sitterfied.currentUser.bookmarks.lenth")
        shortBio: (() ->
            bio = @get('biography')
            if not bio?
                return ""
            return bio.substring(0, 100)
        ).property('biography')
        age: (() ->
            dob = @get('dob')
            if not dob?
                return 0
            return moment().diff(moment(dob), 'years')
        ).property("dob")

        lastBooking: (() ->
            return @get('sorted_bookings.firstObject')
        ).property('sorted_bookings.@each')
        dateLastHired: (() ->
            lastBooking = this.get('lastBooking')
            if lastBooking?.get('start_date_time')?
                return moment(lastBooking.get('start_date_time')).format('MMMM Do')
            else
                return "Never"
        ).property('lastBooking.start_date_time')

        recommends: (() ->
            return this.get('reviews').filterProperty('recommended', true)
        ).property('reviews.@each.recommended', 'reviews')

        inSitterTeam: (() ->
            sitterTeam = Sitterfied.currentUser.get('sitter_teams')
            return sitterTeam.findProperty('id', this.get('id'))?
        ).property("Sitterfied.currentUser.sitter_teams.@each", "Sitterfied.currentUser.sitter_teams.length")

        calc_total_exp: ((value) ->
            return @get('infant_exp') + @get('toddler_exp') + @get('preschool_exp') + @get('school_age_exp') + @get('pre_teenExp') + @get('teen_exp')
        ).property('infant_exp','toddler_exp','preschool_exp', 'school_ageExp', 'pre_teenExp', 'teen_exp')
    )

    Sitterfied.Sitter.adapter = Adapter.create()

    Sitterfied.Language = Ember.Model.extend(
        id: attr()
        language: attr()
        users: hasMany("Sitterfied.User",{key:"users"})
    )
    Sitterfied.Language.adapter = Adapter.create()

    Sitterfied.Certification = Ember.Model.extend(
        id: attr()
        certification: attr()
        sitters: hasMany("Sitterfied.Sitter",{key:"sitters"})
    )
    Sitterfied.Certification.adapter = Adapter.create()

    Sitterfied.OtherService = Ember.Model.extend(
        id: attr()
        service: attr()
        sitters: hasMany("Sitterfied.Sitter",{key:"sitters"})
    )
    Sitterfied.OtherService.adapter = Adapter.create()

    Sitterfied.SpecialNeed = Ember.Model.extend(
        id: attr()
        need: attr()
        children: hasMany("Sitterfied.Child",{key:"children"})
    )
    Sitterfied.SpecialNeed.adapter = Adapter.create()

    Sitterfied.Child = Ember.Model.extend(
        id: attr()
        parent: belongsTo('Sitterfied.Parent', {key:"parent"})
        name: attr()
        dob: attr(Date)
        school: attr()
        special_needs: hasMany("Sitterfied.SpecialNeed",{key:"special_needs"})

        birthMonth: ((key, value) ->
            date = @get('dob')
            if not date
                return
            if arguments.length == 1
                return date.getMonth()
            else
                date.setMonth(value)
                @set('dob', date)
        ).property('dob')

        birthDay: ((key, value) ->
            date = @get('dob')
            if not date
                return
            if arguments.length == 1
                return date.getDate()
            else
                date.setDate(value)
                @set('dob', date)
        ).property('dob')
        birthYear: ((key, value) ->
            date = @get('dob')
            if not date
                return
            if arguments.length == 1
                return date.getFullYear()
            else
                date.setFullYear(value)
                @set('dob', date)
        ).property('dob')

    )
    Sitterfied.Child.adapter = Adapter.create()
    Sitterfied.Child.url = "children"

    Sitterfied.SitterReview = Ember.Model.extend(
        id: attr()
        parent: belongsTo('Sitterfied.Parent', {key:"parent"})
        sitter: belongsTo('Sitterfied.Sitter', {key:"sitter"})
        recommended: attr(Boolean)
        review: attr()

    )
    Sitterfied.SitterReview.adapter = Adapter.create()

    Sitterfied.Booking = Ember.Model.extend(
        id: attr()
        parent: belongsTo('Sitterfied.Parent', {key:"parent"})
        created: attr(Date)
        notes: attr()
        respond_by: attr(Date)
        start_date_time: attr(Date)
        stop_date_time: attr(Date)
        num_children:  attr(Number)
        address1: attr()
        address2: attr()
        city: attr()
        state: attr()
        zip: attr()
        overnight: attr(Boolean)
        accepted_sitter: belongsTo('Sitterfied.Sitter', {key:"accepted_sitter"})
        rate: attr(Number)

        emergency_phone: attr()
        booking_status:attr()
        booking_type: attr()
        sitters: hasMany('Sitterfied.Sitter', {key: 'sitters'})
        declined_sitters: hasMany('Sitterfied.Sitter',{key:"declined_sitters"})
        canceled: attr(Boolean),


        isInterview: (() ->
            return @get('booking_type') == "Interview"
        ).property('booking_type')

        kidsString: (() ->
            if @get('num_children') ==1
                return "Kid"
            return "Kids"
        ).property('num_children')

        googleMapsLink: (() ->
            address1 = @get('address1')
            address2 = @get('address2')
            city = @get('city')
            state = @get('state')
            zip = @get('zip')
            query = "#{address1} #{address2}, #{state} #{city}, #{zip}"
            query = encodeURIComponent(query)
            return "http://maps.google.com/?q=" + query
        ).property("address1", "address2", "city", "state", "zip")

        otherPerson: (() ->
            if Sitterfied.accountType =="Parent"
                return @get('sitter')
            else
                return @get('parent')
        ).property('parent.id', 'sitter.id', 'Sitterfied.accountType')

        sitter: (() ->
            return this.get('sitters.firstObject')
        ).property('sitters.firstObject')

        formattedDate: (() ->
            date = @get('start_date_time')
            if not date
                return ""
            return moment(date).format('dddd, MMMM Do')
        ).property("start_date_time")
        formattedHours: (() ->
            start = @get('start_date_time')
            stop = @get('stop_date_time')
            if not start or not stop
                return ""
            startHour = moment(start).format('h:00 a');
            endHour = moment(stop).format('h:00 a');
            return startHour + " — " + endHour
        ).property('start_date_time', 'stop_date_time')

        startHour: ((key, value) ->
            date = @get('start_date_time')
            if not date
                return
            if not value?
                return moment(date).hour()
            else
                date = moment(date)
                date.hour(value)
                @set('start_date_time', date.toDate())
                return value
        ).property('start_date_time')

        endHour: ((key, value) ->
            date = @get('stop_date_time')
            if not date
                return
            if not value?
                return moment(date).hour()
            else
                date = moment(date)
                date.hour(value)
                @set('stop_date_time', date.toDate())
                return value
        ).property('stop_date_time')

        calendarDate: ((key, value) ->
            fmt_str = "ddd, Do MMM YYYY"
            date = @get('start_date_time')
            date = moment(date)
            if not date
                return
            if arguments.length == 1
                return date.format(fmt_str)
            else
                v = moment(value)
                date.date(v.date())
                date.year(v.year())
                date.month(v.month())
                @set('start_date_time', date.toDate())
                return v.format(fmt_str)
        ).property('start_date_time')

        children_binding: ((key, value) ->
            if value?
                @set('num_children', value.get('value'))
            return @get('num_children')
        ).property('num_children')

        thisSitterAccepted: (() ->
            current_user_id = Sitterfied.currentUser.get('id')
            return this.get('accepted_sitter.id') == current_user_id
        ).property('accepted_sitter')

        isInPast: (() ->
            now = moment().toDate()
            return @get('start_date_time') < now
        ).property('start_date_time')

    )
    Sitterfied.Booking.adapter = Adapter.create()

    Sitterfied.BookingRequest = Ember.Model.extend(
        id: attr()
        booking: belongsTo("Sitterfied.Booking", {key:"booking"})
    )
    Sitterfied.BookingRequest.adapter = Adapter.create()
