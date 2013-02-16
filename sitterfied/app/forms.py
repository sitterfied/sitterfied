from .models import ComingSoonInterest

from django.forms import ModelForm


class ComingSoonInterestForm(ModelForm):

     def __init__(self, *args, **kwargs):
          super(ComingSoonInterestForm, self).__init__(*args, **kwargs)
          self.fields['referred_by'].required = False

     class Meta:
         model = ComingSoonInterest
