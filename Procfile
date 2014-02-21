web: python manage.py runserver
worker: celery worker --app=sitterfied --workdir=sitterfied --loglevel=INFO
broker: redis-server
watcher: python templates.py

