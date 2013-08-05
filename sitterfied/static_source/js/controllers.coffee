define ["ember", "cs!sitterfied", 'moment', "cs!models"], (Em, Sitterfied) ->



    Sitterfied.CurrentUserController = Em.ObjectController.extend({
        #I know childs is a bad name, but data has issues with a custom name
        needs: ['certifications'
                'languages'
                'specialneeds'
                'otherServices'
                'friends'
                'childs']
        accountType: parent_or_sitter

        isSitter: (() ->
            Sitterfied.accountType == "Sitter"
        ).property('parent_or_sitter')

        isParent: (() ->
            Sitterfied.accountType == "Parent"
        ).property('parent_or_sitter')

        saveSettings: () ->
            this.get('controllers.childs').map (child)->
                child.save()

            model = this.get('model')

            #force a save since we might have m2m associations
            model.get('stateManager').goToState('updated')
            model.save()
            settings =  this.get('settings')
            settings.save()



        deleteAccount: () ->
            alert('delete')
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

        newFriendName:  ""
        addFriend: () ->
            newFriendName = @get('newFriendName')
            alert('add Friend, ' + newFriendName)

        invite: () ->
            alert("invite friends")

        deleteGroup: (group) ->
            alert("delete group, " + group)

        newChild: () ->

            newChild = Sitterfied.Child.createRecord(
                parent: this.get('content')
                name:""
                school: ""
                dob: new Date
            )
            #this.get('controllers.childs').pushObject(newChild)


        saveCertification: () ->

            newCert = this.get('controllers.certifications.newCert')
            if newCert == ''
                return
            transaction = this.get("store").transaction();
            certification = transaction.createRecord(Sitterfied.Certification,{certification:newCert})
            transaction.commit()
            this.set('controllers.certifications.newCert', '')

        saveService: () ->

            newService = this.get('controllers.otherServices.newService')
            if newService == ''
                return
            transaction = this.get("store").transaction();
            service = transaction.createRecord(Sitterfied.OtherService,{service:newService})
            transaction.commit()
            this.set('controllers.otherServices.newService', '')

        saveLanguage: () ->
            newLanguage = this.get('controllers.languages.newLanguage')
            if newLanguage == ''
                return
            transaction = this.get("store").transaction();
            language = transaction.createRecord(Sitterfied.Language,{language:newLanguage})
            transaction.commit()
            this.set('controllers.languages.newLanguage', '')


        saveNeed: () ->
            newNeed = this.get('controllers.specialneeds.newNeed')
            if newNeed == ''
                return
            transaction = this.get("store").transaction();
            need = transaction.createRecord(Sitterfied.SpecialNeed,{need:newNeed})
            transaction.commit()
            this.set('controllers.specialneeds.newNeed', '')


        facebookConnect: ()->
                use_fb_data = () ->
                    access_token = FB.getAccessToken()
                    facebook_id = FB.getUserID()
                    Sitterfied.currentUser.set('facebook_token', access_token)
                    Sitterfied.currentUser.set('facebook_id', facebook_id)
                    Sitterfied.currentUser.save()
                    Sitterfied.currentUser.one('didUpdate', () ->
                        $.ajax
                            url: "/facebook_import/"
                            success: () ->
                                alert("facebook connected")
                    )

                FB.getLoginStatus (response) ->
                  if response.status is "connected"
                    use_fb_data()
                  else if response.status is "not_authorized"
                    FB.login ->
                        use_fb_data()

    })

    Sitterfied.BookController = Em.ObjectController.extend(
        cancel: () ->
            this.get('content.transaction').rollback()
            this.transitionTo('search');
        book: () ->
            this.get('content.transaction').commit()
            this.transitionTo('done');

        multiple: (() ->
            return false
        ).property()
    )

    Sitterfied.SitterEditSchedlueController =  Em.ObjectController.extend({
        saveSchedlue: () ->
            @get('model').save()
        checkAll: () ->
            model = @get('model')
            attrs = Object.keys(model.serialize())
            attrs.pop('sitter')
            for x in attrs
                @set(x, true)
        clearAll: () ->
            model = @get('model')
            attrs = Object.keys(model.serialize())
            attrs.pop('sitter')
            for x in attrs
                @set(x, false)

    })

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
    Sitterfied.SitterReviewController  = Em.ObjectController.extend(
    )
    Sitterfied.ChildsController  = Em.ArrayController.extend(
    )
    Sitterfied.SearchController  = Em.ArrayController.extend(
        zip : ""
        when: undefined
        from : 2
        to : 5
        kids : 1
        overnight : false
        date_to : undefined
        findSitters : () ->
            $.ajax("/api/search/").then (response) =>
                store =  DS.get('defaultStore')
                ids = _.pluck(response, 'id')
                sitter_refs = store.loadMany(Sitterfied.Sitter, ids, response)
                sitters = (store.materializeRecord(sitter_ref) for sitter_ref in sitter_refs)
                this.set('content', sitters)

        content: []

        sitterTeam: (() ->
            return @get('content').filterProperty("in_sitter_team", true)
        ).property('content.@each')
        friendTeam: (() ->
            return @get('content').filterProperty("in_friends_team", true)
        ).property('content.@each')
        localTeam: (() ->
            return @get('content').filterProperty("in_friends_team", false).filterProperty('in_sitter_team', false)
        ).property('content.@each')
        zoomToLocalTeam: () ->
            $.scrollTo("#localteam", 500)
        zoomToFriendTeam: () ->
            $.scrollTo("#friendteam", 500)
        zoomToSitterTeam: () ->
            $.scrollTo("#sitterteam", 500)


        book: (sitters) ->
            if not Sitterfied.typeIsArray sitters
                sitters = [sitters]

            if @get('overnight')
                stop_date_time = moment(@get('date_to')).toDate()
            else
                stop_date_time = moment(@get('when')).toDate()


            store = this.get('store')
            transaction = store.transaction()
            booking = Sitterfied.Booking.createRecord
                parent: Sitterfied.currentUser
                notes: ""
                overnight: false
                booking_status: "Pending"
                booking_type: "Job"
                start_date_time: moment(@get('when')).toDate()
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
            transaction.add(booking)

            Sitterfied.set('onDeckBooking', booking)
            this.transitionTo('book')

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
            reviewController.set('model', Sitterfied.SitterReview.createRecord(parent: Sitterfied.currentUser))
