from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.views.generic.base import TemplateView
from .views import StaticView

urlpatterns = patterns('app.views',
    # Examples:
    url(r'^email_submit/$', 'comingsoon_email_submit', name='comingsoon_email_submit'),
    url(r'^invite_email_submit/$', 'invite_email_submit', name='invite_email_submit'),
    url(r'^$', 'index', name="home"),
    url(r'^refer/(?P<interest_id>\d+)?$', 'referral_tracking', name="referral_tracking"),
    url(r'^about/$', TemplateView.as_view(template_name='howitworks.html'), name="howitworks"),
    url(r'^email/$', StaticView.as_view(template_name='invitation_email.html'), name="email"),
    url(r'^invite/(?P<referred_by>\d+)$', 'index'),

)
