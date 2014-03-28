# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from filebrowser.sites import site


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/filebrowser/?', include(site.urls)),
    url(r'^grappelli/?', include('grappelli.urls')),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^', include('favicon.urls')),
    url(r'^favicon.ico/$', RedirectView.as_view(url="/static/favicon.ico")),

)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        '',
        url(
            r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }
        )
    )


urlpatterns += patterns(
    '',
    url(r'', include('app.urls')),
)
