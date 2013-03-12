from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.views.generic.base import TemplateView


urlpatterns = patterns('app.views',
    # Examples:
    url(r'^email_submit/$', 'comingsoon_email_submit', name='comingsoon_email_submit'),
    url(r'^invite_email_submit/$', 'invite_email_submit', name='invite_email_submit'),
    url(r'^$', 'index'),
    url(r'^about/$', TemplateView.as_view(template_name='howitworks.html'), name="howitworks"),
    url(r'^refer/(?P<referred_by>\d+)$', 'index'),


)
