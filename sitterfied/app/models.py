from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.

from model_utils.fields import StatusField
from model_utils.choices import Choices


from django.contrib.auth.models import AbstractUser
from django_localflavor_us.us_states import STATE_CHOICES

from django_localflavor_us.models import USStateField
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django_localflavor_us\.models\.USStateField"])


class User(AbstractUser, TimeStampedModel):
    MEMBERSHIP_STATUS = Choices("Trial", "paid")
    parents_in_network = models.ManyToManyField('Parent')
    sitters_in_network = models.ManyToManyField('Sitter')
    fave_sitters = models.ManyToManyField('Sitter', related_name="favored_by")
    invited_by = models.ManyToManyField('self',  symmetrical = 'false')
    languages = models.ManyToManyField('Language')

    status = models.CharField(blank=False, max_length=10, choices=MEMBERSHIP_STATUS, default="Trial")
    membership_exp_date = models.DateField(null=True)



class Address(TimeStampedModel):
    user = models.ForeignKey(User)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = USStateField()
    zip = models.CharField(max_length=9)  # there is forms.USZipCodeField but no model.USZip..., ComingSoonInterest does not use



class Phone(TimeStampedModel):
    PHONE_TYPES = Choices("Work", "Home", "Cell", "Emergency", "Contact", "Other")

    phone_type = models.CharField(max_length=10, choices=PHONE_TYPES, default="work")
    number = models.CharField(max_length=25)
    #TODO: use a unique partial index to ensure that a user only has a single primary
    primary = models.BooleanField()
    user = models.ForeignKey(User)



class Parent(User):
    emergency_contact = models.OneToOneField('Contact', related_name="emergencies", null=True)
    physician_contact = models.OneToOneField('Contact', related_name="physicians", null=True)
    parking_area = models.BooleanField()
    parking_for_sitter = models.BooleanField()

    class Meta:
         verbose_name = "Parent"

class Sitter(User):
    biography = models.TextField()
    id_verified = models.BooleanField()
    id_scan_path = models.FilePathField("/home/blahblah")  # avatar?


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

    class Meta:
         verbose_name = "Sitter"




class Language(TimeStampedModel):
    language = models.CharField(max_length=100)

    def __unicode__(self):
        return self.language


class EmailSettings(TimeStampedModel):
    user =  models.OneToOneField('User')

    upcoming_booking = models.BooleanField()
    new_review = models.BooleanField()
    new_reference = models.BooleanField()
    new_reference_request = models.BooleanField()


class MobileSettings(TimeStampedModel):
    user =  models.OneToOneField('User')
    message_received = models.BooleanField()
    booking_accepted_denied = models.BooleanField()

class Child(TimeStampedModel):
    parent = models.ForeignKey(Parent)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    school = models.CharField(max_length=50)
    sitter_instructions = models.TextField()
    special_needs = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "children"



class Contact(TimeStampedModel):
    name = models.CharField(max_length=50)
    phone = models.ForeignKey('Phone')


class GeneralAvail(TimeStampedModel):
    sitter = models.OneToOneField(Sitter)
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


class SitterReview(TimeStampedModel):
    parent = models.ForeignKey(Parent)
    sitter  = models.ForeignKey(Sitter)
    recommended = models.BooleanField()
    review = models.TextField()
    rating = models.SmallIntegerField()

    class Meta:
        unique_together = ("parent", "sitter")



class Booking(TimeStampedModel):
    BOOKING_STATUS = Choices('Active', 'Pending', 'Completed', 'Expired', 'Declined', 'Canceled',)
    parent = models.ForeignKey(Parent, related_name="bookings")
    sitter = models.ForeignKey(Sitter, related_name="bookings")
    notes = models.TextField()
    respond_by = models.DateTimeField()
    start_date_time = models.DateTimeField()
    stop_date_time = models.DateTimeField()
    child = models.ManyToManyField('Child')
    emergency_phone = models.ForeignKey('Phone')
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS, default='Active')
    location = models.ForeignKey('Address')
