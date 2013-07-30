define ["ember","cs!sitterfied", "cs!models", "templates", "fancybox"], (Em, Sitterfied) ->
    Sitterfied.Router.map(() ->
        this.resource('sitter', {path: '/sitter/:sitter_id'})
        this.resource('sitterEdit', {path: '/sitter/:sitter_id/edit'}, () ->
            this.route('profile')
            this.route('schedlue')
            this.route('bookings')
            this.route('network')
            this.route('reviews')
            )

        this.route('parent', {path: '/parent/:parent_id'})
        this.route('book', {path: '/book/'})
        this.route('editBook', {path: '/book/:booking_id'})

        this.resource('parentEdit', {path: '/parent/:parent_id/edit'}, () ->
            this.route('profile')
            this.route('bookings')
            this.route('sitterTeam')
            this.route('network')
            this.route('reviews')
        )

        this.route('search')
        this.route('profile')
        this.route('mybookings')
        this.route('done')
        this.route('about')
        this.route('tos')
        this.route('privacy')

        #redirects
        this.route('settings')
        this.route('find friends')
        this.route('rusitterfied')
        this.route('support')
        this.route('sign out')
    )


    Sitterfied.DoneRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.get('onDeckBooking')

        renderTemplate: () ->
            this.render("done", {outlet: 'content'})
            this.render('done.top', { outlet: 'top' })
    )

    Sitterfied.BookRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.get('onDeckBooking')

        redirect: () ->
            if not this.model()
                this.transitionTo('search')
            else
                return false

        renderTemplate: () ->
            this.render("book", {outlet: 'content'})
            this.render('book.top', { outlet: 'top' })
    )

    Sitterfied.EditBookRoute = Em.Route.extend(
        model: (params) ->
            Sitterfied.Booking.find(params.booking_id)

        setupController: (controller, model) ->
            Sitterfied.set('onDeckBooking', model) #for the done screen
            this.controllerFor('book').set('model', model)

        renderTemplate: () ->
            this.render("book", {outlet: 'content', controller:'book'})
            this.render('book.top', { outlet: 'top', controller:'book' })
    )
    Sitterfied.ParentEditRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser

        renderTemplate: () ->
            this.render("parentEdit", {outlet: 'content', controller: 'currentUser'})
            this.render("parentEdit.top", {outlet: 'top', controller: 'currentUser'})
    )

    Sitterfied.ParentEditProfileRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser

        setupController: (controller, model) ->
            this.controllerFor('languages').set('model', Sitterfied.Language.find())
            this.controllerFor('specialneeds', Sitterfied.SpecialNeed).set('model', Sitterfied.SpecialNeed.find())

            children = Sitterfied.Child.find({parent:Sitterfied.currentUser.id})
            this.controllerFor('childs').set('model', children)

        renderTemplate: () ->
            this.render("parentEdit/profile", {into:"parentEdit", controller: 'currentUser'})
    )
    Sitterfied.ParentEditBookingsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("bookings", {into:"parentEdit", controller: 'currentUser'})
    )
    Sitterfied.ParentEditSitterTeamRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser

        renderTemplate: () ->
            this.render("parentEdit/sitterTeam", {into:"parentEdit"})
    )
    Sitterfied.ParentEditNetworkRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("network", {into:"parentEdit", controller: 'currentUser'})
    )
    Sitterfied.ParentEditReviewsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("reviews", {into:"parentEdit", controller: 'currentUser'})
    )
    Sitterfied.ParentEditIndexRoute = Em.Route.extend(
        redirect: () ->
            this.transitionTo('parentEdit.profile')

    )
    Sitterfied.ParentRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("parent", {outlet: 'content'})
            this.render("parent.top", {outlet: 'top'})
    )

    Sitterfied.SitterEditRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser

        renderTemplate: () ->
            this.render("sitterEdit", {outlet: 'content', controller: 'currentUser'})
            this.render("sitterEdit.top", {outlet: 'top'})
    )
    Sitterfied.SitterEditIndexRoute = Em.Route.extend(
        redirect: () ->
            this.transitionTo('sitterEdit.profile')

    )
    Sitterfied.SitterEditProfileRoute = Em.Route.extend(
        setupController: (controller, model) ->
            this.controllerFor('languages').set('model', Sitterfied.Language.find())
            this.controllerFor('certifications').set('model', Sitterfied.Certification.find())
            this.controllerFor('otherServices').set('model', Sitterfied.OtherService.find())

        renderTemplate: () ->
            this.render("sitterEdit/profile", {into:"sitterEdit", controller: 'currentUser'})
    )
    Sitterfied.SitterEditSchedlueRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser.get('schedlue')

        setupController: (controller, model) ->
            controller.set('model', model);

        renderTemplate: () ->
            this.render("sitterEdit/schedlue", {into:"sitterEdit"})
    )
    Sitterfied.SitterEditBookingsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("bookings", {into:"sitterEdit", controller: 'currentUser'})
    )
    Sitterfied.SitterEditNetworkRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("network", {into:"sitterEdit", controller: 'currentUser'})
    )
    Sitterfied.SitterEditReviewsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("reviews", {into:"sitterEdit", controller: 'currentUser'})
    )



    Sitterfied.SitterRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitter", {outlet: 'content'})
            this.render("sitter.top", {outlet: 'top'})
    )

    Sitterfied.SettingsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("settings", {outlet: 'content', controller: 'currentUser'})
            this.render("settings.top", {outlet: 'top'})
    )

    Sitterfied.ProfileRoute = Em.Route.extend(
        redirect: () ->
            if Sitterfied.get('isParent')
                this.transitionTo('parentEdit', Sitterfied.currentUser)
            else
                this.transitionTo('sitterEdit', Sitterfied.currentUser)
    )
    Sitterfied.MybookingsRoute = Em.Route.extend(
        redirect: () ->
            if Sitterfied.get('isParent')
                this.transitionTo('parentEdit.bookings', Sitterfied.currentUser)
            else
                this.transitionTo('sitterEdit.bookings', Sitterfied.currentUser)
    )


    Sitterfied.IndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('footer', {outlet: 'footer'})
    )

    Sitterfied.SearchRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('search.top', {outlet: 'top'})
            this.render('search', { outlet: 'content'})
    )
    Sitterfied.ApplicationRoute = Em.Route.extend(

        postReview: () ->
            alert("base")

        events:{
            openReccomendPopup: ()->
                console.log("")
                $.fancybox
                    href: "#recommend_popup"
                    maxWidth: 960
                    maxHeight: 800
                    minWidth: 700
                    minHeight: 480
                    fitToView: false
                    width: "90%"
                    height: "90%"

            removeFromTeam: ()->
                debugger

            closeReccomendPopup: ()->
                $.fancybox.close()

            gmailConnect: () ->
                alert('gmail connect')


            previewAvatar: () ->
                $("#avatar_field").click()

            uploadAvatar: () ->
                $.ajax
                    type: "POST"
                    url:"/api/users/" + Sitterfied.currentUser.id + "/avatar_upload/"
                    dataType: 'json'
                    data: {
                        avatar: Sitterfied.get('onDeckAvatar')
                    }
                    success: (response) ->
                        Sitterfied.currentUser.set('avatar', response.avatar)
                        $.fancybox.close()
                    error: () ->
                        alert("There was a problem uploading your avatar. Please try again")


            openPhotoPopup: ->
                $.fancybox
                    href:"#edit_photo_popup"
                    maxWidth    : 960
                    maxHeight   : 800
                    minWidth    : 600
                    minHeight   : 580
                    fitToView   : false
                    width       : '90%'
                    height      : '90%'
        }


        setupController: (controller, model) ->
            if Sitterfied.isParent
                reivew = Sitterfied.SitterReview.createRecord(parent: Sitterfied.currentUser)
            else
                review = Sitterfied.SitterReview.createRecord()

            #load the model once more to get fks set
            Sitterfied[parent_or_sitter].find({id:Sitterfied.currentUser.id})

            this.controllerFor('sitterReview').set('model', review)

            friends = Sitterfied.User.find({friends:Sitterfied.currentUser.id})
            this.controllerFor('friends').set('model', friends)




    )
