from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.views.generic.base import TemplateView
from .views import StaticView
import api

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'sitters', api.SitterViewSet)
router.register(r'users', api.UserViewSet)
router.register(r'parents', api.ParentViewSet)
router.register(r'settings', api.SettingsViewSet)
router.register(r'certifications', api.CertificationViewSet)
router.register(r'other_services', api.OtherServiceViewSet)
router.register(r'schedlues', api.SchedlueViewSet)
router.register(r'sitter_reviews', api.ReviewViewSet)
router.register(r'languages', api.LanguageViewSet)



# Core Django Imports
from django.conf.urls import patterns, url, include

from .signup import RegistrationView

urlpatterns = patterns('app.views',
    # Examples:
    url(r'^error/', 'error', name='error'),
    url(r'^facebook_import/', 'facebook_import', name='facebook_import'),
    url(r'^api/', include(router.urls)),
    url(r'^invite_email_submit/$', 'invite_email_submit', name='invite_email_submit'),
    url(r'^unsubscribe/$', 'unsubscribe', name='unsubscribe'),
    url(r'^cancel-unsubscribe/$', 'cancel_unsubscribe', name='cancel_unsubscribe'),
    url(r'^email/$', StaticView.as_view(template_name='invitation_email.html'), name="email"),
    url(r'^signup/$',RegistrationView.as_view(), name='signup'),

)

urlpatterns += patterns('',
                        (r'^accounts/', include('registration.backends.default.urls')),
                        url(r'^login/$', 'django.contrib.auth.views.login', name="login", ),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', {'post_change_redirect':'/'}, name="password_change", ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name="logout", ),

    url(r'^.*', 'app.views.index', name='index'),
)
