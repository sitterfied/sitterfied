# -*- coding: utf-8 -*-
from mixpanel.tasks import EventTracker, PeopleTracker


def track_login(user):
    PeopleTracker.delay(
        'set',
        {
            'distinct_id': user.id,
            '$first_name': user.first_name,
            '$last_name': user.last_name,
            '$name': user.get_full_name(),
            '$email': user.email,
            '$created': user.created.strftime('%Y-%m-%d %H:%M:%S'),
        }
    )


def track_event(event, event_data=None, user=None):
    event_data = event_data if event_data else {}

    if 'distinct_id' not in event_data and user:
        event_data['distinct_id'] = user.id

    EventTracker.delay(event, event_data)
