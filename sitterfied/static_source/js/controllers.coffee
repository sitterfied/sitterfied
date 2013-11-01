define ["ember", "cs!sitterfied", 'moment', "cs!models"], (Em, Sitterfied) ->

    Sitterfied.CurrentUserController = Em.ObjectController.extend({
        needs: ['certifications'
                'languages'
                'specialneeds'
                'otherServices'
                'friends'
                'bookings'
                'children']
        accountType: parent_or_sitter

        isSitter: (() ->
            Sitterfied.accountType == "Sitter"
        ).property('parent_or_sitter', 'Sitterfied.accountType')

        isParent: (() ->
            Sitterfied.accountType == "Parent"
        ).property('parent_or_sitter', 'Sitterfied.accountType')

        saveSettings: () ->
            Em.run.begin()
            model = this.get('model')
            model.set('isDirty', true)
            model.save()
            model.get('settings').save()
            model.get('children')?.save().then((children) ->
                Sitterfied.currentUser.get('children').set('data', children)
                @newChild()
            )
            Em.run.end()

        deleteAccount: () ->
            imsure = confirm("are you sure you want to delete your account? This cannot be undone")
            if imsure
                $.ajax
                    type: "POST"
                    url:"/api/users/" + Sitterfied.currentUser.id + "/active/"
                    dataType: 'json'
                    data: {
                        active: false
                    }
                    success: (response) ->
                        location.reload()
                    error: () ->
                        alert("There was a problem deleting your account. Please try again")

        old_password : ''
        new_password1 : ''
        new_password2 : ''
        resetPassword: () ->
            if @get('new_password1') != @get('new_password2')
                alert("Your passwords must match")
                return
            data = {
                new_password1: @get('new_password1')
                new_password2: @get('new_password2')
                old_password: @get('old_password')
            }
            $.post('password_change/', data).success(alert('password changed'))

        invite: () ->
            alert("invite friends")

        deleteGroup: (group) ->
            groups = @get("sitter_groups")
            toBlock = groups.findProperty('id', group.get('id'))
            groups.removeObject(toBlock)
            @set('isDirty', true)


        newChild: () ->
            if Sitterfied.currentUser.get('children').objectAt(0)?.get('isNew')
                return
            newChild = Sitterfied.Child.create(
                parent: this.get('content')
                name:""
                school: ""
                dob: new Date
            )
            Sitterfied.currentUser.get('children').insertAt(0, newChild)


        addFriend: (friend_id) ->
            friend = Sitterfied.User.find(friend_id)
            @get('model').addFriend(friend)

        removeFriend: (friend_id) ->
            friend = Sitterfied.User.find(friend_id)
            @get('model').removeFriend(friend)



        addGroup: (group_id) ->
            groups = @get('sitter_groups')
            if groups.findProperty('id', group_id)
                return

            group = Sitterfied.Group.find(group_id)
            groups.pushObject(group)

            Sitterfied.currentUser.set('isDirty', true)
            Sitterfied.currentUser.save()

        createGroup: (groupName) ->
            groups = @get('sitter_groups')

            group = Sitterfied.Group.create({name:groupName})
            group.save().then () ->
                groups.pushObject(group)

                Sitterfied.currentUser.set('isDirty', true)
                Sitterfied.currentUser.save()



        saveCertification: () ->
            newCert = this.get('controllers.certifications.newCert')
            if newCert == ''
                return
            Sitterfied.Certification.create({certification:newCert}).save()
            this.set('controllers.certifications.newCert', '')

        saveService: () ->
            newService = this.get('controllers.otherServices.newService')
            if newService == ''
                return
            Sitterfied.OtherService.create({service:newService}).save()
            this.set('controllers.otherServices.newService', '')

        saveLanguage: () ->
            newLanguage = this.get('controllers.languages.newLanguage')
            if newLanguage == ''
                return
            Sitterfied.Language.create({language:newLanguage}).save()
            this.set('controllers.languages.newLanguage', '')

        saveNeed: () ->
            newNeed = this.get('controllers.specialneeds.newNeed')
            if newNeed == ''
                return
            Sitterfied.SpecialNeed.create({need:newNeed}).save()
            this.set('controllers.specialneeds.newNeed', '')

        gmailConnect: ()->
            window.open("/googleoauthbegin/")


        facebookConnect: ()->
            use_fb_data = () ->
                access_token = FB.getAccessToken()
                facebook_id = FB.getUserID()
                Sitterfied.currentUser.set('facebook_token', access_token)
                Sitterfied.currentUser.set('facebook_id', facebook_id)
                promise = Sitterfied.currentUser.save()
                promise.then () ->
                    $.ajax
                        url: "/facebook_import/"
                        success: () ->
                            alert("facebook connected")

            FB.getLoginStatus((response) ->
                if response.status is "connected"
                    use_fb_data()
                else if response.status is "not_authorized"
                    FB.login ->
                        use_fb_data()
            ,true)

    })

    Sitterfied.BookingsController  = Em.ArrayController.extend(
        pendingRequests: (() ->
            return @get('content').filter (item, index, content) ->
                if item.get('canceled')
                    return false
                accepted = Boolean(item.get('accepted_sitter'))
                now = new Date()
                future = item.get('start_date_time') > now
                return not accepted and future

        ).property('content.@each.accepted_sitter', 'content.@each.start_date_time', 'content.@each.canceled')

        upcomingJobs: (() ->
            return @get('content').filter (item, index, content) ->
                if item.get('canceled')
                    return false

                accepted = Boolean(item.get('accepted_sitter'))
                now = new Date()
                future = item.get('start_date_time') > now
                return  accepted and future
        ).property('content.@each.accepted_sitter', 'content.@each.start_date_time', 'content.@each.canceled')

        completedJobs: (() ->
            return @get('content').filter (item, index, content) ->
                if item.get('canceled')
                    return false

                accepted = Boolean(item.get('accepted_sitter'))
                now = new Date()
                future = item.get('start_date_time') > now
                return  accepted and not future
        ).property('content.@each.accepted_sitter', 'content.@each.start_date_time', 'content.@each.canceled')

        missedRequests: (() ->
            return @get('content').filter (item, index, content) ->
                if item.get('canceled')
                    return false

                accepted = Boolean(item.get('accepted_sitter'))
                now = new Date()
                future = item.get('start_date_time') > now
                return  not accepted and not future
        ).property('content.@each', 'content.@each.accepted_sitter', 'content.@each.start_date_time', 'content.@each.canceled')

        canceledRequests: (() ->
            return @get('content').filter (item, index, content) ->
                return item.get('canceled')
        ).property('content.@each.canceled')

        declinedRequests: (() ->
            return @get('content').filter (item, index, content) ->
                declined_sitters = item.get('declined_sitters')
                return declined_sitters.indexOf(item.get('content')) != -1
        ).property('content.@each.declined_sitters')



    )

    Sitterfied.BookController = Em.ObjectController.extend(
        cancel: () ->
            this.transitionTo('search');
        book: () ->
            booking = Sitterfied.get('onDeckBooking')
            promise = booking.save()
            promise.then (booking) =>
                #for some reason, this first load strips out start_date and end_date.
                #it's in the json, just doesn't make it to the object. select2 perhaps?
                p = booking.reload()
                p.then =>
                    Sitterfied.currentUser.get('bookings').pushObject(booking)
                    this.transitionTo('done', booking);

        multiple: (() ->
            return @get('sitters.length') > 1
        ).property("sitters.@each")
    )


    Sitterfied.EditBookController = Em.ObjectController.extend(
        cancel: () ->
            this.transitionTo('mybookings');
        book: () ->
            booking = @get('model')
            booking.save()
            this.transitionTo('done', booking);
        multiple: (() ->
            return @get('sitters.length') > 1
        ).property("sitters.@each")
    )




    Sitterfied.SitterEditSchedlueController =  Em.ObjectController.extend({
        saveSchedlue: () ->
            @get('model').save()
        checkAll: () ->
            model = @get('model')
            attrs = Object.keys(model.toJSON())
            attrs.pop('sitter')
            for x in attrs
                @set(x, true)
        clearAll: () ->
            model = @get('model')
            attrs = Object.keys(model.toJSON())
            attrs.pop('sitter')
            for x in attrs
                @set(x, false)

    })

    Sitterfied.SitterEditBookingsController =  Sitterfied.BookingsController.extend



    Sitterfied.DoneController = Em.ObjectController.extend(
        edit: (booking)  ->
            this.transitionTo('editBook', booking)

        cancel: (booking) ->
            cancel = confirm("are you sure you want to cancel this booking request?")
            if cancel
                this.get('content').deleteRecord()
                this.transitionTo('search')
    )

    Sitterfied.stateController  = Em.ArrayController.create(
        content: Sitterfied.States
    )
    Sitterfied.educationController  = Em.ArrayController.create(
        content: Sitterfied.Educations
    )
    Sitterfied.CertificationsController  = Em.ArrayController.extend(
        newCert: ''
    )
    Sitterfied.OtherServicesController  = Em.ArrayController.extend(
        newService: ''
    )
    Sitterfied.SpecialneedsController  = Em.ArrayController.extend(
        newNeed: ''
    )
    Sitterfied.LanguagesController  = Em.ArrayController.extend(
        newLanguage: ''
    )
    Sitterfied.SitterController  = Em.ObjectController.extend(
        book: () ->
            booking = Sitterfied.Booking.create
                parent: Sitterfied.currentUser
                notes: ""
                overnight: false
                booking_status: "Pending"
                booking_type: "Job"
                start_date_time: moment().toDate()
                stop_date_time: moment().toDate()
                address1: Sitterfied.get('currentUser.address1')
                address2: Sitterfied.get('currentUser.address2')
                city: Sitterfied.get('currentUser.city')
                state: Sitterfied.get('currentUser.state')
                zip: Sitterfied.get('currentUser.zip')
                num_children: Sitterfied.get('currentUser.children.length')
                emergency_phone: Sitterfied.get('currentUser.emergency_contact_one_phone')
                rate: 0
            sitters = [@get('content')]
            booking.get('sitters').addObjects(sitters)
            Sitterfied.set('onDeckBooking', booking)
            this.transitionTo('book')

        interview: () ->
            booking = Sitterfied.Booking.create
                parent: Sitterfied.currentUser
                notes: ""
                overnight: false
                booking_status: "Pending"
                booking_type: "Interview"
                start_date_time: moment().toDate()
                stop_date_time: moment().toDate()
                address1: Sitterfied.get('currentUser.address1')
                address2: Sitterfied.get('currentUser.address2')
                city: Sitterfied.get('currentUser.city')
                state: Sitterfied.get('currentUser.state')
                zip: Sitterfied.get('currentUser.zip')
                num_children: Sitterfied.get('currentUser.children.length')
                emergency_phone: Sitterfied.get('currentUser.emergency_contact_one_phone')
                rate: 0
            sitters = [@get('content')]
            booking.get('sitters').addObjects(sitters)
            Sitterfied.set('onDeckBooking', booking)
            this.transitionTo('book')


    )
    Sitterfied.SitterReviewController  = Em.ObjectController.extend(
    )
    Sitterfied.SearchSitterController  = Em.ObjectController.extend(
        selectTeamClass: (() ->
            if @get('inSitterTeam')
                return 'team'
            if @get('inFriendsTeam')
                return 'friends'
            if @get('inLocalTeam')
                return 'local'
        ).property('inSitterTeam', 'inFriendsTeam', 'inLocalTeam')

        inFriendsTeam: (() ->
            return @get('in_friends_team') and not @get('inSitterTeam')
        ).property('inSitterTeam')

        inLocalTeam: (() ->
            return not @get('in_friends_team') and not @get('inSitterTeam')
        ).property('inSitterTeam')

        isSelected: (() ->
            selected = @get('parentController.selectedSitters')
            return selected.indexOf(@get('content')) != -1
        ).property('parentController.selectedSitters.@each')

        passesFilters: (() ->
            languages = @get("parentController.languages")
            highest_education = @get("parentController.highest_education")
            certifications = @get("parentController.certifications")
            services = @get("parentController.services")
            if services.length == 0 and
            certifications.length == 0 and
            !highest_education? and
            languages.length == 0
                return true
            sitter_languages = @get('languages')
            sitter_highest_education = @get('highest_education')
            sitter_certifications = @get('certifications')
            sitter_services = @get('services')
            if highest_education == sitter_highest_education
                return true
            if  _.intersection(languages, sitter_languages).length > 0 or
            _.intersection(certifications, sitter_certifications).length > 0 or
            _.intersection(services, sitter_services).length > 0
                return true
            return false

        ).property("parentController.languages.@each", "parentController.highest_education",
            "parentController.certifications.@each", "parentController.services.@each",)

    )
    Sitterfied.ChildrenController  = Em.ArrayController.extend(
    )

    Sitterfied.SearchController  = Em.ArrayController.extend(
        multipleSitters: false
        filterSitters: false
        sortSitters: false
        needs: ['certifications'
                'languages'
                #'specialneeds'
                'otherServices'
                ]

        toggleSortSitters: () ->
            isSortSitters = @get('sortSitters')
            @set('sortSitters', !isSortSitters)

        toggleMultipleSitters: () ->
            isMultipleSitters = @get('multipleSitters')
            #ugly hack :(
            if @get('didScrollHide') and isMultipleSitters
                @notifyPropertyChange('multipleSitters')
            else
                @set('multipleSitters', !isMultipleSitters)

        toggleFilterSitters: () ->
            isFilterSitters = @get('filterSitters')
            @set('filterSitters', !isFilterSitters)

        sortSet:(sortProp, direction) ->
            Em.run.begin()
            @set('sortProperties', [])
            @get('sortProperties').push(sortProp)
            #for hilight
            @set('sortProperty', sortProp)

            @set('sortAscending', direction)

            #force a resort
            Em.run.end()
            @notifyPropertyChange('content')




        resetFilters: () ->
            Em.run.begin()
            @set('highest_education', null)
            @set('languages', [])
            @set('services', [])
            @set('certifications', [])
            Em.run.end()

        itemController: 'searchSitter'

        zip : ""
        when: undefined
        from : 2
        to : 5
        kids : 1
        overnight : false
        date_to : undefined
        findSitters : () ->
            $.get("/api/search/", {'zip':@get('zip')}).then (response) =>
                sitters = Em.A()
                for sitter in response
                    s = Sitterfied.Sitter.create()
                    s.load(sitter['id'], sitter)
                    sitters.pushObject(s)
                this.set('model', sitters)

        content: []
        selectedSitters:  Ember.ArrayProxy.create
            content: Ember.A()

        sitterTeam: (() ->
            return @filterProperty('inSitterTeam', true)
        ).property('content.@each.inSitterTeam')

        friendTeam: (() ->
            return @filterProperty("inFriendsTeam", true)
        ).property('content.@each.inSitterTeam')

        localTeam: (() ->
            return @filterProperty("inLocalTeam", true)
        ).property('content.@each.inSitterTeam')

        filteredSitterTeam: (() ->
            return @get('sitterTeam').filterProperty("passesFilters", true)
        ).property('sitterTeam.@each.passesFilters', 'sitterTeam.length')

        filteredFriendTeam: (() ->
            return @get('friendTeam').filterProperty("passesFilters", true)
        ).property('friendTeam.@each.passesFilters', 'friendTeam.length')

        filteredLocalTeam: (() ->
            return @get('localTeam').filterProperty("passesFilters", true)
        ).property('localTeam.@each.passesFilters', 'localTeam.length')

        zoomToLocalTeam: () ->
            $.scrollTo("#local_sitter_title", 500, {offset:-300})
        zoomToFriendTeam: () ->
            $.scrollTo("#myfriends_sitter_title", 500, {offset:-300})
        zoomToSitterTeam: () ->
            $.scrollTo("#sitterteam", 500, {offset:-200})

        multipleSittersText: (() ->
            selectedSitters = @get('selectedSitters')

            if not @get('multipleSitters') or Em.isEmpty(selectedSitters)
                return "Select multiple sitters"
            else
                if selectedSitters.get('length') > 1
                    return selectedSitters.get('lastObject.full_name') + " and " + (selectedSitters.get('length')-1) + " other sitters"
                else
                    return selectedSitters.get('lastObject.full_name')

        ).property("selectedSitters.@each", "multipleSitters")

        selectedSitterTeam: (() ->
            return @get('selectedSitters').filterProperty("in_sitter_team", true)
        ).property('selectedSitters.@each')
        selectedFriendTeam: (() ->
            return @get('selectedSitters').filterProperty("in_friends_team", true)
        ).property('selectedSitters.@each')
        selectedLocalTeam: (() ->
            return @get('selectedSitters').filterProperty("in_friends_team", false).filterProperty('in_sitter_team', false)
        ).property('selectedSitters.@each')

        selectSitter: (sitter) ->
            selected = @get('selectedSitters')
            if selected.indexOf(sitter) == -1
                selected.pushObject(sitter)
            else
                selected.removeObject(sitter)

        clearSelected: () ->
            @set('selectedSitters.content', Em.A())

        addFriendsSitters: () ->
            selected = @get('selectedSitters')
            for sitter in @get('friendTeam')
                if selected.indexOf(sitter) == -1
                    selected.pushObject(sitter)

        book: (sitters) ->
            if not Sitterfied.typeIsArray sitters
                sitters = [sitters]

            if @get('overnight')
                stop_date = @get('stop_date')
            else
                stop_date = @get('start_date')

            start_moment = moment(@get('start_date'))
            start_time = moment(@get('start_time'), "HHmm")

            start_moment.hour(start_time.hour())
            start_moment.minute(start_time.minutes())
            start_date_time = start_moment.toDate()


            stop_moment = moment(stop_date)
            stop_time = moment(@get('stop_time'), "HHmm")
            stop_moment.hour(stop_time.hour())
            stop_moment.minute(stop_time.minutes())
            stop_date_time = stop_moment.toDate()

            booking = Sitterfied.Booking.create
                parent: Sitterfied.currentUser
                notes: ""
                overnight: @get("overnight")
                booking_status: "Pending"
                booking_type: "Job"
                start_date_time: start_date_time
                stop_date_time: stop_date_time
                address1: Sitterfied.get('currentUser.address1')
                address2: Sitterfied.get('currentUser.address2')
                city: Sitterfied.get('currentUser.city')
                state: Sitterfied.get('currentUser.state')
                zip: Sitterfied.get('currentUser.zip')
                num_children: @get('kids')
                emergency_phone: Sitterfied.get('currentUser.emergency_contact_one_phone')
                rate: 0
            booking.get('sitters').addObjects(sitters)

            Sitterfied.set('onDeckBooking', booking)
            this.transitionTo('book')

        interview: (sitters) ->
            if not Sitterfied.typeIsArray sitters
                sitters = [sitters]

            if @get('overnight')
                stop_date = @get('start_date')
            else
                stop_date = @get('stop_date')

            start_moment = moment(@get('start_date'))
            start_time = moment(@get('start_time'), "HHmm")
            start_moment.hour(start_time.hour())
            start_moment.minute(start_time.minute())
            start_date_time = start_moment.toDate()

            stop_moment = moment(stop_date)
            stop_time = moment(@get('stop_time'), "HHmm")
            stop_moment.hour(stop_time.hour())
            stop_moment.minute(stop_time.minute())
            stop_date_time = stop_moment.toDate()


            booking = Sitterfied.Booking.create
                parent: Sitterfied.currentUser
                notes: ""
                overnight: false
                booking_status: "Pending"
                booking_type: "Interview"
                start_date_time: start_date_time
                stop_date_time: stop_date_time
                address1: Sitterfied.get('currentUser.address1')
                address2: Sitterfied.get('currentUser.address2')
                city: Sitterfied.get('currentUser.city')
                state: Sitterfied.get('currentUser.state')
                zip: Sitterfied.get('currentUser.zip')
                num_children: Sitterfied.get('currentUser.children.length')
                emergency_phone: Sitterfied.get('currentUser.emergency_contact_one_phone')
                rate: 0
            booking.get('sitters').addObjects(sitters)
            Sitterfied.set('onDeckBooking', booking)
            this.transitionTo('book')
    )

    Sitterfied.BookingController = Em.ObjectController.extend(
        isNoteShown: false
        toggleNote: () ->
            isNoteShown = @get('isNoteShown')
            @set('isNoteShown', !isNoteShown)

        cancelBooking: (booking) ->
            $.ajax
                type: "POST"
                url:"/api/bookings/" + booking.get('id') + "/cancel_booking/"
                dataType: 'json'
                success: (response) ->
                    booking.load(booking.get('id'), response)
                error: () ->
                    alert("There was a problem canceling this booking. Please try again")

        declineBooking: (booking) ->
            $.ajax
                type: "POST"
                url:"/api/bookings/" + booking.get('id') + "/decline_booking/"
                dataType: 'json'
                success: (response) ->
                    booking.load(booking.get('id'), response)
                error: () ->
                    alert("There was a problem declining this booking. Please try again")

        acceptBooking: (booking) ->
            $.ajax
                type: "POST"
                url:"/api/bookings/" + booking.get('id') + "/accept_booking/"
                dataType: 'json'
                data:
                    booking: booking.get('id')
                success: (response) ->
                    booking.load(booking.get('id'), response)
                error: () ->
                    alert("There was a problem accepting this booking. Please try again")


        rate: ( () ->
            num_children = @get('num_children')
            sitter = @get('sitter')
            if not sitter?
                return ""
            if num_children == 1
                min_rate = sitter.get('one_child_min_rate')
                max_rate = sitter.get('one_child_max_rate')
            else if num_children == 2
                min_rate = sitter.get('two_child_min_rate')
                max_rate = sitter.get('two_child_max_rate')
            else
                min_rate = sitter.get('three_child_min_rate')
                max_rate = sitter.get('three_child_max_rate')
            rate = "#{min_rate} - #{max_rate}"
        ).property('sitter','num_children', 'sitter.one_child_min_rate', 'sitter.one_child_max_rate', 'sitter.two_child_min_rate', 'sitter.two_child_max_rate','sitter.three_child_min_rate', 'sitter.three_child_max_rate')


    )

    Sitterfied.ParentEditSitterTeamController  = Em.ArrayController.extend(
    )

    Sitterfied.ParentController  = Em.ObjectController.extend(
        addFriend: () ->
            Sitterfied.currentUser.addFriend(this.get('model'))
    )


    Sitterfied.ParentEditBookingsController  = Sitterfied.BookingsController.extend()

    Sitterfied.SignupController  = Em.Controller.extend(
        parentSitter: "Parent"

        isSitter: (() ->
            return @get("parentSitter") == "Sitter"
        ).property("parentSitter")

        signup: () ->
            username =@get('firstName') + @get('lastName')
            $.post( "/signup-ajax/",
                parent_or_sitter: @get('parentSitter').toLowerCase()
                first_name: @get('firstName')
                username: username
                last_name: @get('lastName')
                zipcode: @get('zipcode')
                password1: @get('password')
                password2: @get('password2')
                email: @get('email')

            ).done( (data) ->
                user_json = data.user
                user = Sitterfied.loadUserJson(user_json)
                Sitterfied.set('currentUserController.model', user)
                Sitterfied.set('isAuthenticated', true)
                parent_or_sitter = user.get('parent_or_sitter')
                $.fancybox.close()

            ).fail( (data) ->
                alert("there was an error registering you")
            )
    )


    Sitterfied.LoginController  = Em.Controller.extend
        login: () ->
            username = @get('email')
            password = @get('password')
            $.post( "/login-ajax/",
                username:username
                password:password
            ).done((data) ->
                user_json = data.user
                user = Sitterfied.loadUserJson(user_json)
                Sitterfied.set('currentUserController.model', user)
                Sitterfied.set('isAuthenticated', true)
                parent_or_sitter = user.get('parent_or_sitter')
                $.fancybox.close()
            ).fail((data) ->
                alert("there was an error logging you in. Please try again!")
            )






    Sitterfied.FriendsController  = Em.ArrayController.extend(
        parents: (() ->
            return this.get('content').filterProperty("parent_or_sitter", "Parent")
        ).property('content.@each.parent_or_sitter', 'content.[]')
        sitters: (() ->
            return this.get('content').filterProperty("parent_or_sitter", "Sitter")
        ).property('content.@each.parent_or_sitter', 'content.[]')
    )

    Sitterfied.ApplicationController = Ember.Controller.extend
        needs: ['sitterReview', 'friends']

        postReivew: () ->
            $.fancybox.close()
            reviewController = this.get("controllers.sitterReview")
            review = reviewController.get('model')
            review.save()
            reviewController.set('model', Sitterfied.SitterReview.create(parent: Sitterfied.currentUser))
