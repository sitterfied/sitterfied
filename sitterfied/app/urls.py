from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('app.views',
    # Examples:
    url(r'^email_submit/$', 'comingsoon_email_submit', name='comingsoon_email_submit'),
    url(r'^invite_email_submit/$', 'invite_email_submit', name='invite_email_submit'),
    url(r'^$', 'index'),
    url(r'^about/$', direct_to_template, {'template': 'howitworks.html'}, name="howitworks"),
    url(r'^refer/(?P<referred_by>\d+)$', 'index'),


)
