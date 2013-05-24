define ["cs!sitterfied"], (Sitterfied) ->
    Sitterfied.Router.map(() ->
        this.route('sitter')
        this.route('parent')
    )

    Sitterfied.IndexRoute = Em.Route.extend(
      model: () ->
        return ['red', 'yellow', 'blue']
    );
