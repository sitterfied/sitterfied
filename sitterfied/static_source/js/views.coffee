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


    Sitterfied.UnboundSelectOption = Ember.SelectOption.extend(
      template: Ember.Handlebars.compile("{{unbound view.content}}")
      didInsertElement: ->
        @_super()
        view = this
        Ember.run.sync()
        Ember.run.next ->
          $("select").trigger "liszt:updated"
    )

    Sitterfied.ChosenSelect = Ember.Select.extend(
      chosenOptions: {}

      optionLabelPath: "content"
      optionValuePath: "content"

      contentBinding: "controller.content"
      template: Ember.Handlebars.compile("{{#if prompt}}{{unbound prompt}}{{/if}}" + "{{#each content}}{{view Sitterfied.UnboundSelectOption contentBinding=\"this\"}}{{/each}}")

      didInsertElement: ->
        @.$().chosen()

      _closeChosen: ->

        # trigger escape to close chosen
        @$().next(".chzn-container-active").find("input").trigger
          type: "keyup"
          which: 27

      rerender: ->
        # remove now disconnected html
        @$().next(".chzn-container").remove()  if @get("state") is "inDOM"
        @_super()

      rerenderChosen: ->
        @$().trigger "liszt:updated"

      selectionChanged: (() ->
            this.$().trigger('liszt:updated');
        ).observes('selection')

    )


    Sitterfied.MultipleChosenSelect = Sitterfied.ChosenSelect.extend(
        multiple: true,
        attributeBindings: [ 'multiple' ],

    )


    Sitterfied.AvatarFileField = Ember.View.extend(

        init: () ->
            this._super();
            this.on("change", this, this._elementValueDidChange);


        _elementValueDidChange: () ->
            file = this.$()[0].files[0]
            if file
                reader = new FileReader()
                reader.onload = (e) ->
                    $("#imgPreview").attr('src', e.target.result)
                    Sitterfied.set('onDeckAvatar', e.target.result)
                reader.readAsDataURL(file)



        classNames: ['ember-file-field'],
        tagName: "input",
        attributeBindings: ['type', 'value', 'size'],

        value: ""

        type: "file"
    )


    Sitterfied.BookingView = Em.View.extend()
    #showNote
    #isNoteShown
    # action
    # decline
    # cancel
    #
    # Select box utilizing Select2 functionality that overrides Ember.Select;
    # Define view in the same way that you would an Ember.Select view.
    # Additional attributes supported are: width, allowClear, and closeOnSelect;
    # Example view:
    #                {{ view App.Select2
    #                     viewName="fieldValueSelect2"
    #    	       prompt="Please select a value list"
    #                     contentBinding="controller.fieldValuesLists"
    #                     optionLabelPath="content.name"
    #                     optionValuePath="content.id"
    #                     selectionBinding="content.allowedValuesList"
    #                     required="" }}
    #
    # To enable routing upon selection of an item from Select2 box, subclass the
    # Select2 view and add the actions to the valueDidChange event:
    #
    #  App.ContainterSelect2 = App.Select2.extend({
    #
    #	// bind change in selected portfolio to trigger routing
    #	// to show portfolio or portfolio list if null
    #    valueDidChange: Ember.observer(function() {
    #        this._super();
    #        var selection = this.get('selection');
    #        if (selection) {
    #            console.log('select2 value changed to ' + selection.get('name'));
    #        	this.get('controller').transitionToRoute('container.show', selection);
    #        } else {
    #        	this.get('controller').transitionToRoute('container.index');
    #        }
    #    }, 'value')
    #});
    #
    # Author: http://github.com/aboma
    Sitterfied.Select2 = Ember.Select.extend(
      defaultTemplate: Ember.Handlebars.compile("<option>{{#if prompt}}{{unbound prompt}}{{/if}}</option>{{#each view.content}}{{view Ember.SelectOption contentBinding=\"this\"}}{{/each}}")
      attributeBindings: ["required"]
      required: false
      width: "resolve"
      allowClear: true
      closeOnSelect: true

      # initialize Select2 once view is inserted in DOM
      didInsertElement: ->

        #this._super();
        placeholderText = @get("prompt") or ""
        throw new Exception("select2 is required for Sitterfied.Select2 control")  unless @$().select2
        @$().select2
          containerCssClass: "select2-portfolio"
          placeholder: placeholderText
          allowClear: @get("allowClear")
          closeOnSelect: @get("closeOnSelect")
          width: @get("width")


      willDestroyElement: ->
        console.log "destroying select2"
        @$().select2 "destroy"


      # when data is loaded, update select2 to show
      # this data

      # trigger change event on selectbox once data
      # has been loaded to update options values

      # trigger change event on select2
      itemsLoaded: ->(
        console.log "select2 items loaded"
        Ember.run.sync()
        Ember.run.next this, ->
          console.log "updating select2 options list"
          @$().change()  if @$()

      ).observes("controller.content.isLoaded")
      setSelectedValue: (value) ->
        console.log "setting select2 selected value to " + value
        @$().select2 "val", value


      # observe controller selected content and update select2
      # selected item if selected item is changed on the
      # controller and does not match currently selected value;
      # this occurs when the selected value is changed outside of
      # the control; must wait until next ember run since
      # it seems that after create, a new item is not yet available
      # in the list to be selected

      # trigger change event on selectbox once data
      # has been loaded to update options values
      setSelected: (->
        path = @get("optionValuePath")
        s = path.split(".")
        fieldname = s[s.length - 1]
        fieldvalue = ""
        selected = @get("controller.selected")
        sel2Val = @$().select2("val")
        fieldvalue = selected.get(fieldname)  if selected
        if sel2Val isnt fieldvalue or fieldvalue is ""
          Ember.run.sync()
          Ember.run.next this, ->
            @setSelectedValue fieldvalue

      ).observes("controller.selected")
    )