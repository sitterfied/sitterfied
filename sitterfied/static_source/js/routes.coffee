define ["cs!sitterfied", "cs!models", "templates"], (Sitterfied) ->
    Sitterfied.Router.map(() ->
        this.route('sitter')
        this.resource('parents', {path: '/parent/:parent_id'})
        this.route('search')
        this.route('parentBook')
        this.route('parentBookMultiple')
        this.route('done')
        this.route('about')
    )

    Sitterfied.ParentsRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render({outlet: 'topInfo'})
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
