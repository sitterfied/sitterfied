# Create your views here.
from time import sleep
from itertools import chain
import json
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to, ajax_request

from django.views.decorators.http import require_POST

from django.template.loader import render_to_string

from django.http import HttpResponseRedirect

from ecl_facebook import Facebook


from rest_framework.renderers import JSONRenderer
from api import ParentSerializer, SitterSerializer, UserSerializer, ChildSerializer, BookingSerializer
from api import UserViewSet, SitterViewSet, ParentViewSet

from .models import User, Sitter, Parent, Group

from .utils import send_html_email

UPLOADCARE_PUBLIC_KEY = settings.UPLOADCARE['pub_key']




@login_required
@render_to('index.html')
def index(request, referred_by=None):

    if hasattr(request.user, 'sitter'):
        user_model = Sitter.objects
        parent_or_sitter = "Sitter"
        seralizer = SitterSerializer

    elif hasattr(request.user, 'parent'):
        user_model = Parent.objects.prefetch_related('children', 'children__special_needs')
        parent_or_sitter = "Parent"
        seralizer = ParentSerializer

    classed_user = user_model.select_related('settings').prefetch_related('bookings',
                                                                          'sitter_teams',
                                                                          'bookmarks',
                                                                          'friends',
                                                                          'languages',
                                                                          'sitter_groups',
                                                                          'reviews',
                                                                      ).get(id=request.user.id)
    serialized = seralizer(classed_user)
    user_json = JSONRenderer().render(serialized.data)
    return {'user_json':user_json,
            'parent_or_sitter': parent_or_sitter,
            "UPLOADCARE_PUBLIC_KEY": UPLOADCARE_PUBLIC_KEY
    }

from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import SitterSearchSerializer
from django.db.models import Count, Max

@api_view(['GET'])
def search(request):
    sitters = Sitter.objects.select_related().prefetch_related('reviews',
                                                               'languages',
                                                               'sitter_groups',
                                                               'friends',
                                                               'certifications',
                                                               'schedlue',
                                                               'sitter_teams',
                                                               'other_services',
                                                               'bookings',
                                                               'bookmarks',
                                                               'settings')

    sitters = sitters.annotate(rehires=Count("booking__parent")).all()
    serializer = SitterSearchSerializer(sitters, many=True, user=request.user)
    return Response(serializer.data)




@api_view(['GET'])
def network_search(request):
    search_term = request.GET.get('search', '')
    users = [{'label':u.get_full_name(), 'value':'user'} for u in User.objects.filter(Q(first_name__startswith=search_term) | Q(last_name__startswith=search_term))]
    groups = [{'label':g.name, 'value':'group'} for g in Group.objects.filter(Q(name__startswith=search_term))]
    users.extend(groups)
    return Response(users)




def error(request):
    """for testing purposes"""
    raise Exception


@ajax_request
@login_required
def facebook_import(request):
    user = request.user
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
