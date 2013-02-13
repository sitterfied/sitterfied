from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.


from django.contrib.auth.models import AbstractUser


class User(TimeStampedModel, AbstractUser):
    pass

PARENTING_CHOICES=(
    ('s', 'sitter'),
    ('p', 'parent')
    )

class ComingSoonInterest(TimeStampedModel):
    parent_or_sitter = models.CharField(blank=False, max_length=1, choices=PARENTING_CHOICES)
    name  = models.CharField(max_length=80)
    email = models.EmailField()

    def __unicode__(self):
        return self.name
