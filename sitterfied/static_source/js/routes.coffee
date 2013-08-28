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
        this.route('user', {path: '/user/:user_id/'})
        this.route('mybookings')
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
            this.render("done", {outlet: 'content'})
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
            this.render("book", {outlet: 'content'})
            this.render('book.top', { outlet: 'top' })
    )

    Sitterfied.EditBookRoute = Em.Route.extend(
        model: (params) ->
            Sitterfied.Booking.find(params.booking_id)

        setupController: (controller, model) ->
            controller.set('model', model)
            controller.set('content', model)

        renderTemplate: () ->
            this.render("book", {outlet: 'content', controller:'editBook'})
            this.render('book.top', { outlet: 'top', controller:'editBook' })
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
            this.controllerFor('languages').set('model', Sitterfied.Language.findAll())
            this.controllerFor('specialneeds', Sitterfied.SpecialNeed).set('model', Sitterfied.SpecialNeed.findAll())

            children = Sitterfied.currentUser.get('children')
            this.controllerFor('children').set('model', children)

        renderTemplate: () ->
            this.render("parentEdit/profile", {into:"parentEdit", controller: 'currentUser'})
    )
    Sitterfied.ParentEditBookingsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("bookings", {into:"parentEdit", controller: 'parentEditBookings'})
        model: () ->
            Sitterfied.currentUser.get('bookings')

    )
    Sitterfied.ParentEditSitterTeamRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser.get('sitter_teams')

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

    Sitterfied.SitterRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitter", {outlet: 'content'})
            this.render("sitter.top", {outlet: 'top'})


    )

    Sitterfied.SitterIndexRoute = Em.Route.extend(
        redirect: () ->
            this.transitionTo('sitter.snapshot')
    )


    Sitterfied.SitterSnapshotRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitter.snapshot", {into:"sitter", controller: 'sitter'})
    )
    Sitterfied.SitterDetailsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitter.details", {into:"sitter", controller: 'sitter'})
    )

    Sitterfied.SitterReviewsRoute = Em.Route.extend(

        renderTemplate: () ->
            this.render("sitter.reviews", {into:"sitter", controller: 'sitter'})
    )

    Sitterfied.SitterFriendsRoute = Em.Route.extend(

        renderTemplate: () ->
            this.render("sitter.friends", {into:"sitter", controller: 'sitter'})
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
            this.controllerFor('languages').set('model', Sitterfied.Language.findAll())
            this.controllerFor('certifications').set('model', Sitterfied.Certification.findAll())
            this.controllerFor('otherServices').set('model', Sitterfied.OtherService.findAll())

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


    Sitterfied.UserRoute = Em.Route.extend(
        redirect: (user) ->
            if user.get('isParent')
                this.transitionTo('parent', user)
            else
                this.transitionTo('sitter', user)
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
        setupController: (controller, model) ->
            this.controllerFor('languages').set('model', Sitterfied.Language.find())
            this.controllerFor('certifications').set('model', Sitterfied.Certification.find())
            this.controllerFor('otherServices').set('model', Sitterfied.OtherService.find())

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

            editBooking: (booking)  ->
                this.transitionTo('editBook', booking)

            addFriend: (user) ->
                alert("add friend")

            addSitterTeam: (sitter) ->
                Em.run.begin()
                sitterTeam = Sitterfied.currentUser.get('sitter_teams')
                if sitterTeam.findProperty('id', sitter.get('id'))
                    sitter = sitterTeam.findProperty('id', sitter.get('id'))
                    sitterTeam.removeObject(sitter)
                    sitter.get('sitter_teams').removeObject(Sitterfied.currentUser)
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
    )
