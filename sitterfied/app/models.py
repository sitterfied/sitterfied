from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.

from model_utils.fields import StatusField
from model_utils.choices import Choices


from django.contrib.auth.models import AbstractUser
from django_localflavor_us.us_states import STATE_CHOICES
from django_localflavor_us.models import USStateField


class User(AbstractUser, TimeStampedModel):
    home_address = models.ForeignKey('Address')
    parents_in_network = models.ManyToManyField('self', symmetrical = 'false')
    sitters_in_network = models.ManyToManyField('self', symmetrical = 'false')
    fave_sitters = models.ManyToManyField('self', symmetrical = 'false')
    friends =  models.ManyToManyField('self')
    invited_by = models.ManyToManyField('self',  symmetrical = 'false')
    email_settings = models.OneToOneField('EmailSettings')
    mobile_settings = models.OneToOneField('MobileSettings')
    membership_status = models.OneToOneField('MembershipStatus')


class Address(TimeStampedModel):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = USStateField()
    zip = models.CharField(max_length=9)  # there is forms.USZipCodeField but no model.USZip..., ComingSoonInterest does not use


PHONE_TYPES = (
    ('work',      'Work'),
    ('home',      'Home'),
    ('cell',      'Cell'),
    ('emergency', 'Emergency'),
    ('contact',   'Contact'),
    ('other',     'Other'),
)

class Phone(TimeStampedModel):
    user = models.ForeignKey('User')
    phone_type = models.CharField(max_length=10, choices=PHONE_TYPES)
    number = models.CharField(max_length=25)
    primary = models.BooleanField()


class ParentInfo(TimeStampedModel):
    user = models.OneToOneField('User')
    emergency_contact = models.OneToOneField('Contact', related_name="emergencies")
    physician_contact = models.OneToOneField('Contact', related_name="physicians")
    parking_area = models.BooleanField()
    parking_for_sitter = models.BooleanField()


class SitterInfo(TimeStampedModel):
    user = models.OneToOneField('User')
    biography = models.TextField()
    id_verification = models.OneToOneField('IdVerification')

    live_zip = models.CharField(max_length=9)
    work_zip = models.CharField(max_length=9)

    dob = models.DateField()
    smoker = models.BooleanField()
    will_transport = models.BooleanField()

    total_exp = models.SmallIntegerField()
    infant_exp = models.SmallIntegerField()
    toddler_exp = models.SmallIntegerField()
    preschool_exp = models.SmallIntegerField()
    school_age_exp = models.SmallIntegerField()
    pre_teen_exp = models.SmallIntegerField()
    teen_exp = models.SmallIntegerField()

    highest_education = models.CharField(max_length=50)
    last_school = models.CharField(max_length=50)
    current_student = models.BooleanField()

    certification = models.CharField(max_length=50)
    other_services = models.CharField(max_length=100)

    one_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2)
    one_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2)
    two_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2)
    two_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2)
    three_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2)
    three_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2)

    smokers_ok = models.BooleanField()
    dogs_ok = models.BooleanField()
    cats_ok = models.BooleanField()
    other_animals_ok = models.BooleanField()
    general_avail = models.OneToOneField('GeneralAvail')


class Languages(TimeStampedModel):
    user = models.ManyToManyField('User')
    language = models.CharField(max_length=100)


class EmailSettings(TimeStampedModel):
    upcoming_booking = models.BooleanField()
    new_review = models.BooleanField()
    new_reference = models.BooleanField()
    new_reference_request = models.BooleanField()


class MobileSettings(TimeStampedModel):
    message_received = models.BooleanField()
    booking_accepted_denied = models.BooleanField()


MEMBERSHIP_STATUS_CHOICES=(
    ('trial', 'trial'),
    ('paid',  'paid')
)


class MembershipStatus(TimeStampedModel):
    status = models.CharField(blank=False, max_length=10, choices=MEMBERSHIP_STATUS_CHOICES)
    membership_exp_date = models.DateField()


class Child(TimeStampedModel):
    parent = models.ForeignKey('ParentInfo')
    name = models.CharField(max_length=50)
    dob = models.DateField()
    school = models.CharField(max_length=50)
    sitter_instructions = models.TextField()
    special_needs = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)


class Contact(TimeStampedModel):
    name = models.CharField(max_length=50)
    phone = models.ForeignKey('Phone')


class GeneralAvail(TimeStampedModel):
    last_updated = models.DateTimeField(auto_now=True)
    mon_avail_start = models.TimeField()
    mon_avail_stop = models.TimeField()
    tue_avail_start = models.TimeField()
    tue_avail_stop = models.TimeField()
    wed_avail_start = models.TimeField()
    wed_avail_stop = models.TimeField()
    thr_avail_start = models.TimeField()
    thr_avail_stop = models.TimeField()
    fri_avail_start = models.TimeField()
    fri_avail_stop = models.TimeField()
    sat_avail_start = models.TimeField()
    sat_avail_stop = models.TimeField()
    sun_avail_start = models.TimeField()
    sun_avail_stop = models.TimeField()


class IdVerification(TimeStampedModel):
    id_verified = models.BooleanField()
    id_scan_path = models.FilePathField("/home/blahblah")  # avatar?


class SitterReview(TimeStampedModel):
    parent = models.ForeignKey('User', related_name="reviewed")
    sitter  = models.ForeignKey('User', related_name="reviews")
    recommended = models.BooleanField()
    review = models.TextField()
    rating = models.SmallIntegerField()

    class Meta:
        unique_together = ("parent", "sitter")


BOOKING_STATUS_CHOICES=(
    ('active',   'Active'),
    ('pending',  'Pending'),
    ('completed','Completed'),
    ('expired',  'Expired'),
    ('declined', 'Declined'),
    ('canceled', 'Canceled')
)

class Booking(TimeStampedModel):
    parent = models.ForeignKey('User', related_name="parent_bookings")
    sitter = models.ForeignKey('User', related_name="sitter_bookings")
    notes = models.TextField()
    respond_by = models.DateTimeField()
    start_date_time = models.DateTimeField()
    stop_date_time = models.DateTimeField()
    child = models.ManyToManyField('Child')
    emergency_phone = models.ForeignKey('Phone')
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default='active')
    location = models.ForeignKey('Address')


PARENTING_CHOICES=(
    ('s', 'sitter'),
    ('p', 'parent')
    )
