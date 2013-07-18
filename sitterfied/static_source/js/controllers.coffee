define ["ember", "cs!sitterfied", "cs!models"], (Em, Sitterfied) ->



    Sitterfied.CurrentUserController = Em.ObjectController.extend({
        needs: ['certifications', 'languages', 'otherServices', 'friends', 'children']
        accountType: parent_or_sitter
        isSitter: (() ->
            Sitterfied.accountType == "Sitter"
        ).property('parent_or_sitter')
        isParent: (() ->
            Sitterfied.accountType == "Parent"
        ).property('parent_or_sitter')

        saveSettings: () ->
            model = this.get('model')
            #force a save
            model.get('stateManager').goToState('updated')
            settings =  this.get('settings')
            transaction = model.get('transaction')
            transaction.add(settings)
            transaction.commit()

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
            newChild = Sitterfied.Child.createRecord(parent: this.get('content'))
            this.get('controllers.children').pushObject(newChild)


        saveCertification: () ->

            newCert = this.get('controllers.certifications.newCert')
            if newCert == ''
                return
            certification = Sitterfied.Certification.createRecord({certification:newCert})
            certification.get('transaction').commit()
            this.set('controllers.certifications.newCert', '')

        saveService: () ->

            newService = this.get('controllers.otherServices.newService')
            if newService == ''
                return
            service = Sitterfied.OtherService.createRecord({service:newService})
            service.get('transaction').commit();
            this.set('controllers.otherServices.newService', '')

        saveLanguage: () ->
            newLanguage = this.get('controllers.languages.newLanguage')
            if newLanguage == ''
                return
            language = Sitterfied.Language.createRecord({language:newLanguage})
            language.get('transaction').commit();
            this.set('controllers.languages.newLanguage', '')

        addChild: () ->
            Sitterfied.Child.createRecord({parent:Sitterfied.currentUser})




        facebookConnect: ()->
                console.log("get fb data")
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
                                alert("facebook friends imported")
                                Sitterfied.currentUser.reload()
                    )

                FB.getLoginStatus (response) ->
                  if response.status is "connected"
                    use_fb_data()
                  else if response.status is "not_authorized"
                    FB.login ->
                        use_fb_data()

    })

    Sitterfied.BookController = Em.ArrayController.extend(
        cancel: () ->
            alert('cancel')
            this.transitionTo('search');
        book: () ->
            alert('send')
            this.transitionTo('done');
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

    Sitterfied.DoneController = Em.ArrayController.extend(
        cancel: () ->
            alert('cancel')
            this.transitionTo('search');
        edit: () ->
            alert('edit')
            this.transitionTo('book');
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
    Sitterfied.OtherServicesController  = Em.ArrayController.extend(
        newService: ''
    )

    Sitterfied.LanguagesController  = Em.ArrayController.extend(
        newLanguage: ''
    )
    Sitterfied.SitterReviewController  = Em.ObjectController.extend(
    )
    Sitterfied.ChildrenController  = Em.ArrayController.extend(
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
