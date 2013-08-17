define [
    'ember', '_', 'cs!sitterfied', 'data', 'moment','djangoRestAdapter'
    ], (Em, _, Sitterfied) ->


    Sitterfied.Adapter  = DS.DjangoRESTAdapter.extend
        namespace: 'api'

    Sitterfied.Adapter.registerTransform "date",
        serialize: (date) ->
            if date then moment(date).format("YYYY-MM-DD hh:mm") else null

        deserialize: (date) ->
            if date then moment(date).toDate() else null


    Sitterfied.Store = DS.Store.extend(
        revision: 12
        adapter: Sitterfied.Adapter.create()
        isDefaultStore:true
    )


    Sitterfied.User = DS.Model.extend(
        #last_login: DS.attr('date')
        is_superuser: DS.attr('boolean')
        username: DS.attr('string')
        first_name: DS.attr('string')
        last_name: DS.attr('string')
        email: DS.attr('string')
        status: DS.attr('string')
        parent_or_sitter: DS.attr('string')
        sitter_groups: DS.hasMany('Sitterfied.Group')
        languages: DS.hasMany('Sitterfied.Language')
        settings  : DS.belongsTo('Sitterfied.Setting')
        bookings: DS.hasMany('Sitterfied.Booking'),
        friends: DS.hasMany('Sitterfied.User'),
        address1: DS.attr('string')
        address2: DS.attr('string')
        city: DS.attr('string')
        state: DS.attr('string')
        zip: DS.attr('string')
        cell: DS.attr('string')
        reviews: DS.hasMany('Sitterfied.SitterReview')
        avatar: DS.attr('string')


        facebook_token: DS.attr('string')
        facebook_id: DS.attr('number')

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
                return "/media/" + @get('avatar')
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
                return moment().diff(date, 'weeks')
        ).property('sorted_bookings')
        days_since_last_booking: (() ->
            if this.get('sorted_bookings').length == 0
                return 0
            else
                date = this.get('sorted_bookings.firstObject.stop_date_time')
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
    )

    Sitterfied.Setting = DS.Model.extend(
        user  : DS.belongsTo('Sitterfied.' + parent_or_sitter)
        #parent specific
        mobile_booking_accepted_denied: DS.attr('boolean')

        #sitter specific
        mobile_new_review : DS.attr('boolean')
        mobile_booking_request: DS.attr('boolean')

        mobile_friend_joined: DS.attr('boolean')
        mobile_groups_added_network: DS.attr('boolean')
        mobile_upcoming_booking_remind: DS.attr('boolean')

        #parent specific
        email_booking_accepted_denied: DS.attr('boolean')

        #sitter specific
        email_new_review : DS.attr('boolean')
        email_booking_request: DS.attr('boolean')

        email_friend_joined: DS.attr('boolean')
        email_groups_added_network: DS.attr('boolean')
        email_upcoming_booking_remind: DS.attr('boolean')

        email_news: DS.attr('boolean')
        email_blog: DS.attr('boolean')
    )

    Sitterfied.Contact = DS.Model.extend(
        #flush out later
    )

    Sitterfied.Group = DS.Model.extend(
        name: DS.attr('string')
    )

    Sitterfied.Parent = Sitterfied.User.extend(
        emergency_contact_one_name : DS.attr("string")
        emergency_contact_one_phone : DS.attr("string")
        emergency_contact_two_name : DS.attr("string")
        emergency_contact_two_phone : DS.attr("string")
        children: DS.hasMany("Sitterfied.Child")
        sitter_teams: DS.hasMany("Sitterfied.Sitter", {inverse:'sitter_teams'})
        bookmarks: DS.hasMany("Sitterfied.Sitter", {inverse: 'bookmarks'})

    )

    Sitterfied.Schedlue = DS.Model.extend(
        sitter: DS.belongsTo('Sitterfied.Sitter'),
        mon_early_morning: DS.attr('boolean')
        tues_early_morning: DS.attr('boolean')
        wed_early_morning: DS.attr('boolean')
        thurs_early_morning: DS.attr('boolean')
        fri_early_morning: DS.attr('boolean')
        sat_early_morning: DS.attr('boolean')
        sun_early_morning: DS.attr('boolean')

        mon_late_morning: DS.attr('boolean')
        tues_late_morning: DS.attr('boolean')
        wed_late_morning: DS.attr('boolean')
        thurs_late_morning: DS.attr('boolean')
        fri_late_morning: DS.attr('boolean')
        sat_late_morning: DS.attr('boolean')
        sun_late_morning: DS.attr('boolean')

        mon_early_afternoon: DS.attr('boolean')
        tues_early_afternoon: DS.attr('boolean')
        wed_early_afternoon: DS.attr('boolean')
        thurs_early_afternoon: DS.attr('boolean')
        fri_early_afternoon: DS.attr('boolean')
        sat_early_afternoon: DS.attr('boolean')
        sun_early_afternoon: DS.attr('boolean')

        mon_late_afternoon: DS.attr('boolean')
        tues_late_afternoon: DS.attr('boolean')
        wed_late_afternoon: DS.attr('boolean')
        thurs_late_afternoon: DS.attr('boolean')
        fri_late_afternoon: DS.attr('boolean')
        sat_late_afternoon: DS.attr('boolean')
        sun_late_afternoon: DS.attr('boolean')

        mon_early_evening: DS.attr('boolean')
        tues_early_evening: DS.attr('boolean')
        wed_early_evening: DS.attr('boolean')
        thurs_early_evening: DS.attr('boolean')
        fri_early_evening: DS.attr('boolean')
        sat_early_evening: DS.attr('boolean')
        sun_early_evening: DS.attr('boolean')

        mon_late_evening: DS.attr('boolean')
        tues_late_evening: DS.attr('boolean')
        wed_late_evening: DS.attr('boolean')
        thurs_late_evening: DS.attr('boolean')
        fri_late_evening: DS.attr('boolean')
        sat_late_evening: DS.attr('boolean')
        sun_late_evening: DS.attr('boolean')

        mon_overnight: DS.attr('boolean')
        tues_overnight: DS.attr('boolean')
        wed_overnight: DS.attr('boolean')
        thurs_overnight: DS.attr('boolean')
        fri_overnight: DS.attr('boolean')
        sat_overnight: DS.attr('boolean')
        sun_overnight: DS.attr('boolean')
    )

    Sitterfied.Sitter = Sitterfied.User.extend(
        biography: DS.attr('string'),
        gender:  DS.attr('string'),
        id_verified: DS.attr('boolean'),
        id_scanPath: DS.attr('string'),
        live_zip: DS.attr('string'),
        work_zip: DS.attr('string'),
        dob: DS.attr('string'),
        smoker: DS.attr('string'),
        sick: DS.attr('string'),
        will_transport: DS.attr('string'),

        total_exp: DS.attr('number'),
        infant_exp: DS.attr('number'),
        toddler_exp: DS.attr('number'),
        preschool_exp: DS.attr('number'),
        school_age_exp: DS.attr('number'),
        pre_teen_exp: DS.attr('number'),
        teen_exp: DS.attr('number'),

        highest_education: DS.attr('string'),
        last_school: DS.attr('string'),
        current_student: DS.attr('boolean'),

        schedlue: DS.belongsTo('Sitterfied.Schedlue'),

        major: DS.attr('string'),
        occupation:  DS.attr('string'),

        sitter_teams: DS.hasMany("Sitterfied.Parent", {inverse:'sitter_teams'})
        reviews: DS.hasMany('Sitterfied.SitterReview'),
        certifications: DS.hasMany('Sitterfied.Certification'),
        other_services: DS.hasMany('Sitterfied.OtherService'),
        one_child_min_rate: DS.attr('number'),
        one_child_max_rate: DS.attr('number'),
        two_child_min_rate: DS.attr('number'),
        two_child_max_rate: DS.attr('number'),
        three_child_min_rate: DS.attr('number'),
        three_child_max_rate: DS.attr('number'),


        special_needs_exp : DS.attr('string')
        extra_exp: DS.attr('string')

        smokers_ok: DS.attr('string'),
        dogs_ok: DS.attr('string'),
        cats_ok: DS.attr('string'),
        other_animals_ok: DS.attr('string'),
        travel_distance: DS.attr('number'),
        has_drivers_licence: DS.attr('string'),



        in_sitter_team: DS.attr('boolean'),
        in_friends_team: DS.attr('boolean'),
        bookmarks: DS.hasMany("Sitterfied.Parent", {inverse: 'bookmarks'})
        isBookmarked: (() ->
            bookmarks = Sitterfied.currentUser.get('bookmarks')
            return bookmarks.indexOf(this) != -1
        ).property("Sitterfied.currentUser.bookmarks.@each")
        shortBio: (() ->
            @get('biography').substring(0, 100)
        ).property('biography')
        age: (() ->
            dob = @get('dob')
            return moment().diff(moment(dob), 'years')
        ).property("dob")

        dateLastHired: (() ->
            bookings = this.get('sorted_bookings')
            if bookings.length == 0
                return "Never"
            else
                return bookings.get('firstObject.formattedDate')
        ).property('sorted_bookings')

        recommends: (() ->
            return this.get('reviews').filterProperty('recommended', true)
        ).property('reviews.@each')


        calc_total_exp: ((value) ->
            return @get('infant_exp') + @get('toddler_exp') + @get('preschool_exp') + @get('school_ageExp') + @get('pre_teenExp') + @get('teen_exp')
        ).property('infant_exp','toddler_exp','preschool_exp', 'school_ageExp', 'pre_teenExp', 'teen_exp')
    )

    Sitterfied.Language = DS.Model.extend(
        language: DS.attr('string'),
        users: DS.hasMany("Sitterfied.User")
    )
    Sitterfied.Certification = DS.Model.extend(
        certification: DS.attr('string'),
        sitters: DS.hasMany("Sitterfied.Sitter")
    )
    Sitterfied.OtherService = DS.Model.extend(
        service: DS.attr('string'),
        sitters: DS.hasMany("Sitterfied.Sitter")
    )
    Sitterfied.SpecialNeed = DS.Model.extend(
        need: DS.attr('string'),
        children: DS.hasMany("Sitterfied.Child")
    )

    Sitterfied.Child = DS.Model.extend(
        parent: DS.belongsTo('Sitterfied.Parent'),
        name: DS.attr('string'),
        dob: DS.attr('date'),
        school: DS.attr('string'),
        special_needs: DS.hasMany("Sitterfied.SpecialNeed")

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

    Sitterfied.SitterReview = DS.Model.extend(
        parent: DS.belongsTo('Sitterfied.Parent'),
        sitter: DS.belongsTo('Sitterfied.Sitter'),
        recommended: DS.attr('boolean'),
        review: DS.attr('string'),

    )

    Sitterfied.Booking = DS.Model.extend(
        parent: DS.belongsTo('Sitterfied.Parent'),
        created: DS.attr("date")
        notes: DS.attr('string'),
        respond_by: DS.attr('date'),
        start_date_time: DS.attr('date'),
        stop_date_time: DS.attr('date'),
        num_children:  DS.attr('number'),
        address1: DS.attr('string')
        address2: DS.attr('string')
        city: DS.attr('string')
        state: DS.attr('string')
        zip: DS.attr('string')
        overnight: DS.attr('boolean'),
        accepted_sitter: DS.belongsTo('Sitterfied.Sitter'),
        rate: DS.attr('number'),

        emergency_phone: DS.attr('string'),
        #location: models.Foreign_key('Address')
        booking_status:DS.attr('string'),
        booking_type: DS.attr('string'),
        sitters: DS.hasMany('Sitterfied.Sitter'),
        declined_sitters: DS.hasMany('Sitterfied.Sitter'),
        canceled: DS.attr('boolean'),


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
            return moment(date).format('dddd Do MMMM YYYY')
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
            if arguments.length == 1
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
            if arguments.length == 1
                return moment(date).format('h:mm a');
            else
                date = moment(date)
                date.hour(value)
                @set('stop_date_time', date.toDate())
                return value
        ).property('stop_date_time')

        calendarDate: ((key, value) ->
            date = @get('start_date_time')
            date = moment(date)
            if not date
                return
            if arguments.length == 1
                return date.format("YYYY-MM-DD")
            else
                v = moment(value)
                date.date(v.date())
                date.year(v.year())
                date.month(v.month())
                @set('start_date_time', date.toDate())
                return v.format("YYYY-MM-DD")
        ).property('start_date_time')

        thisSitterAccepted: (() ->
            current_user = Sitterfied.currentUser
            return this.get('accepted_sitter') == current_user
        ).property('accepted_sitter')

    )

    Sitterfied.BookingRequest = DS.Model.extend(
        booking: DS.belongsTo("Sitterfied.Booking"),

    )
