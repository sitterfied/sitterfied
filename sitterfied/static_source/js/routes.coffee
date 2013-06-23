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



    Sitterfied.ParentEditIndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("parentEdit/index", {outlet: 'topInfo'})
    )

    Sitterfied.ParentRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'topInfo'})
    )

    Sitterfied.SettingsRoute = Em.Route.extend(
        redirect: () ->
            this.transitionTo('parentEdit');

    )


    Sitterfied.editRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'topInfo'})
    )

    Sitterfied.IndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('footer', {outlet: 'footer'})
        )

    Sitterfied.ApplicationRoute = Em.Route.extend(
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
                    outlet: 'topInfo',              # the name of the outlet in that template
                })
                this.render('noSearchResults', {     # the template to render
                    outlet: 'container',              # the name of the outlet in that template
                })
            else
                this.render('searchResultsTop', {     # the template to render
                    outlet: 'topInfo',              # the name of the outlet in that template
                })
    )
