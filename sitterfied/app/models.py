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
    referred_by = models.ForeignKey('self', null=True)

    def __unicode__(self):
        return self.name

    @property
    def first_name(self):
        return self.name.split(" ", 1)[0]

    @property
    def refer_url(self):
        return "/refer/" + str(self.id)

    @staticmethod
    def static_refer_url(id):
        return "/refer/" + str(id)

    @property
    def referrals(self):
        return ComingSoonInterest.objects.filter(refered_by=self)

    @staticmethod
    def static_referrals(id):
        return ComingSoonInterest.objects.filter(refered_by_id=id)
