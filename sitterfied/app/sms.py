import re
from django.conf import settings

from django_twilio.decorators import twilio_view


from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account


account_sid = settings.TWILIO_ACCOUNT_SID
auth_token  = settings.TWILIO_AUTH_TOKEN
sitterfied_number = settings.TWILIO_DEFAULT_CALLERID


client = TwilioRestClient(account_sid, auth_token)

def send_booking_request(sender, instance, created, **kwargs):
    if not created:
        return
    body = "Babysit from " + instance.booking.start_date_time + "to " + instance.booking.stop_date_time + "? Please text '" + instance.id +":yes' to accept "

    to = instance.sitter.cell
    client.sms.messages.create(body=body,
                               to=to,
                               from_=sitterfied_number)

@twilio_view
def sms_messages(request):
    from_number = request.values.get('From', None)
    try:
        sitter = Sitter.objects.get(cell=from_number)
    except Sitter.DoesNotExist:
        return
    body = request.values.get('body')
    yes = re.search("(\d*):yes", body)
    request_id = yes.groups()[0]
    try:
        booking_request = BookingRequest.objects.get(id=request_id)
        booking_request.sitter_accepted = True
        booking_request.save()
    except BookingRequest.DoesNotExist:
        return

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






from django.db.models.signals import post_save
from .models import BookingRequest
post_save.connect(send_booking_request, sender=BookingRequest)
