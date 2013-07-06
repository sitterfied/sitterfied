from django.db import models
from django.db.models.signals import post_save

from model_utils.models import TimeStampedModel
# Create your models here.

from model_utils.fields import StatusField
from model_utils.choices import Choices


from django.contrib.auth.models import AbstractUser
from django_localflavor_us.us_states import STATE_CHOICES

from django_localflavor_us.models import USStateField
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django_localflavor_us\.models\.USStateField"])


from model_utils.managers import InheritanceManager


class User(AbstractUser, TimeStampedModel):
    MEMBERSHIP_STATUS = Choices("Trial", "paid")
    parents_in_network = models.ManyToManyField('Parent', related_name="parents_in_network")
    sitters_in_network = models.ManyToManyField('Sitter', related_name="sitters_in_network")
    invited_by = models.ManyToManyField('self',  symmetrical =False)
    languages = models.ManyToManyField('Language')

    status = models.CharField(blank=False, max_length=10, choices=MEMBERSHIP_STATUS, default="Trial")
    membership_exp_date = models.DateField(null=True)
    settings =  models.OneToOneField('Settings', null=True)

    #objects = InheritanceManager()

    def __unicode__(self):
        return self.get_full_name()


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
    emergency_contact = models.OneToOneField('Contact', related_name="emergencies", null=True, blank=True)
    physician_contact = models.OneToOneField('Contact', related_name="physicians", null=True, blank=True)
    parking_area = models.BooleanField(default=False)
    parking_for_sitter = models.BooleanField(default=False)
    fave_sitters = models.ManyToManyField('Sitter', related_name="favored_by", blank=True)

    class Meta:
         verbose_name = "Parent"

class Sitter(User):
    biography = models.TextField(blank=True)
    id_verified = models.BooleanField(default=False)

    live_zip = models.CharField(max_length=9)
    work_zip = models.CharField(max_length=9)

    dob = models.DateField(blank=False)
    smoker = models.BooleanField(default=True)
    will_transport = models.BooleanField(default=False)

    total_exp = models.SmallIntegerField(default=0)
    infant_exp = models.SmallIntegerField(default=0)
    toddler_exp = models.SmallIntegerField(default=0)
    preschool_exp = models.SmallIntegerField(default=0)
    school_age_exp = models.SmallIntegerField(default=0)
    pre_teen_exp = models.SmallIntegerField(default=0)
    teen_exp = models.SmallIntegerField(default=0)

    highest_education = models.CharField(max_length=50, blank=True)
    last_school = models.CharField(max_length=50, blank=True)
    current_student = models.BooleanField(default=False)

    certification = models.CharField(max_length=50, blank=True)
    other_services = models.CharField(max_length=100, blank=True)

    one_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2)
    one_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2)
    two_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2)
    two_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2)
    three_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2)
    three_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2)

    smokers_ok = models.BooleanField(default=True)
    dogs_ok = models.BooleanField(default=True)
    cats_ok = models.BooleanField(default=True)
    other_animals_ok = models.BooleanField(default=True)

    class Meta:
         verbose_name = "Sitter"


class Language(TimeStampedModel):
    language = models.CharField(max_length=100)

    def __unicode__(self):
        return self.language


class Settings(TimeStampedModel):
    #parent specific
    mobile_booking_accepted_denied = models.BooleanField()

    #sitter specific
    mobile_new_review  = models.BooleanField()
    mobile_booking_request = models.BooleanField()

    mobile_friend_joined = models.BooleanField()
    mobile_groups_added_network = models.BooleanField()
    mobile_upcoming_booking_remind = models.BooleanField()

    #parent specific
    email_booking_accepted_denied = models.BooleanField()

    #sitter specific
    email_new_review  = models.BooleanField()
    email_booking_request = models.BooleanField()

    email_friend_joined = models.BooleanField()
    email_groups_added_network = models.BooleanField()
    email_upcoming_booking_remind = models.BooleanField()

    email_news = models.BooleanField()
    email_blog = models.BooleanField()

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


def create_user_settings(sender, instance, created, **kwargs):
    if created and not Settings.objects.filter(user=instance).exists():
        Settings.objects.create(user=instance)

post_save.connect(create_user_settings, sender=User)
