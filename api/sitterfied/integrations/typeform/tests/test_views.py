# -*- coding: utf-8 -*-
import autofixture
import random

from datetime import datetime, timedelta
from hamcrest import assert_that, has_key, is_, none
from rest_framework import reverse, status
from rest_framework.authtoken.models import Token

from sitterfied.integrations.typeform.views import get_sitter_names
from sitterfied.test.testcases import SitterfiedApiTestCase


class TestViews(SitterfiedApiTestCase):

    def setUp(self):
        super(TestViews, self).setUp()

        self.typeform_user = autofixture.create_one('app.User')
        Token.objects.create(user=self.typeform_user)
        self.parent = autofixture.create_one('app.Parent', generate_m2m=False)
        self.sitters = autofixture.create('app.Sitter', count=3, generate_m2m=False)

    def test_integration(self):
        url = reverse.reverse('typeform-sitterchoices')
        data = {
            'created': datetime.now(),
            'email': self.parent.email,
            'token': 'token',
            'Full Name': self.parent.get_full_name(),
            'ID': 'ID',
            'Submit date': datetime.now() + timedelta(minutes=5),
        }

        # Make sure at least one sitter is getting added
        sitter = self.sitters[0]
        data.update({sitter.get_full_name(): sitter.get_full_name()})

        # Now randomize the rest of the sitters
        for sitter in self.sitters[1:]:
            full_name = sitter.get_full_name()
            data.update({full_name: full_name if random.choice([True, False]) else ''})

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.typeform_user.auth_token.key)

        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_204_NO_CONTENT), str(response.data))
        assert_that(response.data, none())

        sitter_names = get_sitter_names(data)
        assert_that(self.parent.sitter_teams.count(), is_(len(sitter_names)))

    def test_no_authentication(self):
        response = self.client.post(reverse.reverse('typeform-sitterchoices'), {}, format='json')
        assert_that(response.status_code, is_(status.HTTP_401_UNAUTHORIZED), str(response.data))

    def test_no_email(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.typeform_user.auth_token.key)

        response = self.client.post(reverse.reverse('typeform-sitterchoices'), {}, format='json')
        assert_that(response.status_code, is_(status.HTTP_400_BAD_REQUEST), str(response.data))
        assert_that(response.data, has_key('no_email'))

    def test_parent_not_found(self):
        url = reverse.reverse('typeform-sitterchoices')
        data = {
            'email': 'parent.not.found@sitterfied.com',
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.typeform_user.auth_token.key)

        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_400_BAD_REQUEST), str(response.data))
        assert_that(response.data, has_key('parent_not_found'))

    def test_no_sitters_in_request(self):
        url = reverse.reverse('typeform-sitterchoices')
        data = {
            'email': self.parent.email,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.typeform_user.auth_token.key)

        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_400_BAD_REQUEST), str(response.data))
        assert_that(response.data, has_key('no_sitters_in_request'))

    def test_sitters_not_found(self):
        url = reverse.reverse('typeform-sitterchoices')
        data = {
            'email': self.parent.email,
            'Random Sitter': 'Random Sitter',
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.typeform_user.auth_token.key)

        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_400_BAD_REQUEST), str(response.data))
        assert_that(response.data, has_key('sitters_not_found'))

    def test_duplicate_sitters_are_ignored(self):
        url = reverse.reverse('typeform-sitterchoices')
        data = {
            'created': datetime.now(),
            'email': self.parent.email,
            'token': 'token',
            'Full Name': self.parent.get_full_name(),
            'ID': 'ID',
            'Submit date': datetime.now() + timedelta(minutes=5),
        }

        # Make sure at least one sitter is getting added
        sitter = self.sitters[0]
        data.update({sitter.get_full_name(): sitter.get_full_name()})

        # Add this sitter to the parent's sitter team so that we have a
        # duplicate in the request
        self.parent.sitter_teams.through.objects.create(
            parent=self.parent, sitter=sitter, source='typeform:{}'.format(data.get('ID'))
        )

        # Now randomize the rest of the sitters
        for sitter in self.sitters[1:]:
            full_name = sitter.get_full_name()
            data.update({full_name: full_name if random.choice([True, False]) else ''})

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.typeform_user.auth_token.key)

        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_204_NO_CONTENT), str(response.data))
        assert_that(response.data, none())

        sitter_names = get_sitter_names(data)
        assert_that(self.parent.sitter_teams.count(), is_(len(sitter_names)))
