# Create your views here.
from time import sleep
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from annoying.decorators import render_to, ajax_request

from django.views.decorators.http import require_POST

from django.template.loader import render_to_string

from django.http import HttpResponseRedirect


@render_to('home.html')
def index(request, referred_by=None):
    return {}


#invite tracking
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



#email
def send_html_email(subject, frm, address, text, html):
    try:
        EmailBlacklist.objects.get(email=address)
        return
    except:
        pass
    msg = EmailMultiAlternatives(subject, text, frm, [address])
    msg.attach_alternative(html, "text/html")
    msg.send()



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
