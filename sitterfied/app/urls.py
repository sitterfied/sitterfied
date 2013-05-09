from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.views.generic.base import TemplateView
from .views import StaticView

urlpatterns = patterns('app.views',
    # Examples:
    url(r'^$', 'home', name='home'),


    url(r'^invite_email_submit/$', 'invite_email_submit', name='invite_email_submit'),

    url(r'^unsubscribe/$', 'unsubscribe', name='unsubscribe'),
    url(r'^cancel-unsubscribe/$', 'cancel_unsubscribe', name='cancel_unsubscribe'),

    url(r'^email/$', StaticView.as_view(template_name='invitation_email.html'), name="email"),
)
