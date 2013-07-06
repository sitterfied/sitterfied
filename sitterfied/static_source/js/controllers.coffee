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