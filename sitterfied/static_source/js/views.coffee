define ["ember", "cs!sitterfied"], (Em, Sitterfied) ->
    Ember.RadioButton = Em.View.extend({
        tagName : "input",
        type : "radio",
        attributeBindings : [ "name", "type", "value", "checked:checked:" ],
        click : () ->
            this.set("selection", this.$().val())
        checked : (() ->
            return this.get("value") == this.get("selection");
        ).property('value', 'selection')
    })

    Ember.DatePicker = Em.TextField.extend({
        didInsertElement: ()->
            #setup datepicker and keep ember insync with it
            @.$().datepicker({dateFormat:"yy-mm-dd"}).on 'changeDate', =>
                @.$().trigger('change')
    })



    Ember.ChosenSelect = Em.Select.extend({
        didInsertElement: () ->
            this._super();
            this.$().chosen();

        selectionChanged: (() ->
            this.$().trigger('liszt:updated');
        ).observes('selection')
    })

    Ember.ChosenMultipleSelect = Ember.ChosenSelect.extend({
        multiple: true,
        attributeBindings: [ 'multiple' ],
    });

    Ember.States = [
            'AL',
            'AK',
            'AZ',
            'AR',
            'CA',
            'CO',
            'CT',
            'DE',
            'DC',
            'FL',
            'GA',
            'HI',
            'ID',
            'IL',
            'IN',
            'IA',
            'KS',
            'KY',
            'LA',
            'ME',
            'MD',
            'MA',
            'MI',
            'MN',
            'MS',
            'MO',
            'MT',
            'NE',
            'NV',
            'NH',
            'NJ',
            'NM',
            'NY',
            'NC',
            'ND',
            'OH',
            'OK',
            'OR',
            'PA',
            'RI',
            'SC',
            'SD',
            'TN',
            'TX',
            'UT',
            'VT',
            'VA',
            'WA',
            'WV',
            'WI',
            'WY',
        ]


    Ember.Educations = [
        "Some High Scool"
        "High Scool Degree"
        "Some College"
        "College Degree"
        ]

    Sitterfied.BookingView = Em.View.extend()
    #showNote
    #isNoteShown
    # action
    # decline
    # cancel