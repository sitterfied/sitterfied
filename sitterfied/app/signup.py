from django.dispatch import receiver

from registration.models import RegistrationProfile
from registration.signals import user_registered
from registration.backends.default.views import RegistrationView as DjangoRegistrationView


from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site


from forms import RegistrationForm
from models import Parent, Sitter, Settings, Schedlue

class RegistrationView(DjangoRegistrationView):
    form_class = RegistrationForm

    def register(self, request, **cleaned_data):
        """
        Given a username, email address and password, register a new
        user account, which will initially be inactive.

        Along with the new ``User`` object, a new
        ``registration.models.RegistrationProfile`` will be created,
        tied to that ``User``, containing the activation key which
        will be used for this account.

        An email will be sent to the supplied email address; this
        email should contain an activation link. The email will be
        rendered using two templates. See the documentation for
        ``RegistrationProfile.send_activation_email()`` for
        information about these templates and the contexts provided to
        them.

        After the ``User`` and ``RegistrationProfile`` are created and
        the activation email is sent, the signal
        ``registration.signals.user_registered`` will be sent, with
        the new ``User`` as the keyword argument ``user`` and the
        class of this backend as the sender.

        """
        username, email, password, parent_or_sitter = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1'], cleaned_data['parent_or_sitter']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        if parent_or_sitter == "parent":
            model = Parent

        if parent_or_sitter == "sitter":
            model = Sitter
        else:
            raise Exception
        new_user = model.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.is_active = False
        new_user.save()

        registration_profile = RegistrationProfile.objects.create_profile(new_user)
        registration_profile.send_activation_email(site)

        user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user




@receiver(user_registered)
def create_user_settings(sender, user, request, **kwargs):
    if not Settings.objects.filter(user=user).exists():
        Settings.objects.create(user=user)

@receiver(user_registered)
def create_schedlue(sender, user, request, **kwargs):
    if hasattr(user, 'sitter'):
        if not Schedlue.objects.filter(sitter=user).exists():
            Schedlue.objects.create(sitter=user)



from registration.signals import user_activated
from django.contrib.auth import login, authenticate

def login_on_activation(sender, user, request, **kwargs):
    """Logs in the user after activation"""
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

# Registers the function with the django-registration user_activated signal
user_activated.connect(login_on_activation)
