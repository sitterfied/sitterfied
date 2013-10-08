define ['ember'
        '_'
        "cs!sitterfied"
        'cs!models'
        ], (Em, _, Sitterfied) ->

        Em.Application.initializer(
            name: "currentUser"
            initialize: (container, application) ->
                user = Sitterfied.loadUserJson(user_json)
                controller = container.lookup('controller:currentUser').set('model', user)
                container.typeInjection('controller', 'currentUser', 'controller:currentUser')
                Sitterfied.set('authenticated', authenticated)
                Sitterfied.set('currentUserController', controller)

        )




        # Em.Application.initializer
        #     name: "certificationController"
        #     initialize: (container, application) ->
        #         certController = Sitterfied.CertificationsController.create()
        #         Sitterfied.set('certificationsController',certController)
        #         Sitterfied.set('certificationsController.content',Sitterfied.Certification.find())
        # Em.Application.initializer
        #     name: "otherServicesController"
        #     initialize: (container, application) ->
        #         otherController = Sitterfied.OtherServicesController.create()
        #         Sitterfied.set('otherServicesController', otherController)
        #         Sitterfied.set('otherServicesController.content', Sitterfied.OtherService.find())
        # Em.Application.initializer
        #     name: "languagesController"
        #     initialize: (container, application) ->
        #         languagesController = Sitterfied.LanguagesController.create()
        #         Sitterfied.set('languagesController', languagesController)
        #         Sitterfied.set('languagesController.content', Sitterfied.Language.find())
