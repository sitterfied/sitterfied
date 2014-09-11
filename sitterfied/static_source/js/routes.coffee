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
            this.route('schedule')
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
        events:{
            addFriend: (user) ->
                Em.run.begin()
                Sitterfied.currentUser.addFriend(user)
                this.get("controller").set("isFriend", true)
                
                # Add to sitter team if user is sitter
                if user.get('isSitter') and Sitterfied.currentUser.get('isParent')
                    sitterTeam = Sitterfied.currentUser.get('sitter_teams')
                    dupSitter = sitterTeam.findProperty('id', user.get('id'))
                    if dupSitter
                        console.log("Dupsitter add:", dupSitter)
                    else
                        console.log("No Dupsitter add:", user)
                        sitterTeam.pushObject(user)
                        user.get('sitter_teams').pushObject(Sitterfied.currentUser)
                        # Reflect changes to controller
                        this.get("controller").addSitterInCache(Sitterfied.currentUser)
    
                Sitterfied.currentUser.set('isDirty', true)
                Sitterfied.currentUser.save()
                Em.run.end()
            
            removeFriend: (user) ->
                Em.run.begin()
                Sitterfied.currentUser.removeFriend(user)
                this.get("controller").set("isFriend", false)
                
                # Remove from team
                if user.get('isSitter') and Sitterfied.currentUser.get('isParent')
                    sitterTeam = Sitterfied.currentUser.get('sitter_teams')
                    dupSitter = sitterTeam.findProperty('id', user.get('id'))
                    sitterTeam.removeObject(user)
                    if dupSitter
                        sitterTeam.removeObject(dupSitter)
                        dupSitter.get('sitter_teams').removeObject(Sitterfied.currentUser)
                        # Reflect changes to controller
                        this.get("controller").removeSitterInCache('id', Sitterfied.currentUser.get('id'))
                
                Sitterfied.currentUser.set('isDirty', true)
                Sitterfied.currentUser.save()
                Em.run.end()
                
            addSitterTeam: (sitter) ->
                # Copied from application route but with changes to get data
                # from SitterController.
                Em.run.begin()
                sitterTeam = Sitterfied.currentUser.get('sitter_teams')
                dupSitter = sitterTeam.findProperty('id', sitter.get('id'))
                if dupSitter
                    sitterTeam.removeObject(dupSitter)
                    dupSitter.get('sitter_teams').removeObject(Sitterfied.currentUser)
                    # Reflect changes to controller
                    this.get("controller").removeSitterInCache('id', Sitterfied.currentUser.get('id'))
                    this.get("controller").set("isFriend", false)
                    # Remove to network
                    Sitterfied.currentUser.removeFriend(dupSitter)
                else
                    sitterTeam.pushObject(sitter)
                    sitter.get('sitter_teams').pushObject(Sitterfied.currentUser)
                    # Reflect changes to controller
                    this.get("controller").addSitterInCache(Sitterfied.currentUser)
                    this.get("controller").set("isFriend", true)
                    Sitterfied.currentUser.addFriend(sitter)

                Sitterfied.currentUser.set('isDirty', true)
                Sitterfied.currentUser.save()
                Em.run.end()
        }
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
    Sitterfied.SitterEditScheduleRoute = Em.Route.extend(
        model: () ->
            return Sitterfied.currentUser.get('schedule')

        setupController: (controller, model) ->
            controller.set('model', model);

        renderTemplate: () ->
            this.render("sitterEdit/schedule")
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
            
            if not Sitterfied.currentUser.get("paypal_email")
                # Setup paypal button
                $.ajax(
                    url: "/api/braintree_client/"
                    method: "post"
                ).done (data) ->
                    braintree.setup(data.client_token, "paypal", {
                        container: "paypal-container"
                        paymentMethodNonceInputField: "paypal-payment-method-nonce"
                        singleUse: false
                        onSuccess: ->
                            paypal_method_nonce = $("#paypal-payment-method-nonce").val()
                            $("#paypal-container").html("")
                            $.ajax(
                                url: "/api/update_payment_method/"
                                method: "post"
                                data:
                                    payment_method: "paypal"
                                    payment_method_nonce: paypal_method_nonce
                            ).done (data) ->
                                $("#paypal-container").html(data.paypal_html)
                                console.log("Data:", data)
                    })
                    $("#braintree-paypal-button").html("")
                    $("#braintree-paypal-button").removeAttr("style")
                    $("#braintree-paypal-button").addClass("button-connect-paypal")
                    return
            
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
                this.transitionTo('mybookings.pending')


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
        events:{
            savePaymentDetails: () ->
                # Get braintree client token from server and display form
                $.ajax(
                    url: "/api/braintree_client/"
                    method: "post"
                ).done (data) ->
                    # Create client
                    client = new braintree.api.Client({
                        clientToken: data.client_token
                    })
                    
                    # Concatenate fields to get credit card number
                    credit_card_1 = $("#creditcard_number1").val()
                    credit_card_2 = $("#creditcard_number2").val()
                    credit_card_3 = $("#creditcard_number3").val()
                    credit_card_4 = $("#creditcard_number4").val()
                    credit_card_number = '' + credit_card_1 + credit_card_2 + credit_card_3 + credit_card_4
                    ccv = $("#ccv").val()
                    credit_card_month = $("#creditcard_month").val()
                    credit_card_year = $("#creditcard_year").val()
                    
                    # Billing address
                    street_address = $("#billing_street_address").val()
                    extended_address = $("#billing_extended_address").val()
                    locality = $("#billing_locality").val()
                    region = $("#billing_region").val()
                    postal_code = $("#billing_postal_code").val()
                    
                    # Tokenize card
                    client.tokenizeCard
                        number: credit_card_number
                        expirationMonth: credit_card_month
                        expirationYear: credit_card_year
                        cvv: ccv
                        billingAddress:
                            streetAddress: street_address
                            extendedAddress: extended_address
                            locality: locality
                            region: region
                            postalCode: postal_code
                            countryCodeAlpha2: "US"
                            
                    , (err, nonce) ->
                        $.ajax(
                            url: "/api/update_payment_method/"
                            method: "post"
                            data:
                                payment_method: "credit_card"
                                payment_method_nonce: nonce
                        ).done (data) ->
                            console.log("Update Payment Method Result:", data)
                        console.log("Nonce:", nonce)
                    return
            
            postReview: ()->
                parent = Sitterfied.currentUser
                sitter_id = $("#sitter_id").val()
                recommend = $("#recommended").is(":checked")
                rehire = $("#rehire").is(":checked")
                review = $("#review").val()
                
                if sitter_id
                    sitter = Sitterfied.Sitter.find(sitter_id)
                
                new_review_promise = Sitterfied.SitterReview.create({
                        parent: parent,
                        sitter: sitter,
                        rehire: rehire,
                        recommended: recommend,
                        review: review
                    }).save()
                    
                new_review_promise.then (new_review) =>
                    #Reload new review
                    review_reload_promise = new_review.reload()
                    review_reload_promise.then =>
                        #Repopulate sitters to review by not including sitter from previous list
                        current_sitters_to_review = this.get('controller').get("controllers.currentUser").get("sitters_to_review")
                        sitters_to_review = Em.A()
                        for sitter_to_review in current_sitters_to_review
                            if sitter_id and sitter_to_review.get('id') is not sitter_id
                                sitters_to_review.pushObject(sitter_to_review)
                        this.get('controller').get("controllers.currentUser").set("sitters_to_review", sitters_to_review)
                
                        #Add new_review to review_list
                        current_reviews = this.get('controller').get("controllers.currentUser").get("reviews")
                        current_reviews.pushObject(new_review)
                        this.get('controller').get("controllers.currentUser").set("reviews", current_reviews)
                $.fancybox.close()
                this.get('controller').transitionToRoute('parentEdit.reviews', parent)
                    

            openIntercom: ()->
                Intercom('show')

            removeFromTeam: ()->
                debugger

            editBooking: (booking)  ->
                this.transitionTo('editBook', booking)

            addSitterTeam: (sitter) ->
                Em.run.begin()
                sitterTeam = Sitterfied.currentUser.get('sitter_teams')
                dupSitter = sitterTeam.findProperty('id', sitter.get('id'))
                if dupSitter
                    sitterTeam.removeObject(dupSitter)
                    dupSitter.get('sitter_teams').removeObject(Sitterfied.currentUser)
                    # Remove to network
                    Sitterfied.currentUser.removeFriend(dupSitter)
                else
                    sitterTeam.pushObject(sitter)
                    sitter.get('sitter_teams').pushObject(Sitterfied.currentUser)
                    Sitterfied.currentUser.addFriend(sitter)

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
