define [
    "ember"
    "cs!sitterfied"
    'data'
    'djangoRestAdapter'
    ], (Em, Sitterfied, DS) ->


    Sitterfied.Store = DS.Store.extend(
        revision: 12
        adapter: DS.DjangoRESTAdapter.create({
            namespace: 'api'
        })
        isDefaultStore:true
    )

    Sitterfied.UserMixin = Em.Mixin.create(
        #django builtins
        #last_login: DS.attr('date')
        is_superuser: DS.attr('boolean')
        username: DS.attr('string')
        first_name: DS.attr('string')
        last_name: DS.attr('string')
        email: DS.attr('string')
        status: DS.attr('string')
        parents_inNetwork: DS.hasMany('Sitterfied.Parent')
        sitters_inNetwork: DS.hasMany('Sitterfied.Sitter')
        languages: DS.hasMany('Sitterfied.Language')
        settings  : DS.belongsTo('Sitterfied.Setting')

        full_name: ((key, value) ->
            if arguments.length == 1
                return @get('first_name') + ' ' + @get('last_name')

            else
                [first_name, last_name] = value.trim().split(" ", 2)
                this.set('first_name', first_name)
                this.set('last_name', last_name)
                return value
        ).property('first_name', 'last_name')
    )

    Sitterfied.Setting = DS.Model.extend(
        #parent specific
        mobile_booking_accepted_denied: DS.attr('boolean')

        #sitter specific
        mobile_new_review : DS.attr('boolean')
        mobile_booking_request: DS.attr('boolean')

        mobile_friend_joined: DS.attr('boolean')
        mobile_groups_added_network: DS.attr('boolean')
        mobile_upcoming_booking_remind: DS.attr('boolean')

        #parent specific
        email_booking_accepted_denied: DS.attr('boolean')

        #sitter specific
        email_new_review : DS.attr('boolean')
        email_booking_request: DS.attr('boolean')

        email_friend_joined: DS.attr('boolean')
        email_groups_added_network: DS.attr('boolean')
        email_upcoming_booking_remind: DS.attr('boolean')

        email_news: DS.attr('boolean')
        email_blog: DS.attr('boolean')
    )

    Sitterfied.Contact = DS.Model.extend(
        #flush out later
    )

    Sitterfied.Parent = DS.Model.extend(Sitterfied.UserMixin,
        emergency_contact : DS.belongsTo('Sitterfied.Contact'),
        physician_contact : DS.belongsTo('Sitterfied.Contact'),
        parking_area : DS.attr('boolean'),
        parking_for_sitter: DS.attr('boolean'),
    )

    Sitterfied.Sitter = DS.Model.extend(Sitterfied.UserMixin,
        biography: DS.attr('string'),
        id_verified: DS.attr('boolean'),
        id_scanPath: DS.attr('string'),
        live_zip: DS.attr('string'),
        work_zip: DS.attr('string'),
        dob: DS.attr('date'),
        smoker: DS.attr('boolean'),
        will_transport: DS.attr('boolean'),
        infant_exp: DS.attr('number'),
        toddler_exp: DS.attr('number'),
        preschool_exp: DS.attr('number'),
        school_ageExp: DS.attr('number'),
        pre_teenExp: DS.attr('number'),
        teen_exp: DS.attr('number'),

        highest_education: DS.attr('string'),
        last_school: DS.attr('string'),
        current_student: DS.attr('boolean'),
        certification: DS.attr('string'),
        other_services: DS.attr('string'),
        one_childMin_rate: DS.attr('number'),
        one_childMax_rate: DS.attr('number'),
        two_childMin_rate: DS.attr('number'),
        two_childMax_rate: DS.attr('number'),
        three_childMin_rate: DS.attr('number'),
        three_childMax_rate: DS.attr('number'),

        smokers_ok: DS.attr('boolean'),
        dogs_ok: DS.attr('boolean'),
        cats_ok: DS.attr('boolean'),
        other_animalsOk: DS.attr('boolean'),

        total_exp: (() ->
            return @get('infant_exp') + @get('toddler_exp') + @get('preschool_exp') + @get('school_ageExp') + @get('pre_teenExp') + @get('teen_exp')
        ).property('infant_exp','toddler_exp','preschool_exp', 'school_ageExp', 'pre_teenExp', 'teen_exp')
    )

    Sitterfied.Language = DS.Model.extend(
        language: DS.attr('string'),
    )


    Sitterfied.Child = DS.Model.extend(
        parent: DS.belongsTo('Sitterfied.Parent'),
        name: DS.attr('string'),
        dob: DS.attr('date'),
        school: DS.attr('string'),
        sitter_instructions: DS.attr('string'),
        special_needs: DS.attr('string'),
        allergies: DS.attr('string'),
    )

    Sitterfied.Sitter_review = DS.Model.extend(
        parent: DS.belongsTo('Sitterfied.Parent'),
        sitter: DS.belongsTo('Sitterfied.Sitter'),
        recommended: DS.attr('boolean'),
        review: DS.belongsTo('string'),
        rating: DS.belongsTo('number'),
    )

    Sitterfied.Booking = DS.Model.extend(
        parent: DS.belongsTo('Sitterfid.Parent'),
        sitter: DS.belongsTo('Sitterfied.Sitter'),
        notes: DS.attr('string'),
        respond_by: DS.attr('date'),
        start_dateTime: DS.attr('date'),
        stop_dateTime: DS.attr('date'),
        child: DS.hasMany("Sitterfied.Child"),
        #emergency_phone: models.Foreign_key('Phone')
        #location: models.Foreign_key('Address')
        booking_status:DS.attr('string'),
    )