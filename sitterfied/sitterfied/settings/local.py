from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sitterfied',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'sitterfied',
        'PASSWORD': 'sitterfied',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_ROOT.child("media")
MEDIA_URL = "/media/"

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT.child("static")

GOOGLE_OAUTH_CLIENT_ID = '778609432409-h3p3eumt29copfqrcsv7dksapkpbssbq.apps.googleusercontent.com'
GOOGLE_OAUTH_CLIENT_SECRET = 'Xo2d7W1OK7ezu4rfGBoEhSuM'
GOOGLE_OAUTH_REDIRECT_URI = "http://localhost:8000"

INSTALLED_APPS += (
#    'debug_toolbar',
    'devserver',
)

MIDDLEWARE_CLASSES += (
#    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

INTERNAL_IPS = ('127.0.0.1',)

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
DEVSERVER_AUTO_PROFILE = True
