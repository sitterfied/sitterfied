# -*- coding: utf-8 -*-
from unipath import Path

from .pipeline import *

PROJECT_ROOT = Path(__file__).ancestor(2)

DEBUG = TEMPLATE_DEBUG = False

ADMINS = (
    ('Andrew Lewisohn', 'alewisohn@sitterfied.com'),
)

MANAGERS = ADMINS

SITE_ID = 1

SILENCED_SYSTEM_CHECKS = ('1_6.W001',)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = PROJECT_ROOT.child("static")
STATIC_ROOT = '/www/static'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT.child("static_source"),  # An absolute path: /foo/bar/baz.py
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = "&)y$vgj8lzxlexal31dcd(^ua(0yf95)f^b@$=*to5s)*eznxq"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.request",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages")

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sitterfied.app.middleware.TimezoneMiddleware',
)

ROOT_URLCONF = 'sitterfied.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sitterfied.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT.child('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_twilio',
    'django_mandrill',
    'registration',
    'crispy_forms',
    'floppyforms',
    'annoying',
    'rest_framework',
    'django_extensions',
    'model_utils',
    'pipeline',
    'pyuploadcare.dj',
    'favicon',
    'sitterfied.app',
    'sitterfied.bookings',
    'sitterfied.children',
    'sitterfied.parents',
    'sitterfied.schedules',
    'sitterfied.sitters',
    'sitterfied.users',
    'sitterfied.utils',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/var/log/sitterfied/application.log',
            'maxBytes': 1024 * 1024 * 25,  # 25 MB
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'log_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'log_file'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

EMAIL_BACKEND = 'django_mandrill.mail.backends.mandrillbackend.EmailBackend'

AUTH_USER_MODEL = 'app.User'
LOGIN_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 30

DEFAULT_FROM_EMAIL = 'hello@sitterfied.com'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
ALLOWED_HOSTS = [
    'localhost',
    '.sitterfied.com',
    '.sttrfd.us',
    '.elb.amazonaws.com',
    'ping',
]

AUTHENTICATION_BACKENDS = (
    'sitterfied.app.authentication.EmailAuthBackend',
    'sitterfied.app.authentication.FacebookAuthBackend',
)

# Base URL for shortened URLs
SHORT_URL = 'sttrfd.us/'

# Celery configuration
CELERYD_HIJACK_ROOT_LOGGER = False
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_DISABLE_RATE_LIMITS = True
CELERY_IGNORE_RESULTS = True
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IMPORTS = (
    'sitterfied.app.tasks.jobs',
    'sitterfied.app.tasks.notifications',
    'sitterfied.app.tasks.reminders',
    'sitterfied.app.tasks.users',
    'sitterfied.utils.knowtify',
)
DEFAULT_TASK_LOCK_EXPIRE = 60 * 5

SERVER_EMAIL = 'no-reply@sitterfied.com'

# Reminder times in seconds
JOB_FIRST_REMINDER = 86400  # 24 Hours
JOB_SECOND_REMINDER = 3600  # 1 Hour
JOB_RELIEF_REMINDER = 3600  # 1 Hour

# This sets the X-Frame-Options HTTP response header to allow loading
# of the site in the Popcorn Metrics editor. This is only for the
# Popcorn Metrics editor interface, which requires Firefox.
X_FRAME_OPTIONS = 'ALLOW-FROM www.popcornmetrics.com'

# API Key for OpenCage
OPEN_CAGE_API_KEY = '5c60dbbfd592484f7835ae9a976b96b4'

# AWS Settings
AWS_REGION = 'us-east-1'
AWS_ACCESS_KEY_ID = 'AKIAIRC5KBNUD4ERCW5A'
AWS_SECRET_ACCESS_KEY = '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'

REDIS_URL = 'redis://127.0.0.1:6379'

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}
