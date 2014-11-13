# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch import Signal
from django.utils import timezone
from django.utils.functional import cached_property
from model_utils.models import TimeStampedModel

from sitterfied.app import us_states


booking_accepted = Signal(providing_args=['booking'])
booking_declined = Signal(providing_args=['booking'])
booking_canceled = Signal(providing_args=['booking'])


class Booking(TimeStampedModel):
    """
    Booking model

    """
    BOOKING_STATUS_ACCEPTED = 'accepted'
    BOOKING_STATUS_ACTIVE = 'active'
    BOOKING_STATUS_CANCELED = 'canceled'
    BOOKING_STATUS_COMPLETED = 'completed'
    BOOKING_STATUS_DECLINED = 'declined'
    BOOKING_STATUS_EXPIRED = 'expired'
    BOOKING_STATUS_PENDING = 'pending'
    BOOKING_STATUS = (
        (BOOKING_STATUS_ACCEPTED, BOOKING_STATUS_ACCEPTED),
        (BOOKING_STATUS_ACTIVE, BOOKING_STATUS_ACTIVE),
        (BOOKING_STATUS_CANCELED, BOOKING_STATUS_CANCELED),
        (BOOKING_STATUS_COMPLETED, BOOKING_STATUS_COMPLETED),
        (BOOKING_STATUS_DECLINED, BOOKING_STATUS_DECLINED),
        (BOOKING_STATUS_EXPIRED, BOOKING_STATUS_EXPIRED),
        (BOOKING_STATUS_PENDING, BOOKING_STATUS_PENDING),
    )

    BOOKING_TYPE_JOB = 'job'
    BOOKING_TYPE_MEETUP = 'meetup'
    BOOKING_TYPE_PHONE = 'phone'
    BOOKING_TYPES = (
        (BOOKING_TYPE_JOB, BOOKING_TYPE_JOB),
        (BOOKING_TYPE_MEETUP, BOOKING_TYPE_MEETUP),
        (BOOKING_TYPE_PHONE, BOOKING_TYPE_PHONE),
    )

    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS, default=BOOKING_STATUS_ACTIVE)
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPES, default=BOOKING_TYPE_JOB)
    canceled = models.BooleanField(default=False)
    city = models.CharField(max_length=50, blank=True)
    emergency_phone = models.CharField(max_length=12, blank=True)
    notes = models.TextField(blank=True)
    num_children = models.IntegerField(default=1)
    overnight = models.BooleanField(default=False)
    parent = models.ForeignKey('Parent', related_name='bookings')
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    respond_by = models.DateTimeField(blank=True, null=True)
    sitters = models.ManyToManyField('Sitter', related_name='bookings', through='BookingResponse', blank=True)
    start_date_time = models.DateTimeField()
    state = models.CharField(choices=us_states.US_STATES, max_length=2, blank=True, default='NJ')
    stop_date_time = models.DateTimeField()
    zip = models.CharField(max_length=9, blank=True)

    @cached_property
    def accepted(self):
        return self.booking_status == Booking.BOOKING_STATUS_ACCEPTED

    @cached_property
    def accepted_sitter(self):
        results = self.sitters.filter(responses__booking=self, responses__response=Booking.BOOKING_STATUS_ACCEPTED)
        return results[0] if results.count() == 1 else None

    @property
    def declined_sitters(self):
        return self.sitters.filter(responses__booking=self, responses__response=Booking.BOOKING_STATUS_DECLINED)

    def accept(self, sitter):
        booking_response = sitter.responses.get(booking=self)
        booking_response.response = Booking.BOOKING_STATUS_ACCEPTED
        booking_response.responded_at = timezone.now()
        booking_response.save()

        self.booking_status = Booking.BOOKING_STATUS_ACCEPTED
        self.save()

        booking_accepted.send(sender=self, sitter=sitter)

        if self.booking_type == self.BOOKING_TYPE_JOB:
            reminder = Reminder()
            reminder.booking = self
            reminder.save()

    def decline(self, sitter):
        booking_response = sitter.responses.get(booking=self)
        booking_response.response = Booking.BOOKING_STATUS_DECLINED
        booking_response.responded_at = timezone.now()
        booking_response.save()

        if self.declined_sitters.count() == self.sitters.all().count():
            self.booking_status = Booking.BOOKING_STATUS_DECLINED
            self.save()

        booking_declined.send(sender=self, sitter=sitter)

    def cancel(self, parent_or_sitter):
        self.canceled = True
        self.booking_status = self.BOOKING_STATUS_CANCELED
        self.save()

        # Mark all pending responses as canceled
        self.responses.filter(
            response=Booking.BOOKING_STATUS_PENDING
        ).update(
            response=Booking.BOOKING_STATUS_CANCELED, responded_at=timezone.now())

        # Delete any reminders
        if hasattr(self, 'reminder'):
            for reminder in self.reminders.all():
                reminder.delete()

        booking_canceled.send(sender=self, cancelled_by=parent_or_sitter)

    class Meta:
        app_label = 'app'


class BookingResponse(TimeStampedModel):
    sitter = models.ForeignKey('Sitter', related_name='responses')
    booking = models.ForeignKey(Booking, related_name='responses')
    response = models.CharField(max_length=10, choices=Booking.BOOKING_STATUS, default=Booking.BOOKING_STATUS_PENDING)
    responded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'app'
        db_table = 'app_booking_sitters'
        unique_together = (('booking', 'sitter'))


class Reminder(TimeStampedModel):
    """
    Reminder model

    """
    booking = models.ForeignKey('Booking', related_name='reminders')
    task_id = models.CharField(max_length=256)

    class Meta:
        app_label = 'app'
