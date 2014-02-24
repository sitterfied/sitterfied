define ["jquery", "ember", "cs!sitterfied", 'moment', "cs!models"], ($, Em, Sitterfied) ->

    Sitterfied.CurrentUserController = Em.ObjectController.extend({
        needs: ['certifications'
                'languages'
                'specialneeds'
                'otherServices'
                'friends'
                'bookings'
                'children']
        accountType: parent_or_sitter
        activeReviewPanelUser: null
        sitters_to_review: []
        reviews: []

        isSitter: (() ->
            Sitterfied.accountType == "Sitter"
        ).property('parent_or_sitter', 'Sitterfied.accountType')

        isParent: (() ->
            Sitterfied.accountType == "Parent"
        ).property('parent_or_sitter', 'Sitterfied.accountType')

        saveSettings: () ->
            model = this.get('model')
            model.set('isDirty', true)
            modelP = model.save()
            settings = model.get('settings')
            if settings.get("isLoaded")
                settings.save()
            childrenP = model.get('children')?.save()
            childrenP?.then((children) ->
                Sitterfied.currentUser.get('children').set('data', children)
                @newChild()
            )
            return Em.RSVP.all([modelP, settingsP?, childrenP])

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
            $.post('password_change/', data)

        invite: () ->
            alert("invite friends")

        deleteGroup: (group) ->
            groups = @get("sitter_groups")
            toBlock = groups.findProperty('id', group.get('id'))
            groups.removeObject(toBlock)
            @set('isDirty', true)
            @get('content').save()


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
            friendPromise = Sitterfied.User.fetch(friend_id)
            friendPromise.then (friend) =>
                @get('model').removeFriend(friend)
                # Remove to sitter team if user is parent and friend is sitter
                if Sitterfied.currentUser.get('isParent')
                    if friend.get('isSitter')
                        Em.run.begin()
                        sitterTeam = Sitterfied.currentUser.get('sitter_teams')
                        sitter = sitterTeam.findProperty('id', friend.get('id'))
                        sitterTeam.removeObject(sitter)
                        sitter.get('sitter_teams').removeObject(Sitterfied.currentUser)
                        Sitterfied.currentUser.set('isDirty', true)
                        Sitterfied.currentUser.save()
                        Em.run.end()


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

        update_reviews: (() ->
            #Populate reviews
            this.set("reviews", Sitterfied.currentUser.get('reviews').toArray())

            #Populate users to review
            results = Em.A()
            parent = Sitterfied.currentUser
            revs = parent.get('reviews').toArray()
            sitter_id_set = new Em.Set()

            #Get existing reviews
            for rev in revs
                if rev.get('sitter')
                    sitter_id_set.add(rev.get('sitter').get('id'))

            #Include sitters that has no reviews
            bookings = parent.get('bookings').toArray()
            for booking in bookings
                accepted_sitter = booking.get('accepted_sitter')
                if accepted_sitter and not sitter_id_set.contains(accepted_sitter.get('id'))
                    results.pushObject(accepted_sitter)
            this.set('sitters_to_review', results.uniq())
            return null
        ).property("Sitterfied.currentUser.reviews.@each", "Sitterfied.currentUser.reviews.@each.sitter", "Sitterfied.currentUser.bookings.@each", "Sitterfied.currentUser.bookings.@each.accepted_sitter")

        openReviewPopup: (reviewedUser) ->
            parent = Sitterfied.currentUser
            $("#sitter_id").val(reviewedUser.get('id'))
            this.set('activeReviewPanelUser', reviewedUser)

            $(".popup_title").html("How did it go with " + reviewedUser.get('first_name') + "?")

            promise = parent.sitter_reviews()
            promise.then (revs) =>
                results = Em.A()
                review_length = revs.get('length')
                index = 0
                while index < review_length
                    results.pushObject(revs.content.get(index))
                    index++

                review_exists = false
                for rev in results
                    if rev.get('sitter').get('id') is reviewedUser.get('id') and rev.get('parent').get('id') is parent.get('id')
                        review_exists = true
                        current_review = rev
                        break

                if review_exists
                    $("#recommended").prop('checked', current_review.get('recommended'))
                    $("#rehire").prop('checked', current_review.get('rehire'))
                    $("#review").val(current_review.get('review'))
                else
                    $("#recommended").prop('checked', false)
                    $("#rehire").prop('checked', false)
                    $("#review").val('')

                $.fancybox
                    href: "#recommend_popup"
                    maxWidth: 960
                    maxHeight: 800
                    minWidth: 700
                    minHeight: 480
                    fitToView: false
                    width: "90%"
                    height: "90%"


        googlePoll: () ->
            that = this
            try
                #check if we have access to the window
                that.google_window.history
                location.reload()
            catch error
                window.setInterval((->
                    that.googlePoll()), 1000)

        gmailConnect: ()->
            that = this
            this.google_window = window.open("/googleoauthbegin/")
            window.setInterval((->
                    that.googlePoll()), 3000)


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
                            location.reload()

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
                return item.get('isPending')
        ).property('content.@each.isPending', )

        upcomingJobs: (() ->
            return @get('content').filter (item, index, content) ->
                return item.get('isUpcoming')
        ).property('content.@each.isUpcoming')

        completedJobs: (() ->
            return @get('content').filter (item, index, content) ->
                return item.get('isCompleted')
        ).property('content.@each.isCompleted')

        missedRequests: (() ->
            return @get('content').filter (item, index, content) ->
                return item.get('isMissed')
        ).property('content.@each.isMissed')

        canceledRequests: (() ->
            return @get('content').filter (item, index, content) ->
                return item.get('canceled')
        ).property('content.@each.canceled', 'content.@each.isLoaded')

        declinedRequests: (() ->
            return @get('content').filter (item, index, content) ->
                return item.get('isDeclined')
        ).property('content.@each.isDeclined')

    )

    Sitterfied.BookController = Em.ObjectController.extend(
        pending: false
        
        cancel: () ->
            @transitionToRoute('search');

        book: () ->
            console.log("Start book")

            #debounce clicks
            if @get("pending")
                return
                
            @set("pending", true)
            booking = Sitterfied.get('onDeckBooking')
            
            console.log("Booking:", booking)
                
            booking.save()
                .then (booking) =>
                    p = booking.reload()
                    p.then =>
                        Sitterfied.currentUser.get('bookings').pushObject(booking)
                        @set('pending', false)
                        @transitionToRoute('done', booking)
                .then null, (reason) =>
                    @set('pending', false)
            
        multiple: (() ->
            return @get('sitters.length') > 1
        ).property("sitters.@each")
    )


    Sitterfied.EditBookController = Em.ObjectController.extend(
        cancel: () ->
            @transitionToRoute('mybookings');
        book: () ->
            booking = @get('model')
            booking.save()
            @transitionToRoute('done', booking);
        multiple: (() ->
            return @get('sitters.length') > 1
        ).property("sitters.@each")
    )




    Sitterfied.SitterEditScheduleController =  Em.ObjectController.extend({
        saveSchedule: () ->
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
            @transitionToRoute('editBook', booking)

        cancel: (booking) ->
            cancel = confirm("are you sure you want to cancel this booking request?")
            if cancel
                this.get('content').deleteRecord()
                @transitionToRoute('search')
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
            start_date_time = Sitterfied.onDeckBookingAttrs['start_date_time'] || moment().toDate()
            stop_date_time = Sitterfied.onDeckBookingAttrs['stop_date_time'] || moment().toDate()
            kids = Sitterfied.onDeckBookingAttrs['kids'] || Sitterfied.get('currentUser.children.length')
            overnight = Sitterfied.onDeckBookingAttrs['overnight'] || false

            booking = Sitterfied.Booking.create
                parent: Sitterfied.currentUser
                notes: ""
                overnight: overnight
                booking_status: "Pending"
                booking_type: "Job"
                start_date_time: start_date_time
                stop_date_time: stop_date_time
                address1: Sitterfied.get('currentUser.address1')
                address2: Sitterfied.get('currentUser.address2')
                city: Sitterfied.get('currentUser.city')
                state: Sitterfied.get('currentUser.state')
                zip: Sitterfied.get('currentUser.zip')
                num_children: kids
                emergency_phone: Sitterfied.get('currentUser.cell')
                rate: 0
            sitters = [@get('content')]
            booking.get('sitters').addObjects(sitters)
            Sitterfied.set('onDeckBooking', booking)
            @transitionToRoute('book')

        open_interview_popup: () ->
            $.fancybox
                href: "#interview_popup"
                maxWidth: 390
                maxHeight: 257
                minWidth: 390
                minHeight: 257
                fitToView: false
                closeBtn: false
                enableEscapeButton: false
                width: "90%"
                height: "90%"
        
        interview: (interview_type) ->
            $.fancybox.close()
            
            start_date_time = (Sitterfied.onDeckBookingAttrs && Sitterfied.onDeckBookingAttrs['start_date_time']) || moment().toDate()
            stop_date_time = (Sitterfied.onDeckBookingAttrs && Sitterfied.onDeckBookingAttrs['stop_date_time']) || moment().toDate()
            kids = (Sitterfied.onDeckBookingAttrs && Sitterfied.onDeckBookingAttrs['kids']) || Sitterfied.get('currentUser.children.length')
            overnight = (Sitterfied.onDeckBookingAttrs && Sitterfied.onDeckBookingAttrs['overnight']) || false
                
            booking_type = interview_type + " Interview"

            booking = Sitterfied.Booking.create
                parent: Sitterfied.currentUser
                notes: ""
                overnight: overnight
                booking_status: "Pending"
                booking_type: booking_type
                start_date_time: start_date_time
                stop_date_time: stop_date_time
                address1: Sitterfied.get('currentUser.address1')
                address2: Sitterfied.get('currentUser.address2')
                city: Sitterfied.get('currentUser.city')
                state: Sitterfied.get('currentUser.state')
                zip: Sitterfied.get('currentUser.zip')
                num_children: kids
                emergency_phone: Sitterfied.get('currentUser.cell')
                rate: 0
            sitters = [@get('content')]
            booking.get('sitters').addObjects(sitters)
            Sitterfied.set('onDeckBooking', booking)
            @transitionToRoute('book')

        showBioLink: (() ->
            # hide read more link if text < 100 characters
            bioLength = this.get('biography')?.length
            if bioLength < 100
                return false
            else
                return true
        ).property('biography')
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
            return @get('friends_in_common').length > 0 and not @get('inSitterTeam')
        ).property('inSitterTeam')

        inLocalTeam: (() ->
            return @get('friends_in_common').length == 0 and not @get('inSitterTeam')
        ).property('inSitterTeam')

        isSelected: (() ->
            selected = @get('parentController.selectedSitters')
            return selected.filterProperty("id", @get('id')).length > 0
        ).property('parentController.selectedSitters.@each', "parentController.selectedSitters.content")

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
        searched: false

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

        zip : (->
            return Sitterfied.currentUser.get('zip')
        ).property()
        
        when: undefined
        start_time: '1800'
        stop_time: '2200'
        kids : 1
        overnight : false
        date_to : undefined

        findSitters : () ->
            sitters = Em.A()
            zip = @get("zip")
            start_time = @get("start_time")
            stop_time = @get("stop_time")
            start_date = @get("start_date")
            kids = @get("kids")
            
            #store properties for future bookings
            if not _.every([zip, start_date, start_time, stop_time, kids], _.identity)
                alert("please ensure you've filled out every field")
                return

            Sitterfied.onDeckBookingAttrs = {}
            #probably should do this as a property of the controller rather than adhoc
            start_date_time = moment(start_date)
            start_date_time.hours(start_time.substr(0,2))
            start_date_time.minutes(start_time.substr(2))
            Sitterfied.onDeckBookingAttrs['start_date_time'] = start_date_time

            Sitterfied.onDeckBookingAttrs['kids'] = kids

            stop_date_time = moment(start_date)
            stop_date_time.hours(stop_time.substr(0,2))
            stop_date_time.minutes(stop_time.substr(2))
            Sitterfied.onDeckBookingAttrs['stop_date_time'] = stop_date_time

            payload = {
                kids: kids
                zip: zip
                start_time: start_time
                stop_time: stop_time
                start_date: start_date
            }
            
            if @get("overnight")
                if not @get("stop_date")
                    alert("please ensure you've filled out every field")
                    return
                payload['overnight'] = true
                payload['stop_date'] = @get("stop_date")

                Sitterfied.onDeckBookingAttrs['overnight'] = true
                stop_date_time.date(@get("stop_date"))
                Sitterfied.onDeckBookingAttrs['stop_date_time'] = stop_date_time

            @set('searched', false)
            
            $.get("/api/search/",
                  payload,
                  ).then (response) =>
                sitters = Em.A()
                for sitter in response
                    s = Sitterfied.Sitter.create()
                    s.load(sitter['id'], sitter)
                    sitters.pushObject(s)
                this.set('model', sitters)
                @set('searched', true)

        content: []
        selectedSitters:  Ember.ArrayProxy.create
            content: Ember.A()

        sitterTeam: (() ->
            return @filterProperty('inSitterTeam', true)
        ).property('content.@each.inSitterTeam')

        hasSitterTeam: (() ->
            sitterTeam = @get("sitterTeam")
            return sitterTeam.length > 0
        ).property("sitterTeam")

        hasFriendTeam: (() ->
            friendTeam = @get("friendTeam")
            return friendTeam.length > 0
        ).property("friendTeam")

        selectTeam: () ->
            selected = @get("selectedSitters")
            for sitter in Em.copy(@get("sitterTeam"))
                if selected.filterProperty("id", sitter.get('id')).length == 0
                    selected.pushObject(sitter)

        clearTeam: () ->
            selected = @get("selectedSitters")
            for sitter in Em.copy(@get("sitterTeam"))
                matches = selected.filterProperty("id", sitter.get('id'))
                if matches.length == 1
                    selected.removeObject(matches[0])

        selectFriends: () ->
            selected = @get("selectedSitters")
            for sitter in Em.copy(@get("friendTeam"))
                if selected.filterProperty("id", sitter.get('id')).length == 0
                    selected.pushObject(sitter)

        clearFriends: () ->
            selected = @get("selectedSitters")
            for sitter in Em.copy(@get("friendTeam"))
                matches = selected.filterProperty("id", sitter.get('id'))
                if matches.length == 1
                    selected.removeObject(matches[0])


        isTeamSelected: (() ->
            selected = @get("selectedSitters")
            for sitter in @get("sitterTeam")
                if selected.filterProperty("id", sitter.get('id')).length == 0
                    return false
            return true
        ).property("selectedSitters", "selectedSitters.@each", "sitterTeam")


        isFriendsSelected: (() ->
            selected = @get("selectedSitters")
            for sitter in @get("friendTeam")
                if selected.filterProperty("id", sitter.get('id')).length == 0
                    return false
            return true
        ).property("selectedSitters", "selectedSitters.@each", "friendTeam")

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
            matches = selected.filterProperty('id', sitter.get('id'))
            if matches.length == 0
                selected.pushObject(sitter)
            else
                selected.removeObject(matches[0])

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
                emergency_phone: Sitterfied.get('currentUser.cell')
                rate: 0
            booking.get('sitters').addObjects(sitters)

            Sitterfied.set('onDeckBooking', booking)
            @transitionToRoute('book')

        open_interview_popup: (sitters) ->
            Sitterfied.set("sitters_to_interview", sitters)
            $.fancybox
                href: "#interview_popup"
                maxWidth: 390
                maxHeight: 257
                minWidth: 390
                minHeight: 257
                fitToView: false
                closeBtn: true
                enableEscapeButton: false
                width: "90%"
                height: "90%"

        interview: (interview_type) ->
            $.fancybox.close()
            
            sitters = Sitterfied.get("sitters_to_interview")
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
            
            booking_type = interview_type + " Interview"

            booking = Sitterfied.Booking.create
                parent: Sitterfied.currentUser
                notes: ""
                overnight: false
                booking_status: "Pending"
                booking_type: booking_type
                start_date_time: start_date_time
                stop_date_time: stop_date_time
                address1: Sitterfied.get('currentUser.address1')
                address2: Sitterfied.get('currentUser.address2')
                city: Sitterfied.get('currentUser.city')
                state: Sitterfied.get('currentUser.state')
                zip: Sitterfied.get('currentUser.zip')
                num_children: Sitterfied.get('currentUser.children.length')
                emergency_phone: Sitterfied.get('currentUser.cell')
                rate: 0
            booking.get('sitters').addObjects(sitters)
            Sitterfied.set('onDeckBooking', booking)
            @transitionToRoute('book')
            
        bookTeam: () ->
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
                num_children: 1
                emergency_phone: Sitterfied.get('currentUser.cell')
                rate: 0
            sitters = Sitterfied.currentUser.get('sitter_teams')
            booking.get('sitters').addObjects(sitters)
            Sitterfied.set('onDeckBooking', booking)
            @transitionToRoute('book')
    )

    Sitterfied.BookingController = Em.ObjectController.extend(
        isNoteShown: (() ->
            notes = @get('notes')
            return notes && notes.trim().length > 0
        ).property('notes')

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
        bookTeam: () ->
            booking = Sitterfied.Booking.create
                parent: Sitterfied.currentUser
                notes: ""
                overnight: false
                booking_status: "Pending"
                booking_type: "Job"
                start_date_time: null
                stop_date_time: null
                address1: Sitterfied.get('currentUser.address1')
                address2: Sitterfied.get('currentUser.address2')
                city: Sitterfied.get('currentUser.city')
                state: Sitterfied.get('currentUser.state')
                zip: Sitterfied.get('currentUser.zip')
                num_children: 1
                emergency_phone: Sitterfied.get('currentUser.cell')
                rate: 0
            sitters = @get("content")
            booking.get('sitters').addObjects(sitters)
            Sitterfied.set('onDeckBooking', booking)
            @transitionToRoute('book')
    )

    Sitterfied.ParentController  = Em.ObjectController.extend(
        addFriend: () ->
            Sitterfied.currentUser.addFriend(this.get('model'))
    )


    Sitterfied.ParentEditBookingsController  = Sitterfied.BookingsController.extend()

    Sitterfied.ParentEditReviewsController = Em.ObjectController.extend(
        activeReviewPanelUser: null
    )

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
        needs: ['sitterReview', 'friends', 'currentUser']

        postReivew: () ->
            $.fancybox.close()
            reviewController = this.get("controllers.sitterReview")
            review = reviewController.get('model')
            review.save()
            reviewController.set('model', Sitterfied.SitterReview.create(parent: Sitterfied.currentUser))
