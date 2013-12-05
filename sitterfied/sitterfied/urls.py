from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^admin/filebrowser/?', include(site.urls)),
    url(r'^grappelli/?', include('grappelli.urls')),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^', include('favicon.urls')),
    url(r'^favicon.ico/$', RedirectView.as_view(url="/static/favicon.ico")),

)


from django.conf import settings
#TODO dev
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
urlpatterns += patterns('',
    url(r'', include('app.urls')),
                        )
