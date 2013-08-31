from .models import Settings, SitterReview, User, Booking, booking_accepted, booking_declined, booking_canceled


from django.db.models.signals import post_save
from django.dispatch import receiver


from sms import client as twilio_client
from sms import sitterfied_number

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

        text = html = render_to_string("booking/booking_request_accepted.html",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        send_html_email("Your booking request has been accepted", "hello@sitterfied.com", parent.email, text, html)

    if settings.mobile_booking_accepted_denied:
        sms = render_to_string("booking/booking_request_accepted.sms",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        twilio_client.sms.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)

@receiver(booking_declined)
def booking_request_declined(sender, sitter=None,  **kwargs):
    parent = sender.parent
    settings = parent.settings

    if settings.email_booking_accepted_denied:
        text = html = render_to_string("booking/booking_request_declined.html",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        send_html_email("Your booking request has been declined", "hello@sitterfied.com", parent.email, text, html)

    if settings.mobile_booking_accepted_denied:
        sms = render_to_string("booking/booking_request_declined.sms",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        twilio_client.sms.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)


@receiver(booking_canceled)
def booking_request_canceled(sender, **kwargs):
    parent = sender.parent
    settings = parent.settings
    sitter = sender.accepted_sitter
    if settings.email_booking_accepted_denied:
        text = html = render_to_string("booking/booking_request_cancled.html",
                                       {'first_name':parent.first_name,
                                       })

        send_html_email("Your booking request has been cancled", "hello@sitterfied.com", parent.email, text, html)

    if settings.mobile_booking_accepted_denied:
        sms = render_to_string("booking/booking_request_cancled.sms",{})
        twilio_client.sms.messages.create(body=sms, to=parent.cell, from_=sitterfied_number)



    if not sitter:
        return

    settings = sitter.settings
    if settings.email_booking_accepted_denied:
        text = html = render_to_string("booking/booking_request_cancled.html",
                                       {'first_name':sitter.first_name,
                                       })

        send_html_email("Your booking request has been cancled", "hello@sitterfied.com", sitter.email, text, html)

    if settings.mobile_booking_accepted_denied:
        sms = render_to_string("booking/booking_request_cancled.sms",{})
        twilio_client.sms.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)


@receiver(post_save, sender=Booking)
def receive_booking_request(sender, created=False, instance=None,  **kwargs):
    if created:
        parent = instance.parent
        email_sitters = instance.sitters.filter(settings__email_booking_request=True)
        text_sitters = instance.sitters.filter(settings__mobile_booking_request=True)
        for sitter in email_sitters:
            text = html = render_to_string("booking/booking_request_received.html",
                                           {
                                               'parent_name':parent.get_full_name(),
                                               'first_name':sitter.first_name,

                                           })

            send_html_email("You have recieved a booking request", "hello@sitterfied.com", sitter.email, text, html)


        for sitter in text_sitters:
            sms = render_to_string("booking/booking_request_received.sms",{})
            twilio_client.sms.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)

@receiver(post_save, sender=SitterReview)
def new_review(sender, **kwargs):
    created = kwargs.get('created', False)
    if created:
        sitter = sender.sitter
        settings = sitter.settings
        if settings.mobile_new_review:
            text = html = render_to_string("review/new_review.html",
                                           {
                                               'first_name':sitter.first_name,
                                           })

            send_html_email("You have recieved a new review", "hello@sitterfied.com", sitter.email, text, html)

        if settings.email_new_review:
            sms = render_to_string("reviews/new_review.sms",{})
            twilio_client.sms.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)
