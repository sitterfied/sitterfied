# Create your views here.
from django.contrib.auth import login as auth_login
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect


from itertools import chain
import json
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to, ajax_request, JsonResponse

from django.views.decorators.http import require_POST

from django.template.loader import render_to_string

from django.http import HttpResponseRedirect

from ecl_facebook import Facebook

from signup import RegistrationView

from rest_framework.renderers import JSONRenderer
from api import ParentSerializer, SitterSerializer, UserSerializer, ChildSerializer, BookingSerializer
from api import UserViewSet, SitterViewSet, ParentViewSet, GroupSerializer

from .models import User, Sitter, Parent, Group, Child
from .utils import send_html_email
from django.contrib.auth.forms import AuthenticationForm
from .forms import SitterRegisterForm, ParentRegisterForm, ChildForm, GroupsForm

UPLOADCARE_PUBLIC_KEY = settings.UPLOADCARE['pub_key']

class HttpResponseUnauthorized(HttpResponse):
    status_code = 401


def get_user_json(user):
    if hasattr(user, 'sitter'):
        user_model = Sitter.objects
        seralizer = SitterSerializer

    elif hasattr(user, 'parent'):
        user_model = Parent.objects.prefetch_related('children', 'children__special_needs')
        seralizer = ParentSerializer

    classed_user = user_model.select_related('settings').prefetch_related('bookings',
                                                                          'sitter_teams',
                                                                          'bookmarks',
                                                                          'friends',
                                                                          'languages',
                                                                          'sitter_groups',
                                                                          'reviews',
                                                                      ).get(id=user.id)
    serialized = seralizer(classed_user)
    user_json = JSONRenderer().render(serialized.data)
    return user_json

@render_to()
def index(request, referred_by=None):
    form = AuthenticationForm()
    if request.user.is_anonymous():
        return {'TEMPLATE': "landing.html",
                "form": form,}

    user_json = get_user_json(request.user)
    if hasattr(request.user, 'sitter'):
        parent_or_sitter = "Sitter"
    else:
        parent_or_sitter = "Parent"


    return {'user_json':user_json,
            "parent_or_sitter": parent_or_sitter,
            'intercom_activator': '#Intercom',
            "TEMPLATE":"index.html",
            "UPLOADCARE_PUBLIC_KEY": UPLOADCARE_PUBLIC_KEY,
            "INTERCOM_APP_ID": settings.INTERCOM_APP_ID,
            "first_time": request.GET.get("first_time", "")
    }

@render_to()
def onboarding2(request):
    ChildFormSet = inlineformset_factory(Parent, Child, form=ChildForm, extra=1)
    if request.method == "POST":
        if request.POST["parent_or_sitter"] == "sitter":
            form = SitterRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect("onboarding3")
            else:
                return {'TEMPLATE': "onboardingsitter.html",
                        "UPLOADCARE_PUBLIC_KEY": UPLOADCARE_PUBLIC_KEY, "form":form}
        elif request.POST["parent_or_sitter"] == "parent":
            form = ParentRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                formset = ChildFormSet(request.POST, instance=user.parent)
                if formset.is_valid():
                    formset.save()
                    auth_login(request, user)
                    return redirect("onboarding3")
            else:
                formset = ChildFormSet(request.POST)
                return {'TEMPLATE': "onboardingparent.html",
                        "UPLOADCARE_PUBLIC_KEY": UPLOADCARE_PUBLIC_KEY, "form":form, "formset":formset}

    if request.method == "GET":
        parent_or_sitter = request.GET.get('parent_or_sitter', "parent")
        if parent_or_sitter.lower() == "sitter":
            form = SitterRegisterForm()
            template = "onboardingsitter.html"
            formset = None
        else:
            form = ParentRegisterForm()
            dummy_user = User()
            formset = ChildFormSet(instance=dummy_user)
            template = "onboardingparent.html"

        return {'TEMPLATE': template,"UPLOADCARE_PUBLIC_KEY": UPLOADCARE_PUBLIC_KEY, "form":form, "formset": formset}



@login_required
@render_to("onboarding3.html")
def onboarding3(request):
    if request.method =="POST":
        form = GroupsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            if hasattr(request.user, 'parent'):
                return redirect("/search?first_time=1")
            else:
                return redirect("/profile")
    form = GroupsForm(instance=request.user)
    return {"form":form}

@render_to("onboarding4.html")
def onboarding4(request):
    return {}

""" Injects values into static pages.

"""
@render_to()
def static_page(request, template):
    obj = {'TEMPLATE': template}

    if not request.user.is_anonymous():
        obj['user_json'] = get_user_json(request.user)
        obj['intercom_activator'] = '#IntercomDefaultWidget'
        obj['INTERCOM_APP_ID'] = settings.INTERCOM_APP_ID

    return obj;



from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import SitterSearchSerializer
from django.db.models import Count, Max

@api_view(['GET'])
def search(request):
    zipcode = request.GET.get('zip', '')
    sitters = Sitter.objects.filter(zip=zipcode).select_related().prefetch_related('reviews',
                                                                                   'languages',
                                                                                   'sitter_groups',
                                                                                   'friends',
                                                                                   'certifications',
                                                                                   'schedlue',
                                                                                   'sitter_teams',
                                                                                   'other_services',
                                                                                   'bookings',
                                                                                   'bookmarks',
                                                                                   'settings').annotate(rehires=Count("booking__parent"))

    serializer = SitterSearchSerializer(sitters, many=True, user=request.user)
    return Response(serializer.data)




@api_view(['GET'])
def network_search(request):
    search_term = request.GET.get('search', '')
    users = [{'label':u.get_full_name(), 'value':u.get_full_name(), "type":"user", "id":u.id} for u in User.objects.filter(Q(first_name__startswith=search_term) | Q(last_name__istartswith=search_term))]
    groups = [{'label':g.name, 'value':g.name, "type":"group", "id":g.id} for g in Group.objects.filter(Q(name__istartswith=search_term))]
    users.extend(groups)
    return Response(users)




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
        auth_login(request, form.get_user())

        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
    else:
        return HttpResponseUnauthorized()
    user_json = get_user_json(request.user)
    return {"user":user_json}

from django.contrib.auth import login

class AjaxRegistrationView(RegistrationView):
    def register(self, request, **cleaned_data):
        new_user = super(AjaxRegistrationView, self).register(request, **cleaned_data)
        new_user.zip = cleaned_data['zipcode']
        new_user.first_name =cleaned_data['first_name']
        new_user.last_name =cleaned_data['last_name']
        new_user.save()
        return new_user


    def form_valid(self, request, form):
        new_user = self.register(request, **form.cleaned_data)

        user_json = get_user_json(new_user)
        response =  {"user":user_json}
        json_response = JsonResponse(response)
        json_response['content-length'] = len(json_response.content)
        return json_response

    def form_invalid(self, form):
        return HttpResponseUnauthorized()


@ajax_request
@login_required
def facebook_import(request):
    user = request.user
    if request.method == "POST":
        token = request.POST['token']
        fb_id = request.POST['id']
        user.facebook_token = token
        user.facebook_id = fb_id
        user.save()
    fb = Facebook(user.facebook_token)
    response = fb.me.friends()
    facebook_ids = [friend['id'] for friend in response['data']]
    friends = User.objects.filter(facebook_id__in=facebook_ids)
    ThroughModel = user.users_in_network.through
    models_to = (ThroughModel(from_user_id=user.id,
                              to_user_id=friend.id) for friend in friends)
    models_frm = (ThroughModel(to_user_id=user.id,
                               from_user_id=friend.id) for friend in friends)
    models = chain(models_to, models_frm)
    ThroughModel.objects.bulk_create(models)
    return {}



@ajax_request
@require_POST
def invite_email_submit(request):
    full_name = request.session.get('full_name')
    first_name = request.session.get('first_name')
    interest_id = request.session.get('id')
    personal_message = request.POST['personal_message']
    emails = [email.strip() for email in request.POST.get('email').split(',') if email]

    text = html = render_to_string("invitation_email.html",
                                   {'inviter_first_name':first_name,
                                    'inviter_full_name':full_name,
                                    'personal_message':personal_message,
                                    'signup_url': ComingSoonInterest.static_invite_url(interest_id),
                                    'full_static_url': request.build_absolute_uri(settings.STATIC_URL),
                                    })

    for email in emails:
        send_html_email("You've been invited to Sitterfied", "hello@sitterfied.com", email, text, html)

    return {}





@render_to('unsubscribe.html')
def unsubscribe(request):
    email = request.GET.get('email')
    EmailBlacklist.objects.get_or_create(email=email)
    return {'email':email}

@render_to('cancel_unsubscribe.html')
def cancel_unsubscribe(request):
    email = request.GET.get('email')
    try:
        e = EmailBlacklist.objects.get(email=email)
        e.delete()
    except:
        pass
    return {'email':email}


from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist

class StaticView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(StaticView, self).get_context_data(**kwargs)
        context['full_static_url'] = self.request.build_absolute_uri(settings.STATIC_URL)
        return context
