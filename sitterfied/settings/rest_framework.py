REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}


DEFAULT_FILTER_BACKENDS = ('rest_framework.filters.DjangoFilterBackend',)
DEFAULT_RENDERER_CLASSES = ('drf_ujson.renderers.UJSONRenderer',)


REST_FRAMEWORK = {
}
