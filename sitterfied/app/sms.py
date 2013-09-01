import re
from django.conf import settings

from django_twilio.decorators import twilio_view


from twilio.rest import TwilioRestClient
from twilio.twiml import Response

from .models import Sitter, Booking


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = settings.TWILIO_ACCOUNT_SID
auth_token  = settings.TWILIO_AUTH_TOKEN
sitterfied_number = settings.TWILIO_DEFAULT_CALLERID


client = TwilioRestClient(account_sid, auth_token)
from django.http import HttpResponse



@twilio_view
def sms_messages(request):
    from_number = request.POST.get('From', None)
    resp = Response()
    if from_number.startswith("+1"):
        from_number = from_number[2:]
    try:
        sitter = Sitter.objects.get(cell=from_number)
    except Sitter.DoesNotExist:
        resp.sms("Sorry, but this cell phone isn't registered")
        return str(resp)
    body = request.POST.get('Body')
    yes = re.search("(\d*):yes", body)
    request_id = yes.groups()[0]
    try:
        booking = Booking.objects.get(id=request_id)
        if booking.accepted_sitter:
            resp.sms("Sorry, but this booking has already been accepted")
            return str(resp)
        booking.accepted_sitter = sitter
        booking.save()
    except Booking.DoesNotExist:
        resp.sms("Sorry, but you've tried to accept a booking that doesnt' exist")
        return str(resp)




#for polling via cronjob
def get_new_messages():
    try:
        most_recent_message = IncomingSMSMessage.objects.all().order_by('-date_created')[0]
        most_recent  = most_recent_message.date_created
        messages = client.sms.messages.list(to=sitterfied_number, after=most_recent)
    except IndexError:
        print "no messages yet"
        messages = client.sms.messages.list(to=sitterfied_number)
    for message in messages:
        new_message = IncomingSMSMessage(**message)
        new_message.save()
