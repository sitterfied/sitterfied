Celery
======

An open source distributed task queue.

Overview
--------

This role is meant to be included by top-level playbooks and supports
configuring multiple sites, copying over SSL certificate pairs, and also
htpasswd files for HTTP basic authentication.

Role Variables
--------------

These variables update the values defined under */etc/defaults/celeryd*,
and only **celery_chdir** is required.

### <kbd>celery_chdir</kbd>

Path to change directory to at start. **Required**.

### <kbd>celery_enabled</kbd>

Whether or not to start the celery daemon. Default is *true*.

### <kbd>celery_nodes</kbd>

Node names to start. Default is *celery*

### <kbd>celery_opts</kbd>

Additional arguments to celeryd, see `celeryd –help` for a list.

### <kbd>celery_pid_file</kbd>

Full path to the PID file. Default is */var/run/celery/%n.pid*

### <kbd>celery_log_file</kbd>

Full path to the celeryd log file. Default is */var/log/celery/%n.log*

### <kbd>celery_log_level</kbd>

Log level to use for celeryd. Default is *INFO*.

### <kbd>celery_multi</kbd>

Path to the celeryd-multi program. Default is *celeryd-multi*. You can
point this to a virtualenv, or even use manage.py for django.

### <kbd>celery_celeryctl</kbd>

Path to the celeryctl program. Default is *celeryctl*. You can point this
to a virtualenv, or even use manage.py for django.

### <kbd>celery_user</kbd>

User to run celeryd as. Default is *celery*.

### <kbd>celery_group</kbd>

Group to run celeryd as. Default is *celery*.

### <kbd>celery_app</kbd>

The value to set for the `--app` parameter passed to the `celery multi` or 
`celery beat` commands. Default is nothing.

### <kbd>celery_django_settings_module</kbd>

What to export for the environment variable *$DJANGO_SETTINGS_MODULE*. Default 
is nothing.

Commands
--------

Restart the celery daemon by running:

    $ sudo service celeryd restart

References
----------

* [Daemonizing Celery](http://ask.github.io/celery/cookbook/daemonizing.html)
