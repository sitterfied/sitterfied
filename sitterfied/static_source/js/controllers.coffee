define ["ember", "cs!sitterfied", "cs!models"], (Em, Sitterfied) ->



    Sitterfied.CurrentUserController = Em.ObjectController.extend({
        needs: ['certifications']
        accountType: parent_or_sitter
        isSitter: (() ->
            Sitterfied.accountType == "Sitter"
        ).property('parent_or_sitter')
        isParent: (() ->
            Sitterfied.accountType == "Parent"
        ).property('parent_or_sitter')
        saveSettings: () ->
            settings =  this.get('settings')
            if settings.get('isDirty')
                settings.save()
            if this.get('model.isDirty')
                this.get('model').save()

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
