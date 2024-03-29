# -*- coding: utf-8 -*-
import json
import logging
import random
from datetime import timedelta

import requests
from django.conf import settings

from sitterfied.celeryapp import app
from sitterfied.parents.models import Parent
from sitterfied.sitters.models import Sitter
from sitterfied.utils import time
from sitterfied.utils.tasks import acquire_lock

logger = logging.getLogger(__name__)


def format_generic(contacts):
    return [{
        'id': contact.id,
        'name': contact.get_full_name(),
        'email': contact.email,
        'avatar': contact.avatar_url,
    } for contact in contacts]


def format_sitter_team_sitters(sitters):
    return [{
        'id': sitter.id,
        'name': sitter.get_full_name(),
        'email': sitter.email,
        'avatar': sitter.avatar_url,
        'added': sitter.created.strftime('%Y-%m-%d %H:%M:%S'),
    } for sitter in sitters]


def format_suggested_sitters(parent, sitters):
    # Select a parent from the set of mutually shared parent friends
    # between the current parent and the sitter.
    for sitter in sitters:
        shared_parents = parent.friends.filter(
            id__in=sitter.friends.values_list('id', flat=True)
        )
        sitter.selected_parent = random.choice(shared_parents)

    return [{
        'id': sitter.id,
        'name': sitter.get_full_name(),
        'email': sitter.email,
        'avatar': sitter.avatar_url,
        'parent_id': parent.id,
        'parent_name': parent.get_full_name(),
    } for sitter in sitters]


def get_contacts(dry_run=False):
    if not dry_run:
        api_token = settings.KNOWTIFY_API_TOKEN
        if not api_token:
            logger.error(
                'An error occurred\n       ->The Knowtify API token is not set. '
                'Please set the KNOWTIFY_API_TOKEN environment variable.')
            return

    added_since = time.now() - timedelta(days=7)
    contacts = {'contacts': []}

    for parent in Parent.objects.all():
        sitter_team = parent.sitter_teams.all()
        sitter_team_size = sitter_team.count()
        new_sitters = parent.sitter_teams.filter(created__gte=added_since)
        friends = parent.friends.filter(parent__isnull=False)

        data = {
            'name': parent.get_full_name(),
            'email': parent.email,
            'data': {
                'id': parent.id,
                'first_name': parent.first_name,
                'last_name': parent.last_name,
                'city': parent.city,
                'zip': parent.zip,
                'type': 'parent',
                'friends': format_generic(friends),
                'num_friends': len(friends),
                'sitters': format_sitter_team_sitters(sitter_team),
                'sitter_team_size': sitter_team_size,
                'new_sitters': format_sitter_team_sitters(new_sitters),
                'num_sitters_added': new_sitters.count(),
            },
        }

        if sitter_team_size < 4:
            suggested_sitters = list(Sitter.objects.filter(
                friends__in=parent.friends.filter(parent__isnull=False)
            ).distinct().exclude(sitter_teams=parent))

            random.shuffle(suggested_sitters)
            suggested_sitters = suggested_sitters[:3]

            data['data'].update({
                'suggested_sitters': format_suggested_sitters(parent, suggested_sitters),
                'num_suggested_sitters': len(suggested_sitters),
            })
        else:
            data['data'].update({
                'suggested_sitters': [],
                'num_suggested_sitters': 0,
            })

        contacts['contacts'].append(data)

    for sitter in Sitter.objects.filter(sitter_teams__created__gte=added_since):
        new_parents = Parent.objects.filter(sitter_teams=sitter, created__gte=added_since)
        data = {
            'name': sitter.get_full_name(),
            'email': sitter.email,
            'data': {
                'id': sitter.id,
                'first_name': sitter.first_name,
                'last_name': sitter.last_name,
                'city': sitter.city,
                'zip': parent.zip,
                'type': 'sitter',
                'new_parents': format_generic(new_parents),
                'num_new_parents': new_parents.count(),
            },
        }

        contacts['contacts'].append(data)

    output = {'body': contacts}

    if dry_run:
        logger.debug(json.dumps(contacts))
        return

    try:
        response = requests.post(
            'http://www.knowtify.io/api/v1/contacts/upsert',
            data=json.dumps(contacts),
            headers={
                'Authorization': 'Token token="' + api_token + '"',
                'Content-Type': 'application/json',
            },
        )

        output.update({
            'status_code': response.status_code,
            'content': response.content,
        })
    except Exception as ex:
        output.update({'exception': ex.message})


@app.task
def update_knowtify(dry_run=False):
    with acquire_lock('update-knowtify') as acquired:
        if acquired:
            get_contacts(dry_run)
