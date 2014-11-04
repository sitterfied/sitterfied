# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Schedule(TimeStampedModel):
    """
    Schedule model

    """
    sitter = models.OneToOneField('Sitter', unique=True)

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

    class Meta:
        app_label = 'app'
