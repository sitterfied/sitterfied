# -*- coding: utf-8 -*-
from django.core import validators
from django.db import models
from model_utils.models import TimeStampedModel

from sitterfied.users.models import User
from sitterfied.utils.models import WatchedFieldsMixin


class Sitter(WatchedFieldsMixin, User):
    """
    This model represents a sitter.

    """
    GENDER_FEMALE = 'female'
    GENDER_MALE = 'male'
    GENDERS = (
        (GENDER_MALE, GENDER_MALE),
        (GENDER_FEMALE, GENDER_FEMALE),
    )

    biography = models.TextField(blank=True)
    cats_ok = models.BooleanField(default=True)
    cell = models.CharField(max_length=17, blank=True, unique=True, validators=[
        validators.RegexValidator(
            regex=r'^\+?1?\d{10,15}$',
            message='Phone number must be entered in the format: "+9999999999". Up to 15 digits allowed.')],
        null=True
    )
    certifications = models.ManyToManyField('Certification', blank=True)
    current_student = models.BooleanField(default=False)
    dob = models.DateField(blank=False)
    dogs_ok = models.BooleanField(default=True)
    extra_exp = models.TextField(blank=True, default='', null=True)
    gender = models.CharField(max_length=10, choices=GENDERS, default=GENDER_FEMALE)
    has_drivers_licence = models.BooleanField(default=False)
    highest_education = models.CharField(max_length=50, blank=True, default='', null=True)
    id_verified = models.BooleanField(default=False)
    infant_exp = models.SmallIntegerField(blank=True)
    last_school = models.CharField(max_length=50, blank=True, default='', null=True)
    major = models.CharField(max_length=50, blank=True, default='', null=True)
    occupation = models.CharField(max_length=50, blank=True, default='', null=True)
    one_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2)
    one_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2)
    other_animals_ok = models.BooleanField(default=True)
    other_services = models.ManyToManyField('OtherService', blank=True)
    pre_teen_exp = models.SmallIntegerField(blank=True)
    preschool_exp = models.SmallIntegerField(blank=True)
    school_age_exp = models.SmallIntegerField(blank=True)
    sick = models.BooleanField(default=True)
    smoker = models.BooleanField(default=False)
    smokers_ok = models.BooleanField(default=True)
    special_needs_exp = models.BooleanField(default=True)
    teen_exp = models.SmallIntegerField(blank=True)
    three_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    three_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    toddler_exp = models.SmallIntegerField(blank=True)
    total_exp = models.SmallIntegerField()
    travel_distance = models.PositiveIntegerField(default=10, validators=[validators.MinValueValidator(1)])
    two_child_max_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    two_child_min_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    will_transport = models.BooleanField(default=True)

    class Meta:
        app_label = 'app'
        verbose_name = 'Sitter'


class SitterReview(TimeStampedModel):
    """
    Sitter review model

    """
    parent = models.ForeignKey('Parent', related_name='reviews')
    recommended = models.BooleanField(default=False)
    rehire = models.BooleanField(default=False)
    review = models.TextField(blank=True)
    sitter = models.ForeignKey('Sitter', related_name='reviews')

    class Meta:
        app_label = 'app'
        unique_together = ('parent', 'sitter',)
