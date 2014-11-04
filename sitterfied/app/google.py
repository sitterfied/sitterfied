from oauth2client.client import OAuth2WebServerFlow
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from annoying.decorators import render_to, ajax_request

from sitterfied.users.models import User
from itertools import chain

import requests

client_id = settings.GOOGLE_OAUTH_CLIENT_ID
client_secret = settings.GOOGLE_OAUTH_CLIENT_SECRET
redirect_uri = settings.GOOGLE_OAUTH_REDIRECT_URI

def google_oauth_begin(request):

    flow = OAuth2WebServerFlow(client_id=client_id,
                               client_secret=client_secret,
                               scope='http://www.google.com/m8/feeds',
                               redirect_uri=redirect_uri +'/oauth2callback',
                               access_type='online')
    auth_uri = flow.step1_get_authorize_url()
    return HttpResponseRedirect(auth_uri)

@render_to("oauthcallback.html")
def oauth2callback(request):

    try:
        code = request.GET['code']
        flow = OAuth2WebServerFlow(client_id=client_id,
                                   client_secret=client_secret,
                                   scope='http://www.google.com/m8/feeds',
                                   redirect_uri=redirect_uri +'/oauth2callback',
                                   access_type='online')
        credentials = flow.step2_exchange(code)

        access_token = credentials.access_token
        headers={'Authorization':'OAuth %s' % access_token}
        session = requests.session()
        response = session.get(url='https://www.google.com/m8/feeds/contacts/default/full?max-results=10000', headers=headers)
        xml_string = response.text
        emails = create_google_contacts(xml_string)
        emails.sort()
    except:
        pass

    user = request.user
    friends = User.objects.filter(email__in=emails).exclude(id=request.user.id)
    user.google_imported = True
    user.save()
    user.friends.add(*friends)
    return {}

#in google.py
from atom.http import ProxiedHttpClient #Google contacts use this client

from lxml import etree

class OAuth2Token(object):
    def __init__(self, access_token):
        self.access_token=access_token

    def perform_request(self, *args, **kwargs):
        url = 'http://www.google.com/m8/feeds/contacts/default/full'
        http = ProxiedHttpClient()
        return http.request(
            'GET',
            url,
            headers={
                'Authorization':'OAuth %s' % self.access_token
            }
        )

def create_google_contacts(xml_string):
    emails = []
    response = etree.fromstring((xml_string).encode("utf-8"))
    for entry in response:
        if 'entry' in entry.tag:
            for element in entry:
                if 'email' in element.tag:
                    emails.append(element.items()[1][1].lower())

    return emails
