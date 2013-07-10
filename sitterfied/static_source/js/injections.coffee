define ['ember'
        '_'
        "cs!sitterfied"
        'cs!models'
        ], (Em, _, Sitterfied) ->

        Em.Application.initializer(
            name: "currentUser"
            initialize: (container, application) ->
                store = container.lookup('store:main')
                user_data = JSON.parse(user_json)
                model = parent_or_sitter
                ref = store.load(model, user_data)
                user = Sitterfied[model].find(ref.id)
                Sitterfied.currentUser = user
                controller = container.lookup('controller:currentUser').set('model', user)
                container.typeInjection('controller', 'currentUser', 'controller:currentUser')
                Sitterfied.set('currentUserController', controller)

        )


        Em.Application.initializer(
            name: "certificationController"
            initialize: (container, application) ->
                certController = Sitterfied.CertificationsController.create()
                Sitterfied.set('certificationsController',certController)
                Sitterfied.set('certificationsController.content',Sitterfied.Certification.find())
                # controller = container.lookup('controller:currentUser').set('model', user)
                # container.typeInjection('controller', 'currentUser', 'controller:currentUser')
                # Sitterfied.set('currentUserController', controller)

        )
