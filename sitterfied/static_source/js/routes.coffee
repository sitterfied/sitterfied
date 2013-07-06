define ["ember","cs!sitterfied", "cs!models", "templates"], (Em, Sitterfied) ->
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

        this.resource('parentEdit', {path: '/parent/:parent_id/edit'}, () ->
            this.route('profile')
            this.route('bookings')
            this.route('sitterTeam')
            this.route('network')
            this.route('reviews')
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
            this.render('done.top', { outlet: 'top' })

    )

    Sitterfied.BookRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("book.multiple", {outlet: 'content'})
            this.render('book.top', { outlet: 'top' })

    )


    Sitterfied.ParentEditRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("parentEdit", {outlet: 'content'})
            this.render("parentEdit.top", {outlet: 'top'})
    )

    Sitterfied.ParentRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("parent", {outlet: 'content'})
            this.render("parent.top", {outlet: 'top'})

    )


    Sitterfied.SitterEditRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitterEdit", {outlet: 'content'})
            this.render("sitterEdit.top", {outlet: 'top'})
    )


    Sitterfied.SitterRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render("sitter", {outlet: 'content'})
            this.render("sitter.top", {outlet: 'top'})
    )

    Sitterfied.SettingsRoute = Em.Route.extend(
        model: () ->
            Sitterfied.currentUser

        renderTemplate: () ->
            this.render("settings", {outlet: 'content'})
            this.render("settings.top", {outlet: 'top'})
    )

    Sitterfied.ProfileRoute = Em.Route.extend(
        redirect: () ->
            if Sitterfied.get('isParent')
                this.transitionTo('parentEdit', Sitterfied.currentUser)
            else
                this.transitionTo('sitterEdit', Sitterfied.currentUser)
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
            model = Sitterfied.get('accountType')
            ref = store.load(model, user_data)
            Sitterfied.currentUser = Sitterfied[model].find(ref.id)
    )


    Sitterfied.SearchRoute = Em.Route.extend(
        renderTemplate: () ->
            this.render('search.top', {outlet: 'top'})
            this.render('emptysearch', {outlet: 'content'})
            #this.render('search', { outlet: 'content'})
    )
