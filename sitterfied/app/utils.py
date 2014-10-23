# -*- coding: utf-8 -*-
import random
import string
from datetime import timedelta

from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from redis import Redis


redis_client = Redis.from_url(settings.REDIS_URL + '/2')


def send_html_email(subject, frm, address, text, html):
    msg = EmailMultiAlternatives(subject, text, frm, [address])
    msg.attach_alternative(html, "text/html")
    msg.send()


def send_template_email(template_name, message):
    msg = EmailMessage()
    msg.template_content = message
    msg.template_name = template_name
    msg.send()


def generate_short_url_code(chars=5):
    """Creates a randomized alphanumeric string the specified number of
    characters long.

    """
    code = ''
    for i in range(chars):
        code += random.choice(string.lowercase
                              + string.uppercase
                              + string.digits)
    return code


def lookup_short_url(key):
    """Retrieve a shortened URL from Redis."""
    return redis_client.get(key)


def get_short_url(url, expires=None):
    """Create and persists a shortened URL.

    If :expires is not set, the shortened URL will expire in 7 days.

    """
    ex = expires if expires else timedelta(days=7)
    short_url_code = generate_short_url_code()
    short_url = settings.SHORT_URL + short_url_code
    redis_client.setex(short_url_code, url, ex)
    return short_url
