# -*- coding: utf-8 -*-
import braintree
import re
import time
from datetime import datetime

from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator
from django.db import models
from django.dispatch import Signal
from django.template.loader import render_to_string
from django.utils.functional import cached_property
from intercom import generate_intercom_user_hash
from model_utils.choices import Choices
from model_utils.models import TimeStampedModel
from pyuploadcare.dj import ImageField as UploadcareImageField
from cities_light.models import Region, City

from app.us_states import US_STATES


booking_accepted = Signal(providing_args=['booking'])
booking_declined = Signal(providing_args=['booking'])
booking_canceled = Signal(providing_args=['booking'])


UPLOADS_DIR = 'uploads/{0}/{1.year:04}/{1.month:02}/{1.day:02}/{2}/{3}'


def file_url(name):
    def inner(instance, filename):
        r = re.compile(r'[^\S]')
        filename = r.sub('', filename)
        now = datetime.now()
        timestamp = int(time.time())
        return UPLOADS_DIR.format(name, now, timestamp, filename)
    return inner


class User(AbstractUser, TimeStampedModel):
    objects = UserManager()

    MEMBERSHIP_STATUS = Choices("Trial", "paid")
    users_in_network = models.ManyToManyField('self', blank=True, symmetrical=True)
    friends = models.ManyToManyField('self', blank=True)

    sitter_groups = models.ManyToManyField('Group', blank=True)
    invited_by = models.ManyToManyField('self', symmetrical=False, blank=True)
    languages = models.ManyToManyField('Language', blank=True, related_name="users")
    status = models.CharField(blank=False, max_length=10, choices=MEMBERSHIP_STATUS, default="Trial")
    membership_exp_date = models.DateTimeField(null=True)

    facebook_token = models.CharField(max_length=256, null=True, blank=True)
    facebook_id = models.IntegerField(null=True, blank=True, unique=True)
    google_imported = models.BooleanField(default=False)

    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True, default="")
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(choices=US_STATES, max_length=2, blank=True, default="AL")
    zip = models.CharField(max_length=9, blank=True)  # there is
    timezone = models.CharField(max_length=255, blank=True)
    cell = models.CharField(max_length=12, blank=True)

    avatar = UploadcareImageField(blank=True, manual_crop="174x174 upscale")

    @property
    def avatar_url(self):
        return getattr(self.avatar, 'cdn_url', None)

    @property
    def hash(self):
        if getattr(self, '_hash', None) is None:
            self._hash = generate_intercom_user_hash(self.email)
        return self._hash

    @property
    def profile_completed(self):
        return False

    def __unicode__(self):
        return self.get_full_name()

    def is_parent_or_sitter(self):
        if hasattr(self, 'sitter'):
            return 'Sitter'
        elif hasattr(self, 'parent'):
            return 'Parent'
        else:
            return 'Admin'

    def is_facebook_connected(self):
        return self.facebook_id is not None


class Address(TimeStampedModel):
    user = models.ForeignKey(User)


class Phone(TimeStampedModel):
    PHONE_TYPES = Choices("Work", "Home", "Cell", "Emergency", "Contact", "Other")

    phone_type = models.CharField(max_length=10, choices=PHONE_TYPES, default="work")
    number = models.CharField(max_length=25)
    #TODO: use a unique partial index to ensure that a user only has a single primary
    primary = models.BooleanField()
    user = models.ForeignKey(User)


class Parent(User):
    PAYMENT_OPTIONS = Choices("Paypal", "Credit Card")
    
    emergency_contact_one_name = models.CharField(max_length=128, blank=True)
    emergency_contact_one_phone = models.CharField(max_length=10, blank=True)
    emergency_contact_two_name = models.CharField(max_length=128, blank=True)
    emergency_contact_two_phone = models.CharField(max_length=10, blank=True)
    
    default_payment_method_token = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(max_length=15, choices=PAYMENT_OPTIONS, blank=True)
    billing_address1 = models.CharField(max_length=255, blank=True)
    billing_address2 = models.CharField(max_length=255, blank=True, default="")

    sitter_teams = models.ManyToManyField('Sitter', related_name="sitter_teams", blank=True)
    bookmarks = models.ManyToManyField('Sitter', related_name="bookmarks", blank=True)

    class Meta:
        verbose_name = "Parent"
    
    @property
    def payment_method_type(self):
        if self.default_payment_method_token:
            try:
                payment_method = braintree.PaymentMethod.find(self.default_payment_method_token)
            except braintree.exceptions.not_found_error.NotFoundError:
                return None
            return payment_method.__class__.__name__
    
    @property
    def paypal_email(self):
        return self.get_payment_method_property("email", "PayPalAccount")
    
    @property
    def masked_number(self):
        return self.get_payment_method_property("masked_number", "CreditCard")
    
    @property
    def expiration_month(self):
        return self.get_payment_method_property("expiration_month", "CreditCard")
    
    @property
    def expiration_year(self):
        expiration_year = self.get_payment_method_property("expiration_year", "CreditCard")
        if expiration_year:
            return expiration_year[2:]
        return expiration_year
    
    @property
    def full_billing_address(self):
        address = None
        if self.default_payment_method_token:
            # Search for payment method using token
            try:
                payment_method = braintree.PaymentMethod.find(self.default_payment_method_token)
            except braintree.exceptions.not_found_error.NotFoundError:
                return address
            
            if payment_method.__class__.__name__ == "CreditCard":
                address = "%s, %s %s %s %s" % (
                    payment_method.billing_address.street_address,
                    payment_method.billing_address.extended_address,
                    payment_method.billing_address.locality,
                    payment_method.billing_address.region,
                    payment_method.billing_address.postal_code,
                )
        return address
    
    @property
    def billing_street_address(self):
        return self.get_billing_address_property("street_address")
    
    @property
    def billing_extended_address(self):
        return self.get_billing_address_property("extended_address")
    
    @property
    def billing_locality(self):
        return self.get_billing_address_property("locality")
    
    @property
    def billing_region(self):
        return self.get_billing_address_property("region")
    
    @property
    def billing_postal_code(self):
        return self.get_billing_address_property("postal_code")
    
    def get_payment_method_property(self, property_name, payment_method_class):
        name = None
        if self.default_payment_method_token:
            # Search for payment method using token
            try:
                payment_method = braintree.PaymentMethod.find(self.default_payment_method_token)
            except braintree.exceptions.not_found_error.NotFoundError:
                return name
            
            # Check to see if payment_method is credit card
            if payment_method.__class__.__name__ == payment_method_class:
                name = getattr(payment_method, property_name)
            
        return name
    
    def get_billing_address_property(self, property_name):
        name = None
        if self.default_payment_method_token:
            # Search for payment method using token
            try:
                payment_method = braintree.PaymentMethod.find(self.default_payment_method_token)
            except braintree.exceptions.not_found_error.NotFoundError:
                return name
            
            # Check to see if payment_method is credit card
            if payment_method.__class__.__name__ == "CreditCard":
                billing_address = payment_method.billing_address
                name = getattr(billing_address, property_name)
            
        return name


class Sitter(User):
    biography = models.TextField(blank=True)

    GENDERS = Choices('male', 'female')
    gender = models.CharField(max_length=10, choices=GENDERS, default='female')
    id_verified = models.BooleanField(default=False)

    dob = models.DateTimeField(blank=False, default=datetime.now)
    smoker = models.BooleanField(default=False)
    sick = models.BooleanField(default=True)
    will_transport = models.BooleanField(default=True)

    total_exp = models.SmallIntegerField()
    infant_exp = models.SmallIntegerField(blank=True)
    toddler_exp = models.SmallIntegerField(blank=True)
    preschool_exp = models.SmallIntegerField(blank=True)
    school_age_exp = models.SmallIntegerField(blank=True)
    pre_teen_exp = models.SmallIntegerField(blank=True)
    teen_exp = models.SmallIntegerField(blank=True)

    special_needs_exp = models.BooleanField(default=True)
    extra_exp = models.TextField(blank=True, default="", null=True)

    highest_education = models.CharField(max_length=50, blank=True, default="", null=True)
    last_school = models.CharField(max_length=50, blank=True, default="", null=True)

    major = models.CharField(max_length=50, blank=True, default="", null=True)
    occupation = models.CharField(max_length=50, blank=True, default="", null=True)

    current_student = models.BooleanField(default=False)

    other_services = models.ManyToManyField('OtherService', blank=True)

    one_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2)
    one_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2)
    two_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    two_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    three_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    three_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    smokers_ok = models.BooleanField(default=True)
    dogs_ok = models.BooleanField(default=True)
    cats_ok = models.BooleanField(default=True)
    other_animals_ok = models.BooleanField(default=True)

    has_drivers_licence = models.BooleanField(default=False)
    travel_distance = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1)])

    certifications = models.ManyToManyField("Certification", blank=True)

    class Meta:
        verbose_name = "Sitter"


class Certification(TimeStampedModel):
    certification = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.certification


class OtherService(TimeStampedModel):
    service = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.service


class Language(TimeStampedModel):
    language = models.CharField(max_length=100)

    def __unicode__(self):
        return self.language


class SpecialNeed(TimeStampedModel):
    need = models.CharField(max_length=100)

    def __unicode__(self):
        return self.need


class Settings(TimeStampedModel):
    #parent specific
    user = models.OneToOneField('User', null=True)

    mobile_booking_accepted_denied = models.BooleanField(default=True)

    #sitter specific
    mobile_new_review = models.BooleanField(default=True)
    mobile_booking_request = models.BooleanField(default=True)

    mobile_friend_joined = models.BooleanField(default=True)
    mobile_groups_added_network = models.BooleanField(default=True)
    mobile_upcoming_booking_remind = models.BooleanField(default=True)

    #parent specific
    email_booking_accepted_denied = models.BooleanField(default=True)

    #sitter specific
    email_new_review = models.BooleanField(default=True)
    email_booking_request = models.BooleanField(default=True)

    email_friend_joined = models.BooleanField(default=True)
    email_groups_added_network = models.BooleanField(default=True)
    email_upcoming_booking_remind = models.BooleanField(default=True)

    email_news = models.BooleanField()
    email_blog = models.BooleanField()


class Child(TimeStampedModel):
    parent = models.ForeignKey(Parent, related_name="children")
    name = models.CharField(max_length=50, blank=True, default="")
    dob = models.DateTimeField(blank=True, null=True, default=datetime.now)
    school = models.CharField(max_length=50, blank=True, default="")
    special_needs = models.ManyToManyField(SpecialNeed, blank=True)

    class Meta:
        verbose_name_plural = "children"


class Contact(TimeStampedModel):
    name = models.CharField(max_length=50)
    phone = models.ForeignKey('Phone')


class Schedule(TimeStampedModel):
    sitter = models.OneToOneField(Sitter)

    mon_early_morning = models.BooleanField(default=True)
    tue_early_morning = models.BooleanField(default=True)
    wed_early_morning = models.BooleanField(default=True)
    thu_early_morning = models.BooleanField(default=True)
    fri_early_morning = models.BooleanField(default=True)
    sat_early_morning = models.BooleanField(default=True)
    sun_early_morning = models.BooleanField(default=True)

    mon_late_morning = models.BooleanField(default=True)
    tue_late_morning = models.BooleanField(default=True)
    wed_late_morning = models.BooleanField(default=True)
    thu_late_morning = models.BooleanField(default=True)
    fri_late_morning = models.BooleanField(default=True)
    sat_late_morning = models.BooleanField(default=True)
    sun_late_morning = models.BooleanField(default=True)

    mon_early_afternoon = models.BooleanField(default=True)
    tue_early_afternoon = models.BooleanField(default=True)
    wed_early_afternoon = models.BooleanField(default=True)
    thu_early_afternoon = models.BooleanField(default=True)
    fri_early_afternoon = models.BooleanField(default=True)
    sat_early_afternoon = models.BooleanField(default=True)
    sun_early_afternoon = models.BooleanField(default=True)

    mon_late_afternoon = models.BooleanField(default=True)
    tue_late_afternoon = models.BooleanField(default=True)
    wed_late_afternoon = models.BooleanField(default=True)
    thu_late_afternoon = models.BooleanField(default=True)
    fri_late_afternoon = models.BooleanField(default=True)
    sat_late_afternoon = models.BooleanField(default=True)
    sun_late_afternoon = models.BooleanField(default=True)

    mon_early_evening = models.BooleanField(default=True)
    tue_early_evening = models.BooleanField(default=True)
    wed_early_evening = models.BooleanField(default=True)
    thu_early_evening = models.BooleanField(default=True)
    fri_early_evening = models.BooleanField(default=True)
    sat_early_evening = models.BooleanField(default=True)
    sun_early_evening = models.BooleanField(default=True)

    mon_late_evening = models.BooleanField(default=True)
    tue_late_evening = models.BooleanField(default=True)
    wed_late_evening = models.BooleanField(default=True)
    thu_late_evening = models.BooleanField(default=True)
    fri_late_evening = models.BooleanField(default=True)
    sat_late_evening = models.BooleanField(default=True)
    sun_late_evening = models.BooleanField(default=True)

    mon_overnight = models.BooleanField(default=True)
    tue_overnight = models.BooleanField(default=True)
    wed_overnight = models.BooleanField(default=True)
    thu_overnight = models.BooleanField(default=True)
    fri_overnight = models.BooleanField(default=True)
    sat_overnight = models.BooleanField(default=True)
    sun_overnight = models.BooleanField(default=True)


class SitterReview(TimeStampedModel):
    parent = models.ForeignKey(Parent, related_name="reviews")
    sitter = models.ForeignKey(Sitter, related_name="reviews")
    recommended = models.BooleanField()
    rehire = models.BooleanField()
    review = models.TextField(blank=True)

    class Meta:
        unique_together = ("parent", "sitter")


class Booking(TimeStampedModel):
    BOOKING_STATUS = Choices('Active', 'Pending', 'Completed', 'Expired', 'Declined', 'Canceled', 'Paid',)
    BOOKING_TYPES = Choices('Job', 'Interview', 'Meetup Interview', 'Phone Interview')
    parent = models.ForeignKey(Parent, related_name="bookings")
    sitters = models.ManyToManyField(Sitter, related_name="bookings")
    declined_sitters = models.ManyToManyField(Sitter, blank=True, related_name="declined_bookings")

    notes = models.TextField(blank=True)
    respond_by = models.DateTimeField(blank=True, null=True)
    start_date_time = models.DateTimeField()
    stop_date_time = models.DateTimeField()
    num_children = models.IntegerField(default=1)
    emergency_phone = models.CharField(max_length=12, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(choices=US_STATES, max_length=2, blank=True, default="AL")
    zip = models.CharField(max_length=9, blank=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS, default='Active')
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPES, default='Job')
    accepted_sitter = models.ForeignKey(Sitter, blank=True, null=True)
    overnight = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)

    @cached_property
    def accepted(self):
        return bool(self.accepted_sitter)
    
    @property
    def work_hours(self):
        delta = self.stop_date_time - self.start_date_time
        minutes = delta / 60
        if minutes % 60 == 0:
            return minutes / 60
        return minutes / 60.0

    def accept(self, sitter):
        self.accepted_sitter = sitter
        self.booking_status = 'Accepted'
        self.save()
        booking_accepted.send(sender=self, sitter=sitter)

        if self.booking_type == 'Job':
            reminder = Reminder()
            reminder.booking = self
            reminder.save()

    def decline(self, sitter):
        self.declined_sitters.add(sitter)
        if len(self.declined_sitters.all()) == len(self.sitters.all()):
            self.booking_status = 'Declined'
        self.save()
        booking_declined.send(sender=self, sitter=sitter)

    def cancel(self, parent_or_sitter):
        self.canceled = True
        self.booking_status = 'Canceled'
        self.save()
        if hasattr(self, 'reminder'):
            self.reminder.delete()
        booking_canceled.send(sender=self, cancelled_by=parent_or_sitter)
        
    def send_completed_sms(self):
        """
        Sends a text message to the accepted sitter when a job is completed.
        """
        from app.sms import send_message #Avoid circular imports
        
        sms_template = 'sms/booking/booking_completed_notification.sms'
        sms = render_to_string(sms_template, {
            'hours': self.work_hours,
            'start_time': self.start_date_time.strftime("%l:%M%P"),
            'end_time': self.stop_date_time.strftime("%l:%M%P"),
        })
        send_message(body=sms, to=self.accepted_sitter.cell)
        
    


class IncomingSMSMessage(TimeStampedModel):
    sid = models.CharField(max_length=34)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    date_sent = models.DateTimeField()
    to = models.CharField(max_length=16)
    body = models.CharField(max_length=161)
    status = models.CharField(max_length=12)
    #dealt_with = models.


class Group(TimeStampedModel):
    name = models.CharField(max_length=128, blank=False)

    def __unicode__(self):
        return self.name


class Reminder(TimeStampedModel):
    booking = models.ForeignKey(Booking)
    task_id = models.CharField(max_length=256)


class USManager(models.Manager):
    def get_query_set(self):
        return super(USManager, self).get_query_set().filter(country__name='United States')


class USState(Region):
    objects = USManager()
    
    class Meta:
        proxy = True


class USCity(City):
    objects = USManager()
    
    class Meta:
        proxy = True