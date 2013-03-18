# Create your views here.
from time import sleep
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from annoying.decorators import render_to, ajax_request

from django.views.decorators.http import require_POST

from .forms import ComingSoonInterestForm


@render_to('comingsoon.html')
def index(request, referred_by=None):
    return {"referred_by":referred_by}


@csrf_exempt
@ajax_request
@require_POST
def comingsoon_email_submit(request):
    form = ComingSoonInterestForm(request.POST)
    if form.is_valid():
        coming_soon_interest = form.save()
        return {'id':coming_soon_interest.id}
    else:
        return HttpResponse(status=400)

@csrf_exempt
@ajax_request
@require_POST
def invite_email_submit(request):
    emails = request.POST.getlist('email')
    emails = [email for email in emails if email != ""]
    send_mail('Sitterfied!', 'Sitterfied is great.', 'sitterfied@sitterfied.com',
              emails, fail_silently=True)
    return {}

@render_to('referraltracking.html')
def referral_tracking(request):
    return {}
