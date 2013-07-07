from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.views.generic.base import TemplateView
from .views import StaticView
import api

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'sitters', api.SitterViewSet)
router.register(r'parents', api.ParentViewSet)
router.register(r'settings', api.SettingsViewSet)
router.register(r'certifications', api.CertificationViewSet)
router.register(r'schedlues', api.SchedlueViewSet)
router.register(r'sitter_reviews', api.ReviewViewSet)


urlpatterns = patterns('app.views',
    # Examples:
    url(r'^api/', include(router.urls)),
    url(r'^invite_email_submit/$', 'invite_email_submit', name='invite_email_submit'),
    url(r'^unsubscribe/$', 'unsubscribe', name='unsubscribe'),
    url(r'^cancel-unsubscribe/$', 'cancel_unsubscribe', name='cancel_unsubscribe'),
    url(r'^email/$', StaticView.as_view(template_name='invitation_email.html'), name="email"),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name="login", ),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', {'post_change_redirect':'/'}, name="password_change", ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name="logout", ),
    url(r'^.*', 'app.views.index', name='index'),
)
