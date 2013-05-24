define [
    "ember"
    "cs!sitterfied"
    'ember_data'
    ], (Em, Sitterfied, DS) ->


    Sitterfied.Store = DS.Store.extend(
        revision: 12
    )

    Sitterfied.UserMixin = Em.Mixin.create(
        #django builtins
        id: DS.attr('number'),
        last_login: DS.attr('date'),
        is_superuser: DS.attr('boolean'),
        username: DS.attr('string'),
        firstName: DS.attr('string'),
        lastName: DS.attr('string'),
        email: DS.attr('string'),


        status: DS.attr('string'),
        parentsInNetwork: DS.hasMany('Sitterfied.Parent')
        sittersInNetwork: DS.hasMany('Sitterfied.Sitter')
        languages: DS.hasMany('Sitterfied.Language')


        fullName: (() ->
            return @get('firstName') + ' ' + @get('lastName');
        ).property('firstName', 'lastName')
    )

    Sitterfied.Parent = DS.Model.extend(Sitterfied.UserMixin,
        emergencyContact : DS.belongsTo('Sitterfied.Contact'),
        physicianContact : DS.belongsTo('Sitterfied.Contact'),
        parkingArea : DS.attr('boolean'),
        parkingForSitter: DS.attr('boolean'),
    )

    Sitterfied.Sitter = DS.Model.extend(Sitterfied.UserMixin,
        biography: DS.attr('string'),
        idVerified: DS.attr('boolean'),
        idScanPath: DS.attr('string'),
        liveZip: DS.attr('string'),
        workZip: DS.attr('string'),
        dob: DS.attr('date'),
        smoker: DS.attr('boolean'),
        willTransport: DS.attr('boolean'),
        infantExp: DS.attr('number'),
        toddlerExp: DS.attr('number'),
        preschoolExp: DS.attr('number'),
        schoolAgeExp: DS.attr('number'),
        preTeenExp: DS.attr('number'),
        teenExp: DS.attr('number'),

        highestEducation: DS.attr('string'),
        lastSchool: DS.attr('string'),
        currentStudent: DS.attr('boolean'),
        certification: DS.attr('string'),
        otherServices: DS.attr('string'),
        oneChildMinRate: DS.attr('number'),
        oneChildMaxRate: DS.attr('number'),
        twoChildMinRate: DS.attr('number'),
        twoChildMaxRate: DS.attr('number'),
        threeChildMinRate: DS.attr('number'),
        threeChildMaxRate: DS.attr('number'),

        smokersOk: DS.attr('boolean'),
        dogsOk: DS.attr('boolean'),
        catsOk: DS.attr('boolean'),
        otherAnimalsOk: DS.attr('boolean'),

        totalExp: (() ->
            return @get('infantExp') + @get('toddlerExp') + @get('preschoolExp') + @get('schoolAgeExp') + @get('preTeenExp') + @get('teenExp')
        ).property('infantExp','toddlerExp','preschoolExp', 'schoolAgeExp', 'preTeenExp', 'teenExp')

    Sitterfied.Language = DS.Model.extend(
        language: DS.attr('string'),
    )

    Sitterfied.Child = DS.Model.extend(
        parent: DS.belongsTo('Sitterfied.Parent'),
        name: DS.attr('string'),
        dob: DS.attr('date'),
        school: DS.attr('string'),
        sitterInstructions: DS.attr('string'),
        specialNeeds: DS.attr('string'),
        allergies: DS.attr('string'),
    )

    Sitterfied.SitterReview = DS.Model.extend(
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
        respondBy: DS.attr('date'),
        startDateTime: DS.attr('date'),
        stopDateTime: DS.attr('date'),
        child: DS.hasMany("Sitterfied.Child")
        #emergency_phone: models.ForeignKey('Phone')
        bookingStatus:DS.attr('string'),
        #location: models.ForeignKey('Address')
    )