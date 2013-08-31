from .models import Settings, SitterReview, User, Booking, booking_accepted, booking_declined, booking_canceled


from django.db.models.signals import post_save
from django.dispatch import receiver


#mutual events
@receiver(post_save, sender=User)
def friend_joined(sender, **kwargs):
    created = kwargs.get('created', False)

def groups_added():
    pass

#parent events
@receiver(booking_accepted)
def booking_request_accepted(sender, **kwargs):
    parent = sender.parent
    settings = parent.settings
    if settings.email_booking_accepted_denied:
        print "email"
    if settings.mobile_booking_accepted_denied:
        print "mobile"

@receiver(booking_declined)
def booking_request_declined(sender, **kwargs):
    parent = sender.parent
    settings = parent.settings
    if settings.email_booking_accepted_denied:
        print "email"
    if settings.mobile_booking_accepted_denied:
        print "mobile"

@receiver(booking_canceled)
def booking_request_canceled(sender, **kwargs):
    parent = sender.parent
    settings = parent.settings
    if settings.email_booking_accepted_denied:
        print "email"
    if settings.mobile_booking_accepted_denied:
        print "mobile"

    sitter = sender.accepted_sitter
    if not sitter:
        return
    settings = sitter.settings
    if settings.email_booking_accepted_denied:
        print "email"
    if settings.mobile_booking_accepted_denied:
        print "mobile"

@receiver(post_save, sender=Booking)
def receive_booking_request(sender, created=False, instance=None,  **kwargs):
    if created:
        email_sitters = instance.sitters.filter(settings__email_booking_request=True)
        text_sitters = instance.sitters.filter(settings__mobile_booking_request=True)
        for sitter in email_sitters:
            print "send email"
        for sitter in text_sitters:
            print "send text"

@receiver(post_save, sender=SitterReview)
def new_review(sender, **kwargs):
    created = kwargs.get('created', False)
    if created:
        sitter = sender.sitter
        settings = sitter.settings
        if settings.mobile_new_review:
            print "send text"
        if settings.email_new_review:
            print "send email"
