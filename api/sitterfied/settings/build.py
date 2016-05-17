# -*- coding: utf-8 -*-
"""
File used in build process that specifies temp values necessary for running
management tasks such as collectstatic.

"""
import random
import string

from base import *


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


TWILIO_ACCOUNT_SID = random_string(34)
TWILIO_AUTH_TOKEN = random_string(32)
TWILIO_DEFAULT_CALLERID = ''

UPLOADCARE = {
    'pub_key': None,
    'secret': None,
    'upload_base_url': None,
}
