# -*- coding: utf-8 -*-
import api
import google
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from .signals import *
from .signup import RegistrationView
from .views import AjaxRegistrationView, StaticView, BraintreeClientTokenView, BraintreeUpdatePaymentDetailView


router = DefaultRouter()
router.register(r'sitters', api.SitterViewSet)
router.register(r'users', api.UserViewSet)
router.register(r'parents', api.ParentViewSet)
router.register(r'settings', api.SettingsViewSet)
router.register(r'certifications', api.CertificationViewSet)
router.register(r'otherservices', api.OtherServiceViewSet)
router.register(r'specialneeds', api.SpecialNeedViewSet)
router.register(r'schedules', api.ScheduleViewSet)
router.register(r'sitterreviews', api.ReviewViewSet)
router.register(r'languages', api.LanguageViewSet)
router.register(r'children', api.ChildrenViewSet)
router.register(r'bookings', api.BookingViewSet)
router.register(r'groups', api.GroupViewSet)


urlpatterns = patterns('app.views',
                       # Examples:
                       url(r'^error/', 'error', name='error'),
                       url(r'^onboarding/$', 'onboarding1', name='onboarding1'),
                       url(r'^onboarding2/$', "onboarding2", name='onboarding2'),
                       url(r'^onboarding3/$', "onboarding3", name='onboarding3'),
                       url(r'^onboarding4/$', "onboarding4", name='onboarding4'),
                       url(r'^facebook_import/', 'facebook_import', name='facebook_import'),
                       url(r'^api/search/$', 'search', name='search'),
                       url(regex=r'^api/braintree_client/$',
                           view=BraintreeClientTokenView.as_view(),
                           name='braintree_client'),
                       url(regex=r'^api/update_payment_method/$',
                           view=BraintreeUpdatePaymentDetailView.as_view(),
                           name='braintree_update_payment_detail_view'),
                       url(r'^api/', include(router.urls)),
                       url(r'^remove_friend', 'remove_friend', name='remove_friend'),
                       url(r'^remove_group', 'remove_group', name='remove_group'),
                       url(r'^add_group', 'add_group', name='add_group'),
                       url(r'^network_search', 'network_search', name='network_search'),
                       url(r'^invite_email_submit/$', 'invite_email_submit', name='invite_email_submit'),
                       url(r'^unsubscribe/$', 'unsubscribe', name='unsubscribe'),
                       url(r'^cancel-unsubscribe/$', 'cancel_unsubscribe', name='cancel_unsubscribe'),
                       url(r'^email/$', StaticView.as_view(template_name='invitation_email.html'), name="email"),
                       url(r'^signup/$', RegistrationView.as_view(), name='signup'),
                       url(r'^googleoauthbegin/$', google.google_oauth_begin, name='googleoauthbegin'),
                       url(r'^oauth2callback/$', google.oauth2callback, name='googlecallback'),
                       url(r'^tos/', 'static_page', kwargs=dict(template='tos.html'), name='tos'),
                       url(r'^privacy/', "static_page", kwargs=dict(template='privacy.html'), name="privacy"),
                       url(r'^CloudHealthCheck/', "cloudhealthcheck", name="cloudhealthcheck"),)

urlpatterns += patterns('',
                        (r'^accounts/', include('registration.backends.default.urls')),
                        url(r'^login/$', 'django.contrib.auth.views.login', name="login", ),
                        url(r'^login-facebook/$', 'app.views.login_facebook', name="login-facebook", ),
                        url(r'^login-ajax/$', 'app.views.login_ajax', name="login-ajax", ),
                        url(r'^signup-ajax/$', AjaxRegistrationView.as_view(), name="signup-ajax", ),
                        url(r'^password_change/$', 'django.contrib.auth.views.password_change', {'post_change_redirect': '/'}, name="password_change", ),
                        url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout", ),
                        url(r'^sms/$', 'app.sms.sms_messages', name="sms_messages"),

                        # Catch Short URLs
                        url(r'^[a-zA-Z0-9]{5}$', 'app.views.short_url'),

                        # Finally our catch all
                        url(r'^.*/$', 'app.views.redirect_next'),
                        url(r'^$', 'app.views.index', name='index'),)
