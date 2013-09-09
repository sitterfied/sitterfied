from .models import Settings, SitterReview, User, Booking, booking_accepted, booking_declined, booking_canceled


from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from sms import client as twilio_client
from sms import sitterfied_number

from .utils import send_html_email

#mutual events
@receiver(post_save, sender=User)
def friend_joined(sender, **kwargs):
    created = kwargs.get('created', False)

def groups_added():
    pass

#parent events
@receiver(booking_accepted)
def booking_request_accepted(sender, sitter=None, **kwargs):
    parent = sender.parent
    settings = parent.settings

    if settings.email_booking_accepted_denied:

        text = html = render_to_string("email/booking/booking_request_accepted.html",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        send_html_email("Your booking request has been accepted", "hello@sitterfied.com", parent.email, text, html)

    if settings.mobile_booking_accepted_denied:
        sms = render_to_string("email/booking/booking_request_accepted.sms",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        twilio_client.sms.messages.create(body=sms, to=parent.cell, from_=sitterfied_number)

@receiver(booking_declined)
def booking_request_declined(sender, sitter=None,  **kwargs):
    parent = sender.parent
    settings = parent.settings

    if settings.email_booking_accepted_denied:
        text = html = render_to_string("email/booking/booking_request_declined.html",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        send_html_email("Your booking request has been declined", "hello@sitterfied.com", parent.email, text, html)

    if settings.mobile_booking_accepted_denied:
        sms = render_to_string("email/booking/booking_request_declined.sms",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        twilio_client.sms.messages.create(body=sms, to=parent.cell, from_=sitterfied_number)


@receiver(booking_canceled)
def booking_request_canceled(sender, **kwargs):
    parent = sender.parent
    settings = parent.settings
    sitter = sender.accepted_sitter
    if settings.email_booking_accepted_denied:
        text = html = render_to_string("email/booking/booking_request_canceled.html",
                                       {'first_name':parent.first_name,
                                       })

        send_html_email("Your booking request has been cancled", "hello@sitterfied.com", parent.email, text, html)

    if settings.mobile_booking_accepted_denied:
        sms = render_to_string("email/booking/booking_request_canceled.sms",{})
        twilio_client.sms.messages.create(body=sms, to=parent.cell, from_=sitterfied_number)



    if not sitter:
        return

    settings = sitter.settings
    if settings.email_booking_accepted_denied:
        text = html = render_to_string("email/booking/booking_request_cancled.html",
                                       {'first_name':sitter.first_name,
                                       })

        send_html_email("Your booking request has been cancled", "hello@sitterfied.com", sitter.email, text, html)

    if settings.mobile_booking_accepted_denied:
        sms = render_to_string("email/booking/booking_request_cancled.sms",{})
        twilio_client.sms.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)


@receiver(m2m_changed, sender=Booking.sitters.through)
def receive_booking_request(sender, pk_set=None, instance=None, action=None,  **kwargs):
    if kwargs.get('reverse', False):
        return
    if action == "post_add":
        parent = instance.parent
        email_sitters = instance.sitters.filter(settings__email_booking_request=True).filter(id__in=pk_set)
        text_sitters = instance.sitters.filter(settings__mobile_booking_request=True).filter(id__in=pk_set)
        for sitter in email_sitters:
            text = html = render_to_string("email/booking/booking_request_received.html",
                                           {
                                               'parent_name':parent.get_full_name(),
                                               'first_name':sitter.first_name,

                                           })

            send_html_email("You have recieved a booking request", "hello@sitterfied.com", sitter.email, text, html)


        for sitter in text_sitters:
            sms = render_to_string("email/booking/booking_request_received.sms",{
                'instance': instance
            })
            twilio_client.sms.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)

@receiver(post_save, sender=SitterReview)
def new_review(sender, **kwargs):
    created = kwargs.get('created', False)
    if created:
        sitter = sender.sitter
        settings = sitter.settings
        if settings.mobile_new_review:
            text = html = render_to_string("email/review/new_review.html",
                                           {
                                               'first_name':sitter.first_name,
                                           })

            send_html_email("You have recieved a new review", "hello@sitterfied.com", sitter.email, text, html)

        if settings.email_new_review:
            sms = render_to_string("email/review/new_review.sms",{})
            twilio_client.sms.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)
