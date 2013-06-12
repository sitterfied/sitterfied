define ["cs!sitterfied", "cs!models", "templates"], (Sitterfied) ->
    Sitterfied.Router.map(() ->
        this.resource('sitter', {path: '/parent/:parent_id'}, () ->
            this.resource('edit', () ->
                this.route('profile')
                this.route('schedlue')
                this.route('bookings')
                this.route('network')
                this.route('reviews')
            )
        )
        this.resource('parent', {path: '/parent/:parent_id'}, () ->
            this.resource('edit', () ->
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
    )



    Sitterfied.EditIndexParentRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'topInfo'})

    )
    Sitterfied.EditParentIndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'topInfo'})
    )
    Sitterfied.ParentEditIndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("parent/edit/index", {outlet: 'topInfo'})
    )

    Sitterfied.EditIndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'topInfo'})
    )


    Sitterfied.ParentRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'topInfo'})
    )

    Sitterfied.editRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'topInfo'})
    )


    Sitterfied.IndexRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('index', {outlet: 'topInfo'})
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
