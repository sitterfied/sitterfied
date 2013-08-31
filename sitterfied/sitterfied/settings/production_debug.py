from .base import *
import json
import os

with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

DEBUG = False


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': env.get('DOTCLOUD_CACHE_REDIS_HOST','') + ":" + env.get('DOTCLOUD_CACHE_REDIS_PORT', ''),
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': env.get('DOTCLOUD_CACHE_REDIS_PASSWORD', ''),
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'PICKLE_VERSION': 2,
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sitterfied',
        'USER': env.get('DOTCLOUD_DATA_SQL_LOGIN', ''),
        'PASSWORD': env.get('DOTCLOUD_DATA_SQL_PASSWORD', ''),
        'HOST': env.get('DOTCLOUD_DATA_SQL_HOST', ''),
        'PORT': int(env.get('DOTCLOUD_DATA_SQL_PORT', '0')),
    }
}



# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = "/home/dotcloud/data/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT.child("static")


MIDDLEWARE_CLASSES += (
   'django.middleware.gzip.GZipMiddleware',
   'pipeline.middleware.MinifyHTMLMiddleware',
)

SECRET_KEY =  os.environ.get('DJANGO_SECRET_KEY','boo')
from .mandrill import *



INSTALLED_APPS += (
    'debug_toolbar',
    'devserver'
)

MIDDLEWARE_CLASSES += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEVSERVER_ARGS = ['--werkzeug']

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
)


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
