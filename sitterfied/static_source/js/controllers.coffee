define ["ember", "cs!sitterfied", "cs!models"], (Em, Sitterfied) ->

    Sitterfied.BookController = Em.ArrayController.extend(
        cancel: () ->
            alert('cancel')
            this.transitionTo('search');
        book: () ->
            alert('send')
            this.transitionTo('done');
    )


    Sitterfied.DoneController = Em.ArrayController.extend(
        cancel: () ->
            alert('cancel')
            this.transitionTo('search');
        edit: () ->
            alert('edit')
            this.transitionTo('book');
    )

    Sitterfied.SettingsController = Em.ObjectController.extend(
        save: () ->
            settings =  this.get('settings')
            if settings.get('isDirty')
                settings.save()
            if this.get('model.isDirty')
                this.get('model').save()

        deleteAccount: () ->
            alert('delete')
        old_password : ''
        new_password1 : ''
        new_password2 : ''
        resetPassword: () ->
            if @get('new_password1') != @get('new_password2')
                alert("Your passwords must match")
                return
            data = {
                new_password1: @get('new_password1')
                new_password2: @get('new_password2')
                old_password: @get('old_password')
            }
            $.post('password_change/', data).success(alert('password changed'))
    )