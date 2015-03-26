# Create your views here.
import operator
from datetime import datetime, time

import facebook
import requests
from annoying.decorators import render_to, ajax_request
from django.conf import settings
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q, Count
from django.forms.models import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from ecl_facebook import Facebook
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from signup import RegistrationView

from sitterfied.app import utils
from sitterfied.app.forms import SitterRegisterForm, ParentRegisterForm, ChildForm, GroupsForm, RequiredFormSet
from sitterfied.app.utils import send_html_email

from sitterfied.children.models import Child
from sitterfied.parents.models import Parent
from sitterfied.parents.serializers import ParentSerializer
from sitterfied.sitters.models import Sitter
from sitterfied.sitters.serializers import SitterSerializer, SitterSearchSerializer
from sitterfied.users.models import User
from sitterfied.utils.models import Group


# Universal params used in all views
view_params = {
    'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID,
    'SIDESWIPE_IO_TOKEN': settings.SIDESWIPE_IO_TOKEN,
    'UPLOADCARE_PUBLIC_KEY': settings.UPLOADCARE['pub_key'],
    'UPLOADCARE_CDN_BASE': settings.UPLOADCARE['upload_base_url'],
}


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401


def get_user_json(request):
    if not hasattr(request, 'user'):
        return None

    if hasattr(request.user, 'sitter'):
        user_model = Sitter.objects
        seralizer = SitterSerializer

    elif hasattr(request.user, 'parent'):
        user_model = Parent.objects.prefetch_related('children', 'children__special_needs')
        seralizer = ParentSerializer
    elif request.user.is_superuser:
        user_model = User.objects
    else:
        return None

    classed_user = user_model \
        .select_related('settings') \
        .prefetch_related('bookings',
                          'sitter_teams',
                          'bookmarks',
                          'friends',
                          'languages',
                          'sitter_groups',
                          'reviews',) \
        .get(id=request.user.id)

    serialized = seralizer(classed_user, context={'request': request})
    user_json = JSONRenderer().render(serialized.data)
    return user_json


@render_to()
def index(request, referred_by=None):
    form = AuthenticationForm()
    form.fields['username'].widget.attrs['placeholder'] = "Email"
    form.fields['password'].widget.attrs['placeholder'] = "Password"

    if not request.user.is_authenticated():
        return dict({'TEMPLATE': 'landing.html', 'form': form}, **view_params)

    if 'next' in request.GET and request.GET['next'] != '':
        return redirect(request.GET['next'])

    user_json = get_user_json(request)
    if hasattr(request.user, 'sitter'):
        parent_or_sitter = "Sitter"
    else:
        parent_or_sitter = "Parent"

    return dict({
        'user_json': user_json,
        "parent_or_sitter": parent_or_sitter,
        'intercom_activator': '#Intercom',
        "TEMPLATE": "index.html",
        "INTERCOM_APP_ID": settings.INTERCOM_APP_ID,
        "first_time": request.GET.get("first_time", "")
    }, **view_params)


def redirect_next(request):
    """Handles redirection based on current authentication status.

    If the user is authenticated, then the index page view handles the request,
    if the user is not authenticated, he is redirected to the landing page and
    the 'next' query string param is added to the url.

    """
    if request.user.is_anonymous():
        return redirect('/?login=true&next=' + request.path)
    else:
        return index(request)


def short_url(request):
    """Handles requests for short URLs.

    Checks the Redis cache for a corresponding long URL keyed to the short code.
    If a long URL is not found, returns a 404. If any error occurs, returns a
    404.

    """
    try:
        long_url = utils.lookup_short_url(request.path[1:])
        if long_url is not None:
            return HttpResponseRedirect(long_url)
        else:
            raise HttpResponseNotFound()
    except:
        return HttpResponseNotFound()


@render_to('onboarding1.html')
def onboarding1(request):
    return view_params


@render_to()
def onboarding2(request):
    ChildFormSet = inlineformset_factory(Parent, Child, form=ChildForm, extra=1, formset=RequiredFormSet)
    if request.method == "POST":
        if request.POST["parent_or_sitter"] == "sitter":
            form = SitterRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                fb_id = request.session.get("FACEBOOK_ID", None)
                fb_token = request.session.get("FACEBOOK_TOKEN", None)
                if fb_id:
                    facebook_import_logic(user, fb_token, fb_id)
                auth_login(request, user)
                return redirect("onboarding3")
            else:
                return dict({'TEMPLATE': "onboardingsitter.html", "form": form}, **view_params)

        elif request.POST["parent_or_sitter"] == "parent":
            form = ParentRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                fb_id = request.session.get("FACEBOOK_ID", None)
                fb_token = request.session.get("FACEBOOK_TOKEN", None)
                if fb_id:
                    facebook_import_logic(user, fb_token, fb_id)

                formset = ChildFormSet(request.POST, instance=user.parent)
                if formset.is_valid():
                    formset.save()
                    auth_login(request, user)
                    return redirect("onboarding3")
            else:
                formset = ChildFormSet(request.POST)
                return dict({'TEMPLATE': 'onboardingparent.html',
                             'form': form,
                             'formset': formset}, **view_params)

    if request.method == "GET":
        fb_id = request.session.get("FACEBOOK_ID", None)
        fb_token = request.session.get("FACEBOOK_TOKEN", None)

        if fb_id:
            graph = facebook.GraphAPI(fb_token)
            me = graph.get_object("me")
            birthday = me.get("birthday", "")
            dob = datetime.strptime(birthday, '%m/%d/%Y') if birthday else ''
            initial = {
                "first_name": me.get('first_name', ""),
                "last_name": me.get('last_name', ""),
                "gender": me.get('gender', ""),
                "email": me.get("email", ""),
                'dob': dob,
            }
        else:
            initial = {}

        parent_or_sitter = request.GET.get('parent_or_sitter', "parent")
        if parent_or_sitter.lower() == "sitter":
            form = SitterRegisterForm(initial=initial)
            template = "onboardingsitter.html"
            formset = None
        else:
            form = ParentRegisterForm(initial=initial)
            dummy_user = User()
            formset = ChildFormSet(instance=dummy_user)
            template = "onboardingparent.html"

        return dict({
            'TEMPLATE': template,
            "form": form,
            "formset": formset}, **view_params)


@login_required
@render_to("onboarding3.html")
def onboarding3(request):
    if request.method == "POST":
        if hasattr(request.user, 'parent'):
            return redirect("/search?first_time=1")
        else:
            return redirect("/profile?first_time=1")
    form = GroupsForm(instance=request.user)
    return dict({"form": form}, **view_params)


@render_to("onboarding4.html")
def onboarding4(request):
    return {}


@render_to()
def static_page(request, template):
    """ Injects values into static pages.

    """
    obj = dict({'TEMPLATE': template}, **view_params)

    if not request.user.is_anonymous():
        obj['user_json'] = get_user_json(request)
        obj['intercom_activator'] = '#IntercomDefaultWidget'
        obj['INTERCOM_APP_ID'] = settings.INTERCOM_APP_ID

    return obj


test_zips = [
    {
        "zip_code": "11207",
        "distance": 0
    },
    {
        "zip_code": "12345",
        "distance": 9.932
    },
]


@api_view(['GET'])
def search(request):
    zipcode = request.GET.get('zip', '')
    start_date = request.GET.get('start_date', '')
    stop_date = request.GET.get('stop_date', '')
    stop_time = request.GET.get('stop_time', '')
    start_time = request.GET.get('start_time', '')
    overnight = request.GET.get('overnight', False)

    sitters = Sitter.objects.select_related().prefetch_related('reviews',
                                                               'languages',
                                                               'sitter_groups',
                                                               'friends',
                                                               'certifications',
                                                               'schedule',
                                                               'sitter_teams',
                                                               'other_services',
                                                               'bookings',
                                                               'bookmarks',
                                                               'settings').annotate(rehires=Count("bookings__parent"))

    if not settings.DEBUG:
        #filter by radius
        response = requests.get("https://redline-redline-zipcode.p.mashape.com/rest/radius.json/%s/50/mile" % zipcode,
                                headers={
                                    "X-Mashape-Authorization": "kCS3vjTPWYHa7JKYwD3LY6bIcxpmgp5r"
                                })
        zipcodes = response.json()['zip_codes']

        #zipcodes = test_zips
        q_list = [Q(zip=z['zip_code'], travel_distance__gte=z['distance']) for z in zipcodes]
        reduced_q = reduce(operator.or_, q_list)

        sitters = sitters.filter(reduced_q)

    #figure out which day we care about
    start_date = datetime.strptime(start_date, "%a, %b %d %Y")
    day = datetime.strftime(start_date, "%a").lower()

    start_time = datetime.strptime(start_time, "%H%M")
    start_time = time(start_time.hour, start_time.minute)

    stop_time = datetime.strptime(stop_time, "%H%M")
    stop_time = time(stop_time.hour, stop_time.minute)

    times = dict(early_morning=time(hour=6), late_morning=time(hour=9),
                 early_afternoon=time(hour=12), late_afternoon=time(hour=15),
                 early_evening=time(hour=18), late_evening=time(hour=21),)

    search_terms = {}
    if overnight:
        stop_date = datetime.strptime(stop_date, "%a, %d %b %Y")
        stop_day = datetime.strftime(stop_date, "%a").lower()
        search_terms["schedule__%s_overnight" % day] = True

        for term, search_time in times.items():
            if start_time <= search_time:
                search_terms[("schedule__%s_" % day) + term] = True
            if search_time <= stop_time:
                search_terms[("schedule__%s_" % stop_day) + term] = True

    else:
        for term, search_time in times.items():
            if start_time <= search_time <= stop_time:
                search_terms[("schedule__%s_" % day) + term] = True

    #filter by availiablity
    sitters = sitters.filter(**search_terms)

    serializer = SitterSearchSerializer(sitters, many=True, user=request.user)
    return Response(serializer.data)


@api_view(['GET'])
def network_search(request):
    search_term = request.GET.get('search', '')

    users = [{
        'label': u.get_full_name(),
        'value': u.get_full_name(),
        "type": "user",
        "id": u.id
    } for u in User.objects.filter(Q(first_name__istartswith=search_term) | Q(last_name__istartswith=search_term))]

    groups = [{'label': g.name, 'value': g.name, "type": "group", "id": g.id} for g in Group.objects.filter(Q(name__istartswith=search_term))]
    users.extend(groups)
    return Response(users)


@api_view(['GET'])
def group_search(request):
    search_term = request.GET.get('search', '')
    groups = [{'label': g.name,
               'value': g.name,
               "type": "group",
               "id": g.id} for g in Group.objects.filter(Q(name__istartswith=search_term))]
    return Response(groups)


def error(request):
    """for testing purposes"""
    raise Exception


@sensitive_post_parameters()
@csrf_protect
@never_cache
@require_POST
@ajax_request
def login_ajax(request,
               authentication_form=AuthenticationForm,
               current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    form = authentication_form(data=request.POST)
    if form.is_valid():
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)

        auth_login(request, form.get_user())

        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
    else:
        return HttpResponseUnauthorized()
    user_json = get_user_json(request)
    return {"user": user_json}


@sensitive_post_parameters()
@csrf_protect
@never_cache
@require_POST
@ajax_request
def login_facebook(request):
    """
    Displays the login form and handles the login action.
    """
    facebook_id = request.POST['id']

    user = authenticate(id=facebook_id)
    if not user:
        request.session["FACEBOOK_ID"] = facebook_id
        request.session["FACEBOOK_TOKEN"] = request.POST['token']

        return HttpResponseUnauthorized()

    auth_login(request, user)
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()

    return {}


class AjaxRegistrationView(RegistrationView):
    def register(self, request, **cleaned_data):
        new_user = super(AjaxRegistrationView, self).register(request, **cleaned_data)
        new_user.zip = cleaned_data['zipcode']
        new_user.first_name = cleaned_data['first_name']
        new_user.last_name = cleaned_data['last_name']
        new_user.save()
        return new_user

    def form_valid(self, request, form):
        self.register(request, **form.cleaned_data)

        user_json = get_user_json(request)
        response = {"user": user_json}
        json_response = JsonResponse(response)
        json_response['content-length'] = len(json_response.content)
        return json_response

    def form_invalid(self, form):
        return HttpResponseUnauthorized()


def facebook_import_logic(user, token, fb_id):
    user.facebook_token = token
    user.facebook_id = fb_id
    user.save()
    fb = Facebook(user.facebook_token)
    response = fb.me.friends()
    facebook_ids = [friend['id'] for friend in response['data']]
    friends = User.objects.filter(facebook_id__in=facebook_ids)
    user.friends.add(*friends)


@ajax_request
@login_required
def facebook_import(request):
    facebook_import_logic(request.user, request.user.facebook_token, request.user.facebook_id)
    return {}


@ajax_request
@require_POST
def invite_email_submit(request):
    full_name = request.session.get('full_name')
    first_name = request.session.get('first_name')
    interest_id = request.session.get('id')
    personal_message = request.POST['personal_message']
    emails = [email.strip() for email in request.POST.get('email').split(',') if email]

    text = html = render_to_string("invitation_email.html", {
        'inviter_first_name': first_name,
        'inviter_full_name': full_name,
        'personal_message': personal_message,
        'signup_url': ComingSoonInterest.static_invite_url(interest_id),
        'full_static_url': request.build_absolute_uri(settings.STATIC_URL),
    })

    for email in emails:
        send_html_email("You've been invited to Sitterfied", "hello@sitterfied.com", email, text, html)

    return {}


@ajax_request
@login_required
@require_POST
def remove_friend(request):
    friend_id = request.POST['friend_id']
    friend = User.objects.get(id=friend_id)
    request.user.friends.remove(friend)
    return {}


@ajax_request
@login_required
@require_POST
def remove_group(request):
    group_id = request.POST['group_id']
    group = Group.objects.get(id=group_id)
    request.user.sitter_groups.remove(group)
    return {}


@ajax_request
@login_required
@require_POST
def add_group(request):
    group_name = request.POST['group_name']
    group, created = Group.objects.get_or_create(name=group_name)
    request.user.sitter_groups.add(group)
    return {"id": group.id, "name": group.name}


@render_to('unsubscribe.html')
def unsubscribe(request):
    email = request.GET.get('email')
    EmailBlacklist.objects.get_or_create(email=email)
    return {'email': email}


@render_to('cancel_unsubscribe.html')
def cancel_unsubscribe(request):
    email = request.GET.get('email')
    try:
        e = EmailBlacklist.objects.get(email=email)
        e.delete()
    except:
        pass
    return {'email': email}


class StaticView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(StaticView, self).get_context_data(**kwargs)
        context['full_static_url'] = self.request.build_absolute_uri(settings.STATIC_URL)
        return context


def cloudhealthcheck(request):
    return HttpResponse()
