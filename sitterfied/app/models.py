from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(TimeStampedModel, AbstractUser):
    home_address = models.ForeignKey('Address')
    phone = models.ForeignKey('Phone')
    parent_info = models.OneToOneField('ParentInfo', null=True)
    sitter_info = models.OneToOneField('SitterInfo', null=True)
    parents_in_network = models.ForeignKey('ParentsInNetwork')
    sitters_in_network = models.ForeignKey('SittersInNetwork')
    invited_by = models.ManyToManyField('self',  symmetrical = 'false') #invited by one and only one user?
    languages_spoken = models.OneToOneField('LanguagesSpoken')
    email = models.EmailField()
    email_settings = models.OneToOneField('EmailSettings')
    mobile_notifications = models.OneToOneField('MobileNotifications')
    membership_status = models.OneToOneField('MembershipStatus')
    membership_join_date = models.DateField(auto_now_add = True)
    membership_exp_date = models.DateField()


class Address(models.Model):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=9)


PHONE_TYPES = (
    ('work', 'Work'),
    ('home', 'Home'),
    ('cell', 'Cell'),
    ('other', 'Other'),
)

class Phone(models.Model):
    phone_type = models.CharField(max_length=5, choices=PHONE_TYPES)
    number = models.CharField(max_length=25)
    primary = models.BooleanField()


class ParentInfo(models.Model):
    service_location = models.ForeignKey('Address')
    child = models.ForeignKey('Child')
    parking = models.OneToOneField('Parking')	
    emergency_phone = models.CharField(max_length=25)
    emergency_contact = models.OneToOneField('Contact')
    physician_contact = models.OneToOneField('Contact')


class SitterInfo(models.Model):
    sitter_profile = OneToOneField('SitterProfile')


class AddedParent(models.Model):
added_by = models.ForeignKey('User')
parent = models.ForeignKey('User')


class AddedSitter(models.Model):
added_by = models.ForeignKey('User')
sitter = models.ForeignKey('User')


class AddedFriend(models.Model):
added_by = models.ForeignKey('User')
friend = models.ForeignKey('User')


class FaveSitter(models.Model):
added_by = models.ForeignKey('User')
fave_sitter = models.ForeignKey('User')


class LanguagesSpoken(models.Model):
    arabic = models.BooleanField()
    bengali = models.BooleanField()
    cantonese = models.BooleanField()
    english = models.BooleanField()
    spanish = models.BooleanField()
    tamil = models.BooleanField()
    turkish = models.BooleanField()
    german = models.BooleanField()


class EmailSettings(models.Model):
    upcoming_booking = models.BooleanField()
    new_review = models.BooleanField()
    new_reference = models.BooleanField()
    new_reference_request = models.BooleanField()


class MobileNotifications(models.Model):
    message_received = models.BooleanField()
    booking_accepted_denied = models.BooleanField()


class MembershipStatus(models.Model):
    level = models.Charfield(max_length=20)


class Child(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    school = models.CharField(max_length=50)
    sitter_instructions = models.TextField()
    special_needs = OneToOneField('SpecialNeeds')
    #allergies = OneToOneField('Allergies')


class SpecialNeeds(models.Model):
    add = models.BooleanField()
    asthma = models.BooleanField()
    behaviour_challenges = models.BooleanField()
    autism = models.BooleanField()
    down_syndrome = models.BooleanField()
    sleep_disorders = models.BooleanField()


class Parking(models.Model):
    parking_area = models.BooleanField()
    parking_for_sitter = models.BooleanField()


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)


class SitterProfile(models.Model):
    biography = models.TextField()
    id_verification = models.OneToOneField('IdVerification')

    live_zip = models.CharField(max_length=9)
    work_zip = models.CharField(max_length=9)

    dob = models.DateField()
    smoker = models.BooleanField()
    will_transport = models.BooleanField()

    total_exp = models.IntegerField()
    infant_exp = models.IntegerField()
    toddler_exp = models.IntegerField()
    preschool_exp = models.IntegerField()
    school_age_exp = models.IntegerField()
    pre_teen_exp = models.IntegerField()
    teen_exp = models.IntegerField()

    highest_education = models.CharField(max_length=50)
    last_school = models.CharField(max_length=50)
    current_student = models.BooleanField()

    certification =  = models.CharField(max_length=50)
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
    general_avail = models.OneToOneField(GeneralAvail)


class GeneralAvail(models.Model):
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


class IdVerification(models.Model):
    id_verified = models.BooleanField()
    id_scan_path = models.FilePathField("/home/blahblah")


class SitterReview
    parent = models.OneToOneField('User')
    sitter  = models.OneToOneField('User')
    recommended = models.BooleanField()
    review =  = models.TextField()


BOOKING_STATUS_CHOICES=(
    ('active',   'Active'),    
    ('pending',  'Pending'),   
    ('completed','Completed'), 
    ('expired',  'Expired'),   
    ('declined', 'Declined'),  
    ('canceled', 'Canceled')    
)

class Booking(models.Model):
    parent = models.OneToOneField('User')
    sitter = models.OneToOneField('User')
    notes = models.TextField()
    respond_by = models.DateTimeField()
    start_date_time = models.DateTimeField()
    stop_date_time = models.DateTimeField()
    location = models.OneToOneField('Address')
    kid_count = models.SmallIntegerField()
    emergency_phone = models.CharField(max_length=25)
    booking_status = models.CharField(blank=False, max_length=10, choices=BOOKING_STATUS_CHOICES)


PARENTING_CHOICES=(
    ('s', 'sitter'),
    ('p', 'parent')
    )

class ComingSoonInterest(TimeStampedModel):
    parent_or_sitter = models.CharField(blank=False, max_length=1, choices=PARENTING_CHOICES)
    name  = models.CharField(max_length=80)
    zip = models.CharField(max_length=9)
    email = models.EmailField()
    referred_by = models.ForeignKey('self', null=True)

    def __unicode__(self):
        return self.name

    @property
    def first_name(self):
        return self.name.split(" ", 1)[0]

    @property
    def invite_url(self):
        return "/invite/" + str(self.id)

    @staticmethod
    def static_invite_url(id):
        return "/invite/" + str(id)

    @property
    def referrals(self):
        return ComingSoonInterest.objects.filter(refered_by=self)

    @staticmethod
    def static_referrals(id):
        return ComingSoonInterest.objects.filter(referred_by_id=id)

class EmailBlacklist(TimeStampedModel):
    email = models.EmailField()

    def __unicode__(self):
        return self.email
