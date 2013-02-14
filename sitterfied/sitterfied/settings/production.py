from .base import *
import json
import os

with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

DEBUG = True


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': env['DOTCLOUD_CACHE_REDIS_HOST'] + ":" + env['DOTCLOUD_CACHE_REDIS_PORT'],
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': env['DOTCLOUD_CACHE_REDIS_PASSWORD'],
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'PICKLE_VERSION': 2,
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sitterfied',
        'USER': env['DOTCLOUD_DATA_SQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DATA_SQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DATA_SQL_HOST'],
        'PORT': int(env['DOTCLOUD_DATA_SQL_PORT']),
    }
}



# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT.child("static")


MIDDLEWARE_CLASSES += (
   'django.middleware.gzip.GZipMiddleware',
   'pipeline.middleware.MinifyHTMLMiddleware',
)

SECRET_KEY =  os.environ['DJANGO_SECRET_KEY']
