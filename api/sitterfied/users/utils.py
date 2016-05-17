# -*- coding: utf-8 -*-
import random
import re
import string

from sitterfied.users.models import User


def get_valid_username(username=None):
    """
    Converts a username with invalid characters to a valid username.

    Checks to see if the username is taken and appends a number to make it
    unique.

    """
    username = username or ''.join(random.choice(string.ascii_letters) for _ in range(12))

    # Remove any leading or trailing whitespace
    username = username.strip()
    # Remove any non-alphanumeric characters
    username = re.sub(r'\W', '', username)

    # If after stripping all invalid characters we are left with an empty
    # string, ask for a new username based on nothing.
    if not username:
        return get_valid_username('')

    stem = username
    suffix = 1

    # Make sure the username doesn't exist already
    while User.objects.filter(username=username).exists():
        # Add a number to the end of the username to make it unique
        username = '{}{}'.format(stem, suffix)
        suffix = suffix + 1

    return username
