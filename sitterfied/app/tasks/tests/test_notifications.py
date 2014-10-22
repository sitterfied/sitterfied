# -*- coding: utf-8 -*-
import mock
from hamcrest import *

from sitterfied.app.tasks import notifications

call_args = None


def test_notify_sitters_of_job_requests():
    with mock.patch('app.sms.client') as mock_client:

        def side_effect(*args, **kwargs):
            global call_args
            call_args = kwargs

        mock_client.messages.create.side_effect = side_effect

        notifications.notify_sitters_of_job_request(1, [3])

        mock_client.messages.create.assert_called_once_with(
            body=call_args['body'],
            to=call_args['to'],
            from_=call_args['from_'],
        )

        assert_that(call_args['body'], contains_string('6pm-10pm'))
