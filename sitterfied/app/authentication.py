# -*- coding: utf-8 -*-
from sitterfied.parents.models import Parent
from sitterfied.sitters.models import Sitter
from sitterfied.users.models import User


class EmailAuthBackend(object):
    """
    Email Authentication Backend

    Allows a user to sign in using an email/password pair rather than
    a username/password pair.
    """

    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_parent_or_sitter() is 'Parent':
                return Parent.objects.get(pk=user_id)
            elif user.is_parent_or_sitter() is 'Sitter':
                return Sitter.objects.get(pk=user_id)
            else:
                return user
        except User.DoesNotExist:
            return None


class FacebookAuthBackend(object):
    """
    Facebook Authentication Backend

    Allows a user to sign in using a facebook token rather than
    a username/password pair.
    """
    def authenticate(self, id=None):
        try:
            return User.objects.get(facebook_id=id)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_parent_or_sitter() is 'Parent':
                return Parent.objects.get(pk=user_id)
            else:
                return Sitter.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
