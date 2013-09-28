define ["ember", "cs!sitterfied", 'imgareaselect', 'ucare', 'waypoints'], (Em, Sitterfied) ->
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
            @$().datepicker(
                dateFormat: 'D, dd M yy',
                showOtherMonths: true,
                selectOtherMonths: true,
                numberOfMonths: [ 1, 2 ],
                minDate:0
            ).on 'changeDate', =>
                @$().trigger('change')
    })


    Sitterfied.NetworkDropDown = Em.View.extend({
        selected: null
        add: () ->
            selected = @get('selected')
            if not selected?
                groupName = @$('#autocomplete').val()
                Sitterfied.currentUserController.createGroup(groupName)
            else if selected.type == "user"
                Sitterfied.currentUserController.addFriend(selected.id)
            else if selected.type == "group"
                Sitterfied.currentUserController.addGroup(selected.id)

            @$('#autocomplete').val("")
            @set('selected', null)

        didInsertElement: ()->
            that = this
            selected_event = (event, ui) ->
                that.set('selected', ui.item)

            @$('#autocomplete').autocomplete({
                select: selected_event

                source: (request, response) ->
                    $.ajax
                        url: "/network_search",
                        data:
                            search: request.term
                        success: (data) ->
                            response(data)
            })
            return
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

    Sitterfied.photoPopupView = Ember.View.extend(
        dialogFinished: (file) =>
            $.ajax
                type: "POST"
                url:"/api/users/" + Sitterfied.currentUser.id + "/avatar_upload/"
                dataType: 'json'
                data: {
                    avatar: file.cdnUrl
                }
                success: (response) ->
                    Sitterfied.currentUser.set('avatar', response.avatar)
                error: () ->
                    alert("There was a problem uploading your avatar. Please try again")


        click: () ->
            dialog = uploadcare.openDialog()
            df = this.dialogFinished
            dialog.done (result) ->
                result.then(df)

        tagName: "p"

    )
    Sitterfied.AvatarFileField = Ember.View.extend(
        init: () ->
            this._super()

        _elementValueDidChange: () ->
            value = @.$().attr('value')
            $("#avatar_uuid").attr('value', value)

        classNames: ['ember-file-field'],
        tagName: "input",
        attributeBindings: ['data-images-only', 'data-crop', 'type', 'role', 'data-public-key', 'data-tabs']
        'data-images-only': 'static'
        'data-crop':'174x174 upscale'
        'data-tabs': "file facebook"
        'role':"uploadcare-uploader"
        'type':"hidden"
        value: ""

        didInsertElement: () ->
            uploadcare.start()
            Sitterfied.uploadwidget = uploadcare.initialize()[0]
            Sitterfied.uploadwidget.onChange () =>
                this._elementValueDidChange()

    )


    Sitterfied.SlideDownView = Ember.View.extend
        toggle: ((key, value) ->
            if value == undefined
                return
            @set('_show', value)
        ).property()

        doSlide: (() ->
            direction = @get('_show')
            if direction == false
                @slideUp()
            else
                @slideDown()
        ).observes("_show")

        slideUp: () ->
            @$().slideUp()
        slideDown: () ->
            @$().slideDown()


        _show: false

        didInsertElement: () ->
            @$().hide()

    Sitterfied.SitterAboutView =  Em.View.extend
        scrollSnapshot: () ->
            $.scrollTo("#tab-1-1", 300)
        scrollDetails: () ->
            $.scrollTo("#tab-1-2", 300)


    Sitterfied.ScrollSlideDownView = Sitterfied.SlideDownView.extend
        init: () ->
            this._super();
            @_event = () =>
                @shinkDropdowns()

        shinkDropdowns: () ->
            @set('_show', false)
            #ug this is a hack
            @set('controller.didScrollHide', true)

        slideDown: () ->
            @$().slideDown()
            @set('controller.didScrollHide', false)


        didInsertElement: () ->
            this._super();
            $(window).bind "scroll", @_event

        willDestroyElement: () ->
            this._super();
            $(window).unbind "scroll", @_event

    Sitterfied.ToggleView = Sitterfied.SlideDownView.extend
        slideUp: () ->
            @$().hide( "bounce", { times: 3 }, "fast" )
        slideDown: () ->
            debugger
            @$().show( "bounce", { times: 3 }, "fast" )


    Sitterfied.SortItemView = Em.View.extend
        tagName: "li"

        classNameBindings: ['active']

        click: () ->
            prop = this.get('sortProp')
            direction = this.get('direction')
            this.get('controller').sortSet(prop, direction)

        active: (() ->
            controller = this.get('controller')
            sortProp = controller.get('sortProperties')?[0]

            return this.get('sortProp') == sortProp
        ).property('controller.sortProperties.@each')


    Sitterfied.BackToTop = Em.View.extend
        init: () ->
            this._super();
            @_event = () =>
                y = $(window).scrollTop()
                overflow = $(document).height() > $(window).height()
                if y > 200 and overflow
                    @set('show', true)
                else
                    @set('show', false)

        show: false

        click: () ->
            $.scrollTo(0, 500)

        display: (() ->
            @$().toggle( "bounce", { times: 3 }, "fast" );
        ).observes('show')

        didInsertElement: () ->
            @$().hide()
            $(window).bind "scroll", @_event


    Sitterfied.FixedView =  Em.View.extend
        init: () ->
            this._super();
            @_event = () =>
                @notifyPropertyChange('fixed')


        classNameBindings: ['fixed']

        fixed: (() ->
            y = $(window).scrollTop();
            if y >= this.get('top')
                return true
            else
                return false
        ).property()

        didInsertElement: () ->
            top = this.$().offset().top
            auto =  parseFloat(this.$().css('margin-top').replace(/auto/, 0))
            this.set('top',top - auto)
            $(window).bind "scroll", @_event
            @notifyPropertyChange('fixed')

        willDestroyElement: () ->
            $(window).unbind "scroll", @_event


    Sitterfied.SitterTopView = Em.View.extend
        readMore: () ->
            $('.header .top_info').addClass('show_full_desc');
            $('.header .top_info .desc .full_desc').fadeIn();

        didInsertElement: () ->
            $('.header .top_info .desc .full_desc').on 'click', () ->
                $('.header .top_info').removeClass('show_full_desc')
                $('.header .top_info .desc .full_desc').fadeOut()


    Sitterfied.MobTriggerView = Em.View.extend
        classNameBindings: ['active', ":mob_tab_trigger", "my_mob_tab"]
        active: false
        my_mob_tab:  false
        click: () ->
            @toggleProperty('active')
            @$("+ .subtab_content").slideToggle()
            @$("+ .tab_content").slideToggle()


    Sitterfied.TriggerView = Em.View.extend
        click: () ->
            @$().toggleClass('active')
            $('.header nav').fadeToggle()

    Sitterfied.WaypointActiveView = Em.View.extend
        didInsertElement: () ->
            @$().waypoint () =>
                targetClass = @get('targetClass')
                $("li.active").removeClass('active')
                $("." +targetClass).addClass('active')



    #Sitterfied.BookingView = Em.View.extend


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
    Sitterfied.Select2 = Ember.Select.extend(
      attributeBindings: ["required", "multiple"]
      required: false
      width: "resolve"
      allowClear: true
      closeOnSelect: true
      prompt: "Please make a selection"
      # initialize Select2 once view is inserted in DOM
      didInsertElement: ->
        #this._super();
        placeholderText = @get("prompt")
        throw new Exception("select2 is required for Sitterfied.Select2 control")  unless @$().select2
        @$().select2
          containerCssClass: "select2-portfolio"
          placeholder: placeholderText
          allowClear: @get("allowClear")
          closeOnSelect: @get("closeOnSelect")
          width: @get("width")


      willDestroyElement: ->
        @$().select2 "destroy"


      # when data is loaded, update select2 to show
      # this data

      # trigger change event on selectbox once data
      # has been loaded to update options values

      # trigger change event on select2
      itemsLoaded: (->
        console.log "select2 items loaded"
        Ember.run.sync()
        Ember.run.next this, ->
          console.log "updating select2 options list"
          @$().change()  if @$()
      ).observes("controller.content.isLoaded")

      setSelectedValue: (value) ->
        console.log "setting select2 selected value to " + value
        @$().select2 "val", value if @$()


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
        selection = @get('selection')
        if !selection?
            if @get('multiple')
                newval = []
            else
                newval = ""
        else if fieldname == "content" or typeof(selection) != "object"
            newval = selection
        else
            newval =  Em.get(selection, fieldname)
        Ember.run.sync()
        Ember.run.next this, ->
            @setSelectedValue newval
      ).observes("selection")

    )
