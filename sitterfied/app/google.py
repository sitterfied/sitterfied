def google_oauth_begin(request, id):
    request.session['invite_id'] = id

    flow = OAuth2WebServerFlow(client_id='1005442510888.apps.googleusercontent.com',
                               client_secret='aFExwh6yc9oFqYBz0q12HheZ',
                               scope='http://www.google.com/m8/feeds',
                               redirect_uri='http://gaggyl.com/oauth2callback',
                               access_type='online')
    auth_uri = flow.step1_get_authorize_url()
    return HttpResponseRedirect(auth_uri)


@render_to('invite.html')
def oauth2callback(request):
    occurrence_id = request.session['invite_id']
    hour = request.session['hour']
    del request.session['invite_id']
    form = InviteForm()
    occurrence = Occurrence.objects.get(id=occurrence_id)
    gaggyl = occurrence.gaggyl
    emails = None
    try:
        code = request.GET['code']
        flow = OAuth2WebServerFlow(client_id='1005442510888.apps.googleusercontent.com',
                                   client_secret='aFExwh6yc9oFqYBz0q12HheZ',
                                   scope='http://www.google.com/m8/feeds',
                                   redirect_uri='http://gaggyl.com/oauth2callback',
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
    return {'emails':emails,
            'occurrence': occurrence,
            'hour': hour,
            'gaggyl': gaggyl,
            'form': form}

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
