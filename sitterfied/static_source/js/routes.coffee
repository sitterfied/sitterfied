define ["cs!sitterfied", "cs!models", "templates"], (Sitterfied) ->
    Sitterfied.Router.map(() ->
        this.resource('sitter', {path: '/sitter/:sitter_id'}, () ->
            this.resource('sitterEdit', () ->
                this.route('profile')
                this.route('schedlue')
                this.route('bookings')
                this.route('network')
                this.route('reviews')
            )
        )
        this.resource('parent', {path: '/parent/:parent_id'}, () ->
            this.resource('parentEdit', {path: '/edit'}, () ->
                this.route('profile')
                this.route('bookings')
                this.route('sitterTeam')
                this.route('network')
                this.route('reviews')
            )
        )
        this.route('search')
        this.route('profile')
        this.route('book')
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
        renderTemplate: () ->
            this.render("done", {outlet: 'content'})
            this.render('done.topNotify', { outlet: 'top' })

    )


    Sitterfied.ParentEditIndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("parentEdit/index", {outlet: 'top'})
    )

    Sitterfied.ParentRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'top'})
    )

    Sitterfied.SitterRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('sitter.topInfo', {     # the template to render
                outlet: 'top',              # the name of the outlet in that template
            })
            this.render('sitter.container', {     # the template to render
                    outlet: 'content',              # the name of the outlet in that template
                })



    )

    Sitterfied.SettingsRoute = Em.Route.extend(
        model: () ->
            Sitterfied.currentUser

        renderTemplate: () ->
            this.render('settings.top', {     # the template to render
                outlet: 'top',              # the name of the outlet in that template
            })

            if parent_or_sitter == "Parent"
                this.render('settings.parentContent', {     # the template to render
                    outlet: 'content',              # the name of the outlet in that template
                })

    )

    Sitterfied.profileRoute = Em.Route.extend(
        redirect: () ->
            if parent_or_sitter == "Parent"
                this.transitionTo('parentEdit', Sitterfied.currentUser)
            else if parent_or_sitter == "Sitter"
                this.transitionTo('sitterEdit', Sitterfied.currentUser)
    )



    Sitterfied.editRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'top'})
    )

    Sitterfied.IndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('footer', {outlet: 'footer'})
        )

    Sitterfied.ApplicationRoute = Em.Route.extend(
        ## load currentUser
        activate: () ->
            store = this.get("store")
            user_data = JSON.parse(user_json)
            model = Sitterfied.get(parent_or_sitter)
            ref = store.load(model, user_data)
            Sitterfied.currentUser = model.find(ref.id)
    )



    Sitterfied.SearchRoute = Em.Route.extend(
        renderTemplate: () ->
            noResults = true
            if noResults
                this.render('noSearchResultsTop', {     # the template to render
                    outlet: 'top',              # the name of the outlet in that template
                })
                this.render('noSearchResults', {     # the template to render
                    outlet: 'content',              # the name of the outlet in that template
                })
            else
                this.render('searchResultsTop', {     # the template to render
                    outlet: 'top',              # the name of the outlet in that template
                })
    )
