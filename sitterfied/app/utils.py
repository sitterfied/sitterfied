# -*- coding: utf-8 -*-
import random
import string

from django.core.mail import EmailMultiAlternatives
from django_mandrill.mail.mandrillmail import MandrillTemplateMail

def send_html_email(subject, frm, address, text, html):
    msg = EmailMultiAlternatives(subject, text, frm, [address])
    msg.attach_alternative(html, "text/html")
    msg.send()

def send_template_email(template_name, message):
    MandrillTemplateMail(template_name, [], message).send()

def generate_short_url_code():
    code = ''
    for i in range(5):
        code += random.choice(string.lowercase + string.uppercase + string.digits)
    return code
