# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from sitterfied.app import api, google
from sitterfied.bookings.views import BookingViewSet
from sitterfied.children.views import ChildViewSet
from sitterfied.integrations import textit, typeform
from sitterfied.parents.views import ParentViewSet
from sitterfied.sitters.views import SitterViewSet
from sitterfied.users.views import UserViewSet

from .signals import *
from .signup import RegistrationView

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'certifications', api.CertificationViewSet)
router.register(r'children', ChildViewSet)
router.register(r'groups', api.GroupViewSet)
router.register(r'languages', api.LanguageViewSet)
router.register(r'otherservices', api.OtherServiceViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'schedules', api.ScheduleViewSet)
router.register(r'settings', api.SettingsViewSet)
router.register(r'specialneeds', api.SpecialNeedViewSet)
router.register(r'sitters', SitterViewSet)
router.register(r'sitterreviews', api.ReviewViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('sitterfied.app.views',
    url(r'^error/', 'error', name='error'),
    url(r'^onboarding/$', 'onboarding1', name='onboarding1'),
    url(r'^onboarding2/$', "onboarding2", name='onboarding2'),
    url(r'^onboarding3/$', "onboarding3", name='onboarding3'),
    url(r'^onboarding4/$', "onboarding4", name='onboarding4'),
    url(r'^facebook_import/', 'facebook_import', name='facebook_import'),
    url(r'^api/integrations/textit/bookings/requests', textit.views.booking_requests, name='textit-booking-requests'),
    url(r'^api/integrations/textit/bookings/tiers', textit.views.booking_tier, name='textit-booking-tier'),
    url(r'^api/integrations/typeform/sitterchoices', typeform.views.sitterchoices, name='typeform-sitterchoices'),
    url(r'^api/search/$', 'search', name='search'),
    url(r'^api/', include(router.urls)),
    url(r'^remove_friend', 'remove_friend', name='remove_friend'),
    url(r'^remove_group', 'remove_group', name='remove_group'),
    url(r'^add_group', 'add_group', name='add_group'),
    url(r'^network_search', 'network_search', name='network_search'),
    url(r'^signup/$', RegistrationView.as_view(), name='signup'),
    url(r'^googleoauthbegin/$', google.google_oauth_begin, name='googleoauthbegin'),
    url(r'^oauth2callback/$', google.oauth2callback, name='googlecallback'),
    url(r'^tos/', 'static_page', kwargs=dict(template='tos.html'), name='tos'),
    url(r'^privacy/', "static_page", kwargs=dict(template='privacy.html'), name="privacy"),
    url(r'^CloudHealthCheck/', "cloudhealthcheck", name="cloudhealthcheck"),)

urlpatterns += patterns('',
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login", ),
    url(r'^login-facebook/$', 'sitterfied.app.views.login_facebook', name="login-facebook", ),
    url(r'^login-ajax/$', 'sitterfied.app.views.login_ajax', name="login-ajax", ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout", ),
    url(r'^sms/$', 'sitterfied.app.sms.sms_messages', name="sms_messages"),
    # Catch Short URLs
    url(r'^[a-zA-Z0-9]{5}$', 'sitterfied.app.views.short_url'),
    # Finally our catch all
    url(r'^.*/$', 'sitterfied.app.views.redirect_next'),
    url(r'^$', 'sitterfied.app.views.index', name='index'),
)
