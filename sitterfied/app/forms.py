from .models import ComingSoonInterest

from django.forms import ModelForm


class ComingSoonInterestForm(ModelForm):
     class Meta:
         model = ComingSoonInterest
