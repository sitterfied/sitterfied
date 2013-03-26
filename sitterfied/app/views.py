# Create your views here.
from time import sleep
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from annoying.decorators import render_to, ajax_request

from django.views.decorators.http import require_POST

from .forms import ComingSoonInterestForm
from .models import ComingSoonInterest

from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

from django.http import HttpResponseRedirect

def send_html_email(subject, frm, address, text, html):
    msg = EmailMultiAlternatives(subject, text, frm, [address])
    msg.attach_alternative(html, "text/html")
    msg.send()



@render_to('comingsoon.html')
def index(request, referred_by=None):
    if request.session.get('full_name', False):
        pass #return HttpResponseRedirect("/referrals")
    return {"referred_by":referred_by}


@csrf_exempt
@ajax_request
@require_POST
def comingsoon_email_submit(request):
    form = ComingSoonInterestForm(request.POST)
    if form.is_valid():
        coming_soon_interest = form.save()
        if coming_soon_interest.parent_or_sitter == "s":
            email_template = "welcome_email_sitter.html"
        else:
            email_template = "welcome_email_parent.html"

        text = html = render_to_string(email_template,
                                       {'first_name':coming_soon_interest.first_name,
                                        'signup_url': coming_soon_interest.refer_url,
                                        'full_static_url': request.build_absolute_uri(settings.STATIC_URL),
                                        })

        send_html_email("Welcome to Sitterfied!",
                        "hello@sitterfied.com",
                        coming_soon_interest.email, text, html)
        request.session['full_name'] = coming_soon_interest.name
        request.session['first_name'] = coming_soon_interest.first_name
        request.session['id'] = coming_soon_interest.id


        if coming_soon_interest.referred_by:
            email = coming_soon_interest.referred_by.email
            text = html = render_to_string("referral_signed_up_email.html",
                                       {'invited_full_name':coming_soon_interest.name,
                                        'first_name': coming_soon_interest.referred_by.first_name,
                                        'full_static_url': request.build_absolute_uri(settings.STATIC_URL),
                                        })


            send_html_email("Your friend signed up for Sitterfied!",
                            "hello@sitterfied.com",
                            email, text, html)


        return {'url':coming_soon_interest.refer_url}
    else:
        return HttpResponse(status=400)

@csrf_exempt
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
                                    'signup_url': ComingSoonInterest.static_refer_url(interest_id),
                                    'full_static_url': request.build_absolute_uri(settings.STATIC_URL),
                                    })

    for email in emails:
        send_html_email("You've been invited to Sitterfied!", "hello@sitterfied.com", email, text, html)

    return {}

@render_to('referraltracking.html')
def referral_tracking(request):
    interest_id = request.session.get('id', False)
    if not interest_id:
        return HttpResponseRedirect("/")
    refer_url = ComingSoonInterest.static_refer_url(interest_id)

    referrals = ComingSoonInterest.static_referrals(interest_id)
    if len(referrals) > 5:
        referrals = range(5)
    width = max(len(referrals) * 200, 117)
    left = 6 - len(referrals)
    return {"refer_url":refer_url, "referrals":referrals, 'width':width, 'left':left}


from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist

class StaticView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(StaticView, self).get_context_data(**kwargs)
        context['full_static_url'] = self.request.build_absolute_uri(settings.STATIC_URL)
        return context
