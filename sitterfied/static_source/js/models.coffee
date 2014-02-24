define ['jquery'
        'ember', '_', 'cs!sitterfied', 'model', 'moment','phoneformat'], ($,Em, _, Sitterfied) ->
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
            if date then moment(date).utc().toISOString() else null
        deserialize: (date) ->
            #deal with ujson wierdniss
            if date
                if $.type(date) ==  "number"
                    date = moment.unix(date)
                else
                    date = moment(date)
                return date.local().toDate()
            else null
    }

    Phone = {
        serialize: (number) ->
            return formatE164("US", number)
        deserialize: (number) ->
            return formatLocal("US", number)
    }


    BooleanType = {
        serialize: (bool) ->
            return bool
        deserialize: (bool) ->
            return bool
    }

    Sitterfied.User = Ember.Model.extend(
        id: attr()
        #last_login: attr(Date)
        date_joined: attr(Date)
        is_superuser: attr(BooleanType)
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
        cell: attr(Phone)
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
        myFriends: (() ->
            friends = this.get('friends')
            myself = friends.findProperty('id', this.get('id'))
            if myself
                friends.removeObject(myself)
            return friends
        ).property('friends.@each', 'friends.length')

        addFriend: (friend) ->
            friends = @get("friends")
            if friends.findProperty('id', friend.get("id"))
                return
            friends.pushObject(friend)
            @set('isDirty', true)
            @save()

        removeFriend: (friend) ->
            friends = @get("friends")
            toBlock = friends.findProperty('id', friend.get('id'))
            friends.removeObject(toBlock)
            @set('isDirty', true)
            @save()

        removeGroup: (group) ->
            groups = @get("sitter_groups")
            toBlock = groups.findProperty('id', group.get('id'))
            groups.removeObject(toBlock)
            @set('isDirty', true)
            @save()


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
            return myFriends.filter((item, index, list) ->
                if item.get("id") == Sitterfied.get('currentUser.id') then return false
                Boolean(usersFriends.findProperty("id", item.get("id")))
            )
        ).property('friends.@each',
            "friends.@each.isLoaded",
            'Sitterfied.currentUser.friends.length',
            'Sitterfied.currentUser.friends.@each',
            'Sitterfied.currentUser.friends.@each.isLoaded')

        sitter_friends_in_common: (() ->
            @get('friends_in_common').filter((item, index, list) ->
                item.get("isSitter")
            )
        ).property('friends_in_common')

        parent_friends_in_common: (() ->
            @get('friends_in_common').filter((item, index, list) ->
                item.get("isParent")
            )
        ).property('friends_in_common')

        groups_in_common: (() ->
            usersGroups = Sitterfied.get('currentUser.sitter_groups')
            myGroups = @get('sitter_groups')
            return usersGroups.filter((item, index, list) ->
                Boolean(myGroups.findProperty("id", item.get("id")))
            )
        ).property('sitter_groups.@each', 'Sitterfied.currentUser.sitter_groups')

        memberSince : (() ->
            date_joined = @get("date_joined")
            if not date_joined
                return ""
            return moment(date_joined).format("MMM YYYY")
        ).property("date_joined")

        #once we have the user data, upgrade to the real thing.
        sitter: (() ->
            if not @get("id")
                return null
            return Sitterfied.Sitter.find(@get("id"))
        ).property("id")
        parent: (() ->
            if not @get("id")
                return null
            return Sitterfied.Parent.find(@get("id"))
        ).property("id")

    )
    Sitterfied.User.adapter = Adapter.create()

    Sitterfied.Setting = Ember.Model.extend(
        id: attr()
        user  : belongsTo('Sitterfied.' + parent_or_sitter, {key:"user"})
        #parent specific
        mobile_booking_accepted_denied: attr(BooleanType)

        #sitter specific
        mobile_new_review : attr(BooleanType)
        mobile_booking_request: attr(BooleanType)

        mobile_friend_joined: attr(BooleanType)
        mobile_groups_added_network: attr(BooleanType)
        mobile_upcoming_booking_remind: attr(BooleanType)

        #parent specific
        email_booking_accepted_denied: attr(BooleanType)

        #sitter specific
        email_new_review : attr(BooleanType)
        email_booking_request: attr(BooleanType)

        email_friend_joined: attr(BooleanType)
        email_groups_added_network: attr(BooleanType)
        email_upcoming_booking_remind: attr(BooleanType)

        email_news: attr(BooleanType)
        email_blog: attr(BooleanType)
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
        parent: (() ->
            return this
        ).property()


        sitters_to_review: (() ->
            results = Em.A()
            revs = this.get('reviews').toArray()
            sitter_id_set = new Em.Set()
            
            #Get existing reviews
            for rev in revs
                if rev.get('sitter')
                    sitter_id_set.add(rev.get('sitter').get('id'))
            
            #Include sitters that has no reviews
            bookings = this.get('bookings').toArray()
            for booking in bookings
                accepted_sitter = booking.get('accepted_sitter')
                if accepted_sitter and not sitter_id_set.contains(accepted_sitter.get('id'))
                    results.pushObject(accepted_sitter)
            return results.uniq()
        ).property('reviews.@each', "reviews.@each.sitter", 'bookings.@each', "bookings.@each.accepted_sitter")
            
        sitter_reviews: (() ->
            return Sitterfied.SitterReview.fetch()
        )

    )
    Sitterfied.Parent.adapter = Adapter.create()


    Sitterfied.Schedule = Ember.Model.extend(
        id: attr()
        sitter: belongsTo('Sitterfied.Sitter', {key:"sitter"})
        mon_early_morning: attr(BooleanType)
        tue_early_morning: attr(BooleanType)
        wed_early_morning: attr(BooleanType)
        thu_early_morning: attr(BooleanType)
        fri_early_morning: attr(BooleanType)
        sat_early_morning: attr(BooleanType)
        sun_early_morning: attr(BooleanType)

        mon_late_morning: attr(BooleanType)
        tue_late_morning: attr(BooleanType)
        wed_late_morning: attr(BooleanType)
        thu_late_morning: attr(BooleanType)
        fri_late_morning: attr(BooleanType)
        sat_late_morning: attr(BooleanType)
        sun_late_morning: attr(BooleanType)

        mon_early_afternoon: attr(BooleanType)
        tue_early_afternoon: attr(BooleanType)
        wed_early_afternoon: attr(BooleanType)
        thu_early_afternoon: attr(BooleanType)
        fri_early_afternoon: attr(BooleanType)
        sat_early_afternoon: attr(BooleanType)
        sun_early_afternoon: attr(BooleanType)

        mon_late_afternoon: attr(BooleanType)
        tue_late_afternoon: attr(BooleanType)
        wed_late_afternoon: attr(BooleanType)
        thu_late_afternoon: attr(BooleanType)
        fri_late_afternoon: attr(BooleanType)
        sat_late_afternoon: attr(BooleanType)
        sun_late_afternoon: attr(BooleanType)

        mon_early_evening: attr(BooleanType)
        tue_early_evening: attr(BooleanType)
        wed_early_evening: attr(BooleanType)
        thu_early_evening: attr(BooleanType)
        fri_early_evening: attr(BooleanType)
        sat_early_evening: attr(BooleanType)
        sun_early_evening: attr(BooleanType)

        mon_late_evening: attr(BooleanType)
        tue_late_evening: attr(BooleanType)
        wed_late_evening: attr(BooleanType)
        thu_late_evening: attr(BooleanType)
        fri_late_evening: attr(BooleanType)
        sat_late_evening: attr(BooleanType)
        sun_late_evening: attr(BooleanType)

        mon_overnight: attr(BooleanType)
        tue_overnight: attr(BooleanType)
        wed_overnight: attr(BooleanType)
        thu_overnight: attr(BooleanType)
        fri_overnight: attr(BooleanType)
        sat_overnight: attr(BooleanType)
        sun_overnight: attr(BooleanType)
    )
    Sitterfied.Schedule.adapter = Adapter.create()


    Sitterfied.Sitter = Sitterfied.User.extend(
        biography: attr()
        gender:  attr()
        id_verified: attr(BooleanType)
        id_scanPath: attr()

        dob: attr(Date)
        smoker: attr(BooleanType)
        sick: attr(BooleanType)
        will_transport: attr(BooleanType)

        total_exp: attr(Number)
        infant_exp: attr(Number)
        toddler_exp: attr(Number)
        preschool_exp: attr(Number)
        school_age_exp: attr(Number)
        pre_teen_exp: attr(Number)
        teen_exp: attr(Number)

        highest_education: attr(),
        last_school: attr(),
        current_student: attr(BooleanType)

        schedule: belongsTo('Sitterfied.Schedule', {key:"schedule"})

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

        smokers_ok: attr(BooleanType)
        dogs_ok: attr(BooleanType)
        cats_ok: attr(BooleanType)
        other_animals_ok: attr(BooleanType)
        travel_distance: attr(Number)
        has_drivers_licence: attr(BooleanType)

        bookings: hasMany('Sitterfied.Booking',{key:"bookings"})

        in_sitter_team: attr(BooleanType)


        biographyPList: (() ->
            bio = @get('biography')
            return bio?.split(/\r?\n\r?\n/)
        ).property('biography')

        in_friends_team: attr(BooleanType)
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
            
        rehires: (() ->
            return this.get('reviews').filterProperty('rehire', true)
        ).property('reviews.@each.rehire', 'reviews')

        inSitterTeam: (() ->
            sitterTeam = Sitterfied.currentUser.get('sitter_teams')
            return sitterTeam.findProperty('id', this.get('id'))?
        ).property("Sitterfied.currentUser.sitter_teams.@each", "Sitterfied.currentUser.sitter_teams.length")

        calc_total_exp: ((value) ->
            return @get('infant_exp') + @get('toddler_exp') + @get('preschool_exp') + @get('school_age_exp') + @get('pre_teenExp') + @get('teen_exp')
        ).property('infant_exp','toddler_exp','preschool_exp', 'school_ageExp', 'pre_teenExp', 'teen_exp')


        birthMonth: ((key, value) ->
            date = @get('dob')
            if not date
                return
            if arguments.length == 1 or not value
                return date.getMonth()
            else
                date.setMonth(value)
                @set('dob', date)
            return value
        ).property('dob')

        birthDay: ((key, value) ->
            date = @get('dob')
            if not date
                return
            if arguments.length == 1 or not value
                return date.getDate()
            else
                date.setDate(value)
                @set('dob', date)
        ).property('dob')

        birthYear: ((key, value) ->
            date = @get('dob')
            if not date
                return
            if arguments.length == 1 or not value
                return date.getFullYear()
            else

                date.setFullYear(value)
                @set('dob', date)
        ).property('dob')

        sitter: (() ->
            return this
        ).property()
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

        displayName: (() ->
            name = @get('name')
            if not name? or name == ""
                return "Child"
            name.split(' ')[0]

        ).property('name')

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
        recommended: attr(BooleanType)
        rehire: attr(BooleanType)
        review: attr()

        sitterAvatarUrl: (() ->
            if this.get('sitter')
                if this.get('sitter').get('avatar')
                    return this.get('sitter').get('avatar')
            else
                return "/static/images/WhiteHeart_Avatar.jpg"
        ).property('sitter', 'sitter.avatar')
            
        parentAvatarUrl: (() ->
            if this.get('parent')
                if this.get('parent').get('avatar')
                    return this.get('parent').get('avatar')
            else
                return "/static/images/WhiteHeart_Avatar.jpg"
        ).property('parent', 'parent.avatar')
            
        inSitterTeam: (() ->
            if this.get('sitter')
                console.log("In sitter team:", this.get('sitter').get('inSitterTeam'))
                return this.get('sitter').get('inSitterTeam')
            return null
        ).property('sitter')
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
        overnight: attr(BooleanType)
        accepted_sitter: belongsTo('Sitterfied.Sitter', {key:"accepted_sitter"})
        rate: attr(Number)

        emergency_phone: attr(Phone)
        booking_status:attr()
        booking_type: attr()
        sitters: hasMany('Sitterfied.Sitter', {key: 'sitters'})
        declined_sitters: hasMany('Sitterfied.Sitter',{key:"declined_sitters"})
        canceled: attr(BooleanType),

        display_booking_type: (() ->
            if @get('isInterview')
                return "Interview"
            return @get('booking_type')
        ).property('booking_type')

        isInterview: (() ->
            return @get('booking_type') && @get('booking_type').indexOf("Interview") != -1
        ).property('booking_type')
            
        isMeetupInterview: (() ->
            return @get('booking_type') == "Meetup Interview" || @get('booking_type') == "Interview"
        ).property('booking_type')
            
        isPhoneInterview: (() ->
            return @get('booking_type') == "Phone Interview"
        ).property('booking_type')

        kidsString: (() ->
            if @get('num_children') == 1
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
            if @get("accepted_sitter")
                return @get("accepted_sitter")
            return this.get('sitters.firstObject')
        ).property('sitters.firstObject')

        formattedDate: (() ->
            date = @get('start_date_time')
            if not date
                return ""
            return moment(date).format('ddd, MMM Do')
        ).property("start_date_time")
        formattedHours: (() ->
            start = @get('start_date_time')
            stop = @get('stop_date_time')
            if not start or not stop
                return ""
            startHour = moment(start).format('h:mm a');
            endHour = moment(stop).format('h:mm a');
            return startHour + " — " + endHour
        ).property('start_date_time', 'stop_date_time')

        startHour: ((key, value) ->
            date = @get('start_date_time')
            if not date and not value
                return
            if not value?
                return moment(date).format("HHmm")
            else
                date = moment(date) or moment()
                value_date = moment(value, "HHmm")
                date.hour(value_date.hour())
                date.minute(value_date.minute())
                @set('start_date_time', date.toDate())
                return value
        ).property('start_date_time')

        endHour: ((key, value) ->
            date = @get('stop_date_time')
            if not date and not value
                return
            if not value?
                return moment(date).format("HHmm")
            else
                date = moment(date) or moment()
                value_date = moment(value, "HHmm")
                date.hour(value_date.hour())
                date.minute(value_date.minute())
                @set('stop_date_time', date.toDate())
                return value
        ).property('stop_date_time')

        calendarDate: ((key, value) ->
            fmt_str = "ddd, Do MMM YYYY"
            date = @get('start_date_time')
            date = moment(date)
            if not date and not value
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

        hasMultipleSitters: (() ->
            return @get("sitters.length") > 1 and not @get("accepted_sitter")
        ).property("sitters")

        isPending: (() ->
            if this.get('canceled')
                return false
            accepted = Boolean(this.get('accepted_sitter'))
            declined_sitters = this.get('declined_sitters')
            if declined_sitters.filterProperty("id", Sitterfied.currentUser.get("id")).length > 0
                return false
            now = moment().toDate()
            future = this.get('start_date_time') > now
            return not accepted and future
        ).property('accepted_sitter', 'declined_sitters.@each', 'start_date_time', 'canceled', 'isLoaded')

        isUpcoming: (() ->
            if this.get('canceled')
                return false
            accepted = Boolean(this.get('accepted_sitter'))
            if accepted
                if Sitterfied.get("isSitter") and this.get('accepted_sitter.id') != Sitterfied.currentUser.get("id")
                    return false
                now = moment().toDate()
                future = this.get('start_date_time') > now
                return  accepted and future
            else
                return false
        ).property('accepted_sitter', 'start_date_time', 'canceled', 'isLoaded')


        isCompleted: (() ->
            if this.get('canceled')
                return false
            accepted = Boolean(this.get('accepted_sitter'))
            now = moment().toDate()
            future = this.get('start_date_time') > now
            return  accepted and not future
        ).property('accepted_sitter', 'start_date_time', 'canceled', 'isLoaded')


        isMissed: (() ->
            if this.get('canceled')
                return false
            accepted = Boolean(this.get('accepted_sitter'))
            now = moment().toDate()
            future = this.get('start_date_time') > now
            return  not accepted and not future
        ).property('accepted_sitter', 'start_date_time', 'canceled', 'isLoaded')

        isDeclined: (() ->
            declined_sitters = this.get('declined_sitters')
            if declined_sitters.get("length") == 0
                return false
            if declined_sitters.filterProperty("id", Sitterfied.currentUser.get("id")).length > 0
                return true
            return false
        ).property('declined_sitters', 'declined_sitters.@each')


    )
    Sitterfied.Booking.adapter = Adapter.create()

    Sitterfied.BookingRequest = Ember.Model.extend(
        id: attr()
        booking: belongsTo("Sitterfied.Booking", {key:"booking"})
    )
    Sitterfied.BookingRequest.adapter = Adapter.create()
