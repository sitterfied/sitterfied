# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import celery
import pytz
from django.conf import settings
from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from app.models import Settings, SitterReview, User, Booking, booking_accepted, booking_declined, booking_canceled, Parent, Sitter, Schedule, Reminder
from app.sms import send_message
from app.tasks import notifications, reminders
from app.utils import get_short_url, send_template_email


#mutual events
@receiver(post_save, sender=User)
def friend_joined(sender, **kwargs):
    pass


def groups_added():
    pass


#parent events
@receiver(booking_accepted, dispatch_uid='app.booking.booking_accepted')
def booking_request_accepted(sender, sitter=None, **kwargs):
    parent = sender.parent

    if parent.settings.email_booking_accepted_denied:
        # TODO: send_html_email("Your booking request has been accepted", "hello@sitterfied.com", parent.email, text, html)
        pass

    if parent.settings.mobile_booking_accepted_denied and parent.cell:
        short_url = get_short_url('/mybookings/upcoming')

        if 'Interview' in sender.booking_type:
            sms_template = 'sms/interview/interview_request_accepted_parent.sms'
        else:
            sms_template = 'sms/booking/booking_request_accepted.sms'

        sms = render_to_string(sms_template, {
            'sitter_name': sitter.first_name,
	    'sitter_cell': sitter.cell,
            'start_date_time': sender.start_date_time,
            'stop_date_time': sender.stop_date_time,
            'short_url': short_url,
        })
        send_message(body=sms, to=parent.cell)

    if sitter.settings.email_booking_accepted_denied:
        pass

    if sitter.settings.mobile_booking_accepted_denied and sitter.cell:
        short_url = get_short_url('/mybookings/upcoming')

        if 'Interview' in sender.booking_type:
            sms_template = 'sms/interview/interview_request_accepted_sitter.sms'
        else:
            sms_template = 'sms/booking/booking_request_accepted_sitter.sms'

        sms = render_to_string(sms_template, {
            'sitter_name': sitter.first_name,
	    'parent_name': parent.first_name,
	    'parent_cell': parent.cell,
            'short_url': short_url,
        })
        send_message(body=sms, to=sitter.cell)


@receiver(booking_declined, dispatch_uid='app.booking.booking_declined')
def booking_request_declined(sender, sitter=None, **kwargs):
    parent = sender.parent
    parent_settings = parent.settings

    if parent_settings.email_booking_accepted_denied:
        # TODO: send_html_email("Your booking request has been
        # declined", "hello@sitterfied.com", parent.email, text, html)
        pass

    if parent_settings.mobile_booking_accepted_denied and parent.cell:
        if len(sender.declined_sitters.all()) == len(sender.sitters.all()):
            short_url = get_short_url('/search')

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
            send_message(body=sms, to=parent.cell)

    if sitter.settings.email_booking_accepted_denied:
        pass

    if sitter.settings.mobile_booking_accepted_denied and sitter.cell:
        short_url = get_short_url('/sitter/' + str(sitter.id) + '/edit/schedule')

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
        send_message(body=sms, to=sitter.cell)


@receiver(booking_canceled, dispatch_uid='app.booking.booking_canceled')
def booking_request_canceled(sender, cancelled_by, **kwargs):
    parent = sender.parent
    sitter = sender.accepted_sitter

    if parent.settings.email_booking_accepted_denied:
        # TODO: send_html_email("Your booking request has been
        # canceled", "hello@sitterfied.com", parent.email, text, html)
        pass

    if parent.settings.mobile_booking_accepted_denied and parent.cell:
        if cancelled_by == sitter:
            short_url = get_short_url('/search')

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

        send_message(body=sms, to=parent.cell)

    if sitter:
        if sitter.settings.email_booking_accepted_denied:
            # TODO: send_html_email("Your booking request has been
            # canceled", "hello@sitterfied.com", sitter.email, text,
            # html)
            pass

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

            send_message(body=sms, to=sitter.cell)


@receiver(m2m_changed, sender=Booking.sitters.through)
def receive_booking_request(sender, pk_set=None, instance=None, action=None, **kwargs):
    if kwargs.get('reverse', False):
        return

    if action == "post_add":
        # Queue Celery task for sending parent confirmation
        notifications.notify_parent_of_job_request.s(instance.id).delay()

        # Queue Celery task for sending job requests to sitters
        notifications.notify_sitters_of_job_request.s(instance.id, list(pk_set)).delay()


@receiver(post_save, sender=SitterReview)
def new_review(sender, instance=None, **kwargs):
    created = kwargs.get('created', False)
    if created:
        sitter = instance.sitter
        if sitter.settings.mobile_new_review:
            # TODO: send_html_email("You have recieved a new review",
            # "hello@sitterfied.com", sitter.email, text, html)
            pass

        if sitter.settings.email_new_review and sitter.cell:
            short_url = get_short_url('/sitter/' + str(sitter.id) + '/edit/reviews/' + str(instance.id))

            sms = render_to_string('sms/review/new_review.sms', {'short_url': short_url})
            send_message(body=sms, to=sitter.cell)


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


@receiver(post_save, sender=Reminder)
def reminder_save_handler(*args, **kwargs):
    reminder = kwargs.get('instance')

    if not reminder.task_id:
        first_reminder = settings.JOB_FIRST_REMINDER
        second_reminder = settings.JOB_SECOND_REMINDER
        relief_reminder = settings.JOB_RELIEF_REMINDER

        start_date_time = reminder.booking.start_date_time
        stop_date_time = reminder.booking.stop_date_time
        timezone = pytz.timezone(reminder.booking.parent.timezone)
        delta = start_date_time - datetime.now(timezone)

        if delta.total_seconds() > first_reminder:
            eta = start_date_time - timedelta(seconds=first_reminder)
            reminder_type = 'first'
            seconds = first_reminder
            next_reminders = [
                {
                    'eta': (start_date_time - timedelta(seconds=second_reminder)).strftime('%Y-%m-%d %H:%M:%S'),
                    'reminder_type': 'second',
                    'seconds': second_reminder,
                },
                {
                    'eta': (stop_date_time - timedelta(seconds=relief_reminder)).strftime('%Y-%m-%d %H:%M:%S'),
                    'reminder_type': 'relief',
                    'seconds': relief_reminder,
                },
            ]
        elif delta.total_seconds() > second_reminder:
            eta = start_date_time - timedelta(seconds=second_reminder)
            reminder_type = 'second'
            seconds = second_reminder
            next_reminders = [
                {
                    'eta': (stop_date_time - timedelta(seconds=relief_reminder)).strftime('%Y-%m-%d %H:%M:%S'),
                    'reminder_type': 'relief',
                    'seconds': relief_reminder,
                },
            ]
        else:
            eta = stop_date_time - timedelta(seconds=relief_reminder)
            reminder_type = 'relief'
            seconds = relief_reminder
            next_reminders = []

        if eta:
            result = reminders.send_reminders.apply_async(
                eta=eta.astimezone(timezone),
                kwargs={
                    'id': reminder.id,
                    'reminder_type': reminder_type,
                    'seconds': seconds,
                    'reminders': next_reminders,
                }
            )
            reminder.task_id = result.task_id
            reminder.save()


@receiver(pre_delete, sender=Reminder)
def reminder_del_handler(sender, instance, **kwargs):
    reminder = instance
    if reminder.task_id:
        celery.task.control.revoke(reminder.task_id)


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
