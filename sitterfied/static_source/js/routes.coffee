define ["ember","cs!sitterfied", "cs!models", "templates", "fancybox"], (Em, Sitterfied) ->
    Sitterfied.Router.map(() ->
        this.resource('sitter', {path: '/sitter/:sitter_id/'}, () ->
            this.route('snapshot')
            this.route('details')
            this.route('reviews')
            this.route('friends')
        )
        this.resource('sitterEdit', {path: '/sitter/:sitter_id/edit'}, () ->
            this.route('profile')
            this.route('schedlue')
            this.route('network')
            this.route('reviews')
        )

        this.route('parent', {path: '/parent/:parent_id'})
        this.route('book', {path: '/book/'})
        this.route('editBook', {path: '/book/:booking_id'})

        this.resource('parentEdit', {path: '/parent/:parent_id/edit'}, () ->
            this.route('profile')
            this.route('sitterTeam')
            this.route('network')
            this.route('reviews')
        )

        this.route('search')
        this.route('profile')
        this.route('user', {path: '/user/:user_id/'})
        this.resource('mybookings', () ->
            this.route('pending')
            this.route('missed')
            this.route('canceled')
            this.route('upcoming')
            this.route('completed')
            this.route('declined')
        )

        this.route('done', {path: '/done/:booking_id/'})
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
        renderTemplate: () ->
            this.render("done")
            this.render('done.top', { outlet: 'top' })
    )

    Sitterfied.BookRoute = Em.Route.extend(
        setupController: (controller, model) ->
            controller.set('model',  Sitterfied.get('onDeckBooking'))
            controller.set('content',  Sitterfied.get('onDeckBooking'))


        redirect: () ->
            if not Sitterfied.get('onDeckBooking')?
                this.transitionTo('search')
            else
                return false

        renderTemplate: () ->
            this.render("book")
            this.render('book.top', { outlet: 'top' })
    )

    Sitterfied.EditBookRoute = Em.Route.extend(
        model: (params) ->
            Sitterfied.Booking.find(params.booking_id)

        setupController: (controller, model) ->
            controller.set('model', model)
            controller.set('content', model)

        renderTemplate: () ->
            this.render("book", {controller:'editBook'})
            this.render('book.top', { outlet: 'top', controller:'editBook' })
    )
    Sitterfied.ParentEditRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser

        renderTemplate: () ->
            this.render("parentEdit", {controller: 'currentUser'})
            this.render("parentEdit.top", {outlet: 'top', controller: 'currentUser'})
    )

    Sitterfied.ParentEditProfileRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser

        setupController: (controller, model) ->
            this.controllerFor('languages').set('model', Sitterfied.Language.findAll())
            this.controllerFor('specialneeds', Sitterfied.SpecialNeed).set('model', Sitterfied.SpecialNeed.findAll())

            children = Sitterfied.currentUser.get('children')
            this.controllerFor('children').set('model', children)
            Sitterfied.currentUserController.newChild()


        renderTemplate: () ->
            this.render("parentEdit/profile", {controller: 'currentUser'})

    )

    Sitterfied.MybookingsRoute = Em.Route.extend(
        setupController: (controller, model) ->
            this.controllerFor('bookings').set('model', Sitterfied.currentUser.get('bookings'))

        renderTemplate: () ->
            if Sitterfied.currentUserController.get('isParent')
                this.render("parentBookings", {controller: 'currentUser'})
                this.render("parentEdit.top", {outlet: 'top', controller: 'currentUser'})
            else
                this.render("sitterBookings", {controller: 'currentUser'})
                this.render("sitterEdit.top", {outlet: 'top', controller: 'currentUser'})
    )

    Sitterfied.MybookingsIndexRoute = Em.Route.extend(
        redirect: () ->
            this.transitionTo('mybookings.pending')
    )


    Sitterfied.MybookingsPendingRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("pendingBookings", {controller: 'bookings'})
        model: () ->
            Sitterfied.currentUser.get('bookings')
    )


    Sitterfied.MybookingsUpcomingRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("upcomingBookings", {controller: 'bookings'})
        model: () ->
            Sitterfied.currentUser.get('bookings')
    )
    Sitterfied.MybookingsCompletedRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("completedBookings", {controller: 'bookings'})
        model: () ->
            Sitterfied.currentUser.get('bookings')
    )
    Sitterfied.MybookingsMissedRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("missedBookings", {controller: 'bookings'})
        model: () ->
            Sitterfied.currentUser.get('bookings')
    )
    Sitterfied.MybookingsDeclinedRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("declinedBookings",{controller: 'bookings'})
        model: () ->
            Sitterfied.currentUser.get('bookings')
    )
    Sitterfied.MybookingsCanceledRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("canceledBookings", {controller: 'bookings'})
        model: () ->
            Sitterfied.currentUser.get('bookings')
    )


    Sitterfied.ParentEditSitterTeamRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser.get('sitter_teams')

        renderTemplate: () ->
            this.render("parentEdit/sitterTeam")
    )
    Sitterfied.ParentEditNetworkRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("network", {controller: 'currentUser'})

    )
    Sitterfied.ParentEditReviewsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("reviews", {controller: 'currentUser'})
    )
    Sitterfied.ParentEditIndexRoute = Em.Route.extend(
        redirect: () ->
            this.transitionTo('parentEdit.profile')

    )
    Sitterfied.ParentRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("parent")
            this.render("parent.top", {outlet: 'top'})
    )

    Sitterfied.SitterRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitter")
            this.render("sitter.top", {outlet: 'top'})
    )

    Sitterfied.SitterIndexRoute = Em.Route.extend(
        redirect: () ->
            this.transitionTo('sitter.snapshot')
    )


    Sitterfied.SitterSnapshotRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitter.snapshot", {controller: 'sitter'})
    )
    Sitterfied.SitterDetailsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitter.details", {controller: 'sitter'})
    )

    Sitterfied.SitterReviewsRoute = Em.Route.extend(

        renderTemplate: () ->
            this.render("sitter.reviews", {controller: 'sitter'})
    )

    Sitterfied.SitterFriendsRoute = Em.Route.extend(

        renderTemplate: () ->
            this.render("sitter.friends", {controller: 'sitter'})
    )



    Sitterfied.SitterEditRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser

        renderTemplate: () ->
            this.render("sitterEdit", {controller: 'currentUser'})
            this.render("sitterEdit.top", {outlet: 'top'})
    )

    Sitterfied.SitterEditIndexRoute = Em.Route.extend(
        redirect: () ->
            this.transitionTo('sitterEdit.profile')

    )

    Sitterfied.SitterEditProfileRoute = Em.Route.extend(
        setupController: (controller, model) ->
            this.controllerFor('languages').set('model', Sitterfied.Language.findAll())
            this.controllerFor('certifications').set('model', Sitterfied.Certification.findAll())
            this.controllerFor('otherServices').set('model', Sitterfied.OtherService.findAll())

        renderTemplate: () ->
            this.render("sitterEdit/profile", {controller: 'currentUser'})
    )
    Sitterfied.SitterEditSchedlueRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser.get('schedlue')

        setupController: (controller, model) ->
            controller.set('model', model);

        renderTemplate: () ->
            this.render("sitterEdit/schedlue")
    )
    Sitterfied.SitterEditBookingsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("bookings", {controller: 'sitterEditBookings'})
        model: () ->
            Sitterfied.currentUser.get('bookings')
    )
    Sitterfied.SitterEditNetworkRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("network", {controller: 'currentUser'})
    )
    Sitterfied.SitterEditReviewsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("reviews", {controller: 'currentUser'})
    )




    Sitterfied.SettingsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("settings", {controller: 'currentUser'})
            this.render("settings.top", {outlet: 'top'})
    )

    Sitterfied.ProfileRoute = Em.Route.extend(
        redirect: () ->
            if Sitterfied.get('isParent')
                this.transitionTo('parentEdit', Sitterfied.currentUser)
            else
                this.transitionTo('sitterEdit', Sitterfied.currentUser)
    )


    Sitterfied.UserRoute = Em.Route.extend(
        redirect: (user) ->
            if user.get('isParent')
                this.transitionTo('parent', user)
            else
                this.transitionTo('sitter', user)
    )
    Sitterfied.TosRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('tos')
    )
    Sitterfied.PrivacyRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('privacy')
    )


    Sitterfied.IndexRoute = Em.Route.extend(
        redirect: (user) ->
            if Sitterfied.currentUser.get('isParent')
                this.transitionTo('search')
            else
                this.transitionTo('profile')


        renderTemplate: () ->
            this.render('footer', {outlet: 'footer'})
    )


    Sitterfied.SearchRoute = Em.Route.extend(
        help_target:  "#onboarding_final"

        setupController: (controller, model) ->
            this.controllerFor('languages').set('model', Sitterfied.Language.find())
            this.controllerFor('certifications').set('model', Sitterfied.Certification.find())
            this.controllerFor('otherServices').set('model', Sitterfied.OtherService.find())

        renderTemplate: () ->
            this.render('search.top', {outlet: 'top'})
            this.render('search')
    )
    Sitterfied.ApplicationRoute = Em.Route.extend(

        postReview: () ->
            alert("base")

        events:{
            openReccomendPopup: ()->
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

            editBooking: (booking)  ->
                this.transitionTo('editBook', booking)

            addFriend: (user) ->
                alert("add friend")

            addSitterTeam: (sitter) ->
                Em.run.begin()
                sitterTeam = Sitterfied.currentUser.get('sitter_teams')
                dupSitter = sitterTeam.findProperty('id', sitter.get('id'))
                if dupSitter
                    sitterTeam.removeObject(dupSitter)
                    dupSitter.get('sitter_teams').removeObject(Sitterfied.currentUser)
                else
                    sitterTeam.pushObject(sitter)
                    sitter.get('sitter_teams').pushObject(Sitterfied.currentUser)

                Sitterfied.currentUser.set('isDirty', true)
                Sitterfied.currentUser.save()
                Em.run.end()

            bookmark: (sitter) ->
                bookmarks = Sitterfied.currentUser.get('bookmarks')

                if bookmarks.findProperty('id', sitter.get('id'))
                    sitter = bookmarks.findProperty('id', sitter.get('id'))
                    bookmarks.removeObject(sitter)
                    sitter.get('bookmarks').removeObject(Sitterfied.currentUser)
                else
                    bookmarks.pushObject(sitter)
                    sitter.get('bookmarks').pushObject(Sitterfied.currentUser)

                Sitterfied.currentUser.set('isDirty', true)
                Sitterfied.currentUser.save()


            closeReccomendPopup: ()->
                $.fancybox.close()

            gmailConnect: () ->
                alert('gmail connect')


        }

        setupController: (controller, model) ->
            #load the model once more to get fks set
            user = Sitterfied.currentUser
            #preload the settings
            user.get("settings")
    )
