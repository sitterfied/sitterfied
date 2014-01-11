from django.core.mail import EmailMultiAlternatives
from django_mandrill.mail.mandrillmail import MandrillTemplateMail

def send_html_email(subject, frm, address, text, html):
    msg = EmailMultiAlternatives(subject, text, frm, [address])
    msg.attach_alternative(html, "text/html")
    msg.send()

def send_template_email(template_name, message):
    MandrillTemplateMail(template_name, [], message).send()
