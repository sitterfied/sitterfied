from django.dispatch import receiver

from registration.models import RegistrationProfile
from registration.signals import user_registered
from registration.backends.default.views import RegistrationView as DjangoRegistrationView


from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from django.contrib.auth import login, authenticate

from forms import RegistrationForm
from sitterfied.parents.models import Parent
from sitterfied.schedules.models import Schedule
from sitterfied.sitters.models import Sitter
from sitterfied.users.models import Settings


class RegistrationView(DjangoRegistrationView):
    form_class = RegistrationForm

    def register(self, request, **cleaned_data):
        """
        Given a username, email address and password, register a new
        user account

        """
        username, email, password, parent_or_sitter = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1'], cleaned_data['parent_or_sitter']
        parent_or_sitter = parent_or_sitter.lower()

        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        if parent_or_sitter == "parent":
            model = Parent

        elif parent_or_sitter == "sitter":
            model = Sitter
        else:
            raise Exception
        new_user = model.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        u = authenticate(username=email, password=password)
        login(request, u)


        return new_user



@receiver(user_registered)
def create_user_settings(sender, user, request, **kwargs):
    if not Settings.objects.filter(user=user).exists():
        Settings.objects.create(user=user)

@receiver(user_registered)
def create_schedule(sender, user, request, **kwargs):
    if hasattr(user, 'sitter'):
        if not Schedule.objects.filter(sitter=user).exists():
            Schedule.objects.create(sitter=user)



from registration.signals import user_activated


def login_on_activation(sender, user, request, **kwargs):
    """Logs in the user after activation"""
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

# Registers the function with the django-registration user_activated signal
user_activated.connect(login_on_activation)
