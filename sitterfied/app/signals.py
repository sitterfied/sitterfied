# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from twilio import TwilioException
from sms import client as twilio_client, sitterfied_number
from utils import generate_short_url_code
from views import redis_client

from .models import Settings, SitterReview, User, Booking, booking_accepted, booking_declined, booking_canceled, Parent, Sitter, Schedule
from .utils import send_html_email, send_template_email, generate_short_url_code


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

    if parent.settings.email_booking_accepted_denied:

        text = html = render_to_string("email/booking/booking_request_accepted.html",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        # TODO: send_html_email("Your booking request has been accepted", "hello@sitterfied.com", parent.email, text, html)

    if parent.settings.mobile_booking_accepted_denied and parent.cell:
        short_url_code = generate_short_url_code()
        short_url = settings.SHORT_URL + short_url_code
        redis_client.set(short_url_code, '/mybookings/upcoming')

        if 'Interview' in sender.booking_type:
            sms_template = 'sms/interview/interview_request_accepted_parent.sms'
        else:
            sms_template = 'sms/booking/booking_request_accepted.sms'

        sms = render_to_string(sms_template, {
            'sitter_name': sitter.first_name,
            'start_date_time': sender.start_date_time,
            'stop_date_time': sender.stop_date_time,
            'short_url': short_url,
        })
        twilio_client.messages.create(body=sms, to=parent.cell, from_=sitterfied_number)
  
    if sitter.settings.email_booking_accepted_denied:
        pass

    if sitter.settings.mobile_booking_accepted_denied and sitter.cell:
        short_url_code = generate_short_url_code()
        short_url = settings.SHORT_URL + short_url_code
        redis_client.set(short_url_code, '/mybookings/upcoming')

        if 'Interview' in sender.booking_type:
            sms_template = 'sms/interview/interview_request_accepted_sitter.sms'
        else:
            sms_template = 'sms/booking/booking_request_accepted_sitter.sms'

        sms = render_to_string(sms_template, {
            'sitter_name': sitter.first_name,
            'short_url': short_url,
        })
        twilio_client.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)

@receiver(booking_declined)
def booking_request_declined(sender, sitter=None, **kwargs):
    parent = sender.parent
    parent_settings = parent.settings

    if parent_settings.email_booking_accepted_denied:
        text = html = render_to_string("email/booking/booking_request_declined.html",
                                       {'sitter_first_name':sitter.first_name,
                                        'sitter_full_name':sitter.get_full_name(),
                                        'booking': sender,
                                        'parent': parent
                                       })

        # TODO: send_html_email("Your booking request has been declined", "hello@sitterfied.com", parent.email, text, html)

    if parent_settings.mobile_booking_accepted_denied and parent.cell:
        if len(sender.declined_sitters.all()) == len(sender.sitters.all()):
            short_url_code = generate_short_url_code()
            short_url = settings.SHORT_URL + short_url_code
            redis_client.set(short_url_code, '/search')

            if 'Interview' in sender.booking_type:
                sms_template = 'sms/interview/interview_request_declined_parent.sms'
            else:
                sms_template = ('sms/booking/booking_request_declined.sms'
                                if len(sender.sitters.all()) == 1
                                else 'sms/booking/booking_request_declined_all.sms')

            sms = render_to_string(sms_template, {
                'sitter_name': sitter.first_name,
                'parent_name': parent.first_name,
                'start_date_time': sender.start_date_time,
                'short_url': short_url,
                'single_sitter_requested': len(sender.sitters.all()) == 1,
            })
            twilio_client.messages.create(body=sms, to=parent.cell, from_=sitterfied_number)

    if sitter.settings.email_booking_accepted_denied:
        pass

    if sitter.settings.mobile_booking_accepted_denied and sitter.cell:
        short_url_code = generate_short_url_code()
        short_url = settings.SHORT_URL + short_url_code
        redis_client.set(short_url_code, '/sitter/' + str(sitter.id) + '/edit/schedule')

        if 'Interview' in sender.booking_type:
            sms_template = 'sms/interview/interview_request_declined_sitter.sms'
        else:
            sms_template = 'sms/booking/booking_request_declined_sitter.sms'

        sms = render_to_string(sms_template, {
            'sitter_name': sitter.first_name,
            'parent_name': parent.first_name,
            'parent_cell': parent.cell,
            'short_url': short_url,
        })
        twilio_client.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)


@receiver(booking_canceled)
def booking_request_canceled(sender, cancelled_by, **kwargs):
    parent = sender.parent
    sitter = sender.accepted_sitter

    if parent.settings.email_booking_accepted_denied:
        text = html = render_to_string("email/booking/booking_request_canceled.html",
                                       {'first_name':parent.first_name,
                                       })

        # TODO: send_html_email("Your booking request has been canceled", "hello@sitterfied.com", parent.email, text, html)

    if parent.settings.mobile_booking_accepted_denied and parent.cell:
        if cancelled_by == sitter:
            short_url_code = generate_short_url_code()
            short_url = settings.SHORT_URL + short_url_code
            redis_client.set(short_url_code, '/search')

            if 'Interview' in sender.booking_type:
                sms_template = 'sms/interview/interview_cancelled_by_sitter_parent_notification.sms'
            else:
                sms_template = 'sms/booking/booking_request_canceled_by_sitter_to_parent.sms'

            sms = render_to_string(sms_template, {
                'sitter_name': sitter.first_name,
                'sitter_contact': sitter.cell if sitter.cell else sitter.email,
                'start_date_time': sender.start_date_time,
                'stop_date_time': sender.stop_date_time,
                'short_url': short_url,
            })
        else:
            if sitter:
                sitter_first_name = sitter.first_name
                sitter_contact_info = sitter.cell if sitter.cell else sitter.email
            else:
                sitter_first_name = None
                sitter_contact_info = None
            
            if 'Interview' in sender.booking_type:
                sms_template = 'sms/interivew/interview_cancelled_by_parent_confirmation.sms'
            else:
                sms_template = 'sms/booking/booking_request_canceled_by_parent.sms'

            sms = render_to_string(sms_template, {
                'sitter_name': sitter_first_name,
                'start_date_time': sender.start_date_time,
                'sitter_contact_info': sitter_contact_info,
            })

        twilio_client.messages.create(body=sms, to=parent.cell, from_=sitterfied_number)

    if sitter:

        if sitter.settings.email_booking_accepted_denied:
            text = html = render_to_string("email/booking/booking_request_canceled.html", {
                'first_name': sitter.first_name,
            })
            # TODO: send_html_email("Your booking request has been canceled", "hello@sitterfied.com", sitter.email, text, html)

        if sitter.settings.mobile_booking_accepted_denied and sitter.cell:
            if cancelled_by == sitter:
                parent_contact_info = parent.cell if parent.cell else parent.email
                
                if 'Interview' in sender.booking_type:
                    sms_template = 'sms/interview/interview_cancelled_by_sitter_confirmation.sms'
                else:
                    sms_template = 'sms/booking/booking_request_canceled_by_sitter.sms'

                sms = render_to_string(sms_template, {
                    'start_date_time': sender.start_date_time,
                    'parent_name': parent.first_name,
                    'parent_contact_info': parent_contact_info,
                })
            else:
                if 'Interview' in sender.booking_type:
                    sms_template = 'sms/interview/interview_cancelled_by_parent_sitter_notification.sms'
                else:
                    sms_template = 'sms/booking/booking_request_canceled_by_parent_to_sitter.sms'

                sms = render_to_string(sms_template, {
                    'parent_name': parent.first_name,
                    'start_date_time': sender.start_date_time,
                    'stop_date_time': sender.stop_date_time,
                })

            twilio_client.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)


@receiver(m2m_changed, sender=Booking.sitters.through)
def receive_booking_request(sender, pk_set=None, instance=None, action=None, **kwargs):
    if kwargs.get('reverse', False):
        return

    if action == "post_add":
        parent = instance.parent
        email_sitters = instance.sitters.filter(settings__email_booking_request=True).filter(id__in=pk_set)
        text_sitters = instance.sitters.filter(settings__mobile_booking_request=True).filter(id__in=pk_set)
        multi_request_suffix = '_multiple' if len(instance.sitters.all()) > 1 else ''

        for sitter in email_sitters:
            """
            *|FULL_NAME|* [URL link to parent's profile page] would like you to
            sit for *|CHILD_1|*, *|CHILD_2|* and *|CHILD_3|* on *|JOB_DATE|* from 
            *|FROM_TIME|* to *|TO_TIME|*.

            The job is located at *|JOB_ADDRESS|*
            
            Go to your bookings page [URL link to sitter's bookings page] to 
            Accept or Decline this job.

            *|FNAME|* added a note- "*|SHOW_NOTE|*"

            You can reach *|FNAME|* by email: *|EMAIL|* or phone: *|MOBILE|*
            """
            message = create_message_base()
            message['subject'] = 'You have a new job request!'
            message['to'] = [create_email_to(sitter.email, sitter.get_full_name())]
            message['global_merge_vars'] = [{
                'FNAME': sitter.first_name,
                'PARENT_NAME': parent.get_full_name(),
                'PARENT_URL': '/profile/' + str(parent.id),
                
            }]
            
            # TODO: send_template_email('', message)

        short_url_code = generate_short_url_code()
        short_url = settings.SHORT_URL + short_url_code
        redis_client.set(short_url_code, '/mybookings/pending')

        for sitter in text_sitters:
            if not sitter.cell:
                continue

            if 'Interview' in instance.booking_type:
                booking_type = instance.booking_type.replace('Interview', '_Interview').lower()
                sms_template = 'sms/interview/{0}_request_to_sitter.sms'.format(booking_type)
            else:
                sms_template = 'sms/booking/booking_request_received{0}.sms'.format(multi_request_suffix)

            booking_date = instance.start_date_time.date()

            sms = render_to_string(sms_template, {
                'sitter_name': sitter.first_name,
                'parent_name': parent.get_full_name(),
                'booking_date': booking_date,
                'start_date_time': instance.start_date_time,
                'stop_date_time': instance.stop_date_time,
                'parent_city': parent.city,
                'short_url': short_url,
                'booking_code': instance.id,
                'num_sitters': len(instance.sitters.all()) - 1,
            })
            twilio_client.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)

        # Notify parent that the job request was sent via email and/or mobile
        if parent.settings.email_booking_accepted_denied:
            pass  # TODO: implement email for parent request sent

        if parent.settings.mobile_booking_accepted_denied:
            if 'Interview' in instance.booking_type:
                sms_template = 'sms/interview/interview_request_parent_confirmation.sms'
            else:
                sms_template = 'sms/booking/booking_request_sent.sms'
            sms = render_to_string(sms_template, {'short_url': short_url})
            twilio_client.messages.create(body=sms, to=parent.cell, from_=sitterfied_number)

@receiver(post_save, sender=SitterReview)
def new_review(sender, instance=None, **kwargs):
    created = kwargs.get('created', False)
    if created:
        sitter = instance.sitter
        if sitter.settings.mobile_new_review:
            text = html = render_to_string("email/review/new_review.html", {'first_name': sitter.first_name})
            # TODO: send_html_email("You have recieved a new review", "hello@sitterfied.com", sitter.email, text, html)

        if sitter.settings.email_new_review and sitter.cell:
            short_url_code = generate_short_url_code()
            short_url = settings.SHORT_URL + short_url_code
            redis_client.set(short_url_code, '/sitter/' + str(sitter.id) + '/edit/reviews/' + str(instance.id))

            sms = render_to_string('sms/review/new_review.sms', {'short_url': short_url})
            twilio_client.messages.create(body=sms, to=sitter.cell, from_=sitterfied_number)


@receiver(post_save, sender=Parent)
def new_settings_parent(sender, instance=None, **kwargs):
    created = kwargs.get('created', False)
    if created:
        Settings.objects.create(user=instance)


@receiver(post_save, sender=Sitter)
def new_settings_sitter(sender, instance=None, **kwargs):
    created = kwargs.get('created', False)
    if created:
        Settings.objects.create(user=instance)


@receiver(post_save, sender=Sitter)
def new_schedule_parent(sender, instance=None, **kwargs):
    created = kwargs.get('created', False)
    if created:
        Schedule.objects.create(sitter=instance)


@receiver(post_save, sender=Sitter)
def new_sitter(sender, instance=None, **kwargs):
    created = kwargs.get('created', False)
    if created:
        message = create_message_base()
        message['subject'] = 'Welcome to Sitterfied!'
        message['to'] = [create_email_to(instance.email, instance.get_full_name())]
        message['global_merge_vars'] = [{'name': 'FNAME', 'content': instance.first_name}]
        send_template_email('welcome-sitter', message)


@receiver(post_save, sender=Parent)
def new_parent(sender, instance=None, **kwargs):
    created = kwargs.get('created', False)
    if created:
        message = create_message_base()
        message['subject'] = 'Welcome to Sitterfied!'
        message['to'] = [create_email_to(instance.email, instance.get_full_name())]
        message['global_merge_vars'] = [{'name': 'FNAME', 'content': instance.first_name}]
        send_template_email('welcome-parent', message)


def create_email_to(email, name):
    return {'email': email, 'name': name}


def create_message_base():
    return {
        'from_email': settings.DEFAULT_FROM_EMAIL,
        'from_name': 'Sitterfied',
        'subject': None,
        'to': None,
        'global_merge_vars': None,
    }
