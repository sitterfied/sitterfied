# -*- coding: utf-8 -*-
import random
import string

from autofixture import AutoFixture, generators, get, register
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.db.models.fields import related
from mock import patch


@patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
@patch('sitterfied.app.signals.notifications.notify_sitter_of_job_request.delay')
@patch('sitterfied.app.signals.notifications.notify_parent_of_job_request.delay')
def create_bookings(notify_parent, notify_sitter, get_time_zone, count=1):
    if count == 1:
        return get('app.Booking').create_one()
    return get('app.Booking').create(count)


def phone_number_generator():
    value = u'+1'
    for x in range(10):
        value += random.choice(string.digits)
    return value


class ChildDobGenerator(generators.DateGenerator):
    max_date = datetime.now() - timedelta(365 * 1)
    min_date = datetime.now() - timedelta(365 * 13)


class NameGenerator(generators.Generator):
    first_name_generator = generators.FirstNameGenerator()
    last_name_generator = generators.LastNameGenerator()

    def generate(self):
        first_name = self.first_name_generator.generate()
        last_name = self.last_name_generator.generate()
        return '{} {}'.format(first_name, last_name)


class SitterDobGenerator(generators.DateGenerator):
    max_date = datetime.now() - timedelta(365 * 18)
    min_date = datetime.now() - timedelta(365 * 35)


class UsernameGenerator(generators.StringGenerator):

    def __init__(self, chars=None, max_length=None, min_length=None, *args, **kwargs):
        kwargs['chars'] = chars or string.ascii_lowercase
        kwargs['max_length'] = max_length or 30
        kwargs['min_length'] = min_length or 3

        super(UsernameGenerator, self).__init__(*args, **kwargs)


class BaseFixture(AutoFixture):

    def process_m2m(self, instance, field):
        # check django's version number to determine how intermediary models
        # are checked if they are auto created or not.
        auto_created_through_model = False
        through = field.rel.through
        auto_created_through_model = through._meta.auto_created

        if auto_created_through_model:
            return self.process_field(instance, field)
        # if m2m relation has intermediary model:
        #   * only generate relation if 'generate_m2m' is given
        #   * first generate intermediary model and assign a newly created
        #     related model to the foreignkey
        kwargs = {}
        if field.name in self.generate_m2m:
            # get fk to related model on intermediary model
            related_fks = [fk
                for fk in through._meta.fields
                if isinstance(fk, related.ForeignKey) and
                    fk.rel.to is field.rel.to]
            self_fks = [fk
                for fk in through._meta.fields
                if isinstance(fk, related.ForeignKey) and
                    fk.rel.to is self.model]
            assert len(related_fks) == 1
            assert len(self_fks) == 1
            related_fk = related_fks[0]
            self_fk = self_fks[0]
            min_count, max_count = self.generate_m2m[field.name]
            intermediary_model = generators.MultipleInstanceGenerator(
                AutoFixture(
                    through,
                    field_values={
                        self_fk.name: instance,
                        related_fk.name: generators.InstanceGenerator(
                            get(field.rel.to))
                    }),
                min_count=min_count,
                max_count=max_count,
                **kwargs).generate()


class BookingFixture(BaseFixture):
    field_values = {
        'address1': '501 Adams St',
        'address2': 'Apt 2E',
        'city': 'Hoboken',
        'start_date_time': datetime.now(),
        'state': 'NJ',
        'stop_date_time': datetime.now() + timedelta(hours=4),
        'zip': '07030',
    }
    generate_fk = True
    generate_m2m = {
        'sitters': (3, 5),
    }


class ChildFixture(BaseFixture):
    field_values = {
        'dob': ChildDobGenerator(),
        'name': NameGenerator(),
    }


class ParentFixture(BaseFixture):
    field_values = {
        'cell': phone_number_generator,
        'email': generators.EmailGenerator(),
        'first_name': generators.FirstNameGenerator(),
        'last_name': generators.LastNameGenerator(),
        'password': make_password('password'),
        'username': UsernameGenerator(),
    }
    generate_fk = True
    generate_m2m = {'sitter_teams': (3, 5)}


class SitterFixture(BaseFixture):
    field_values = {
        'cell': phone_number_generator,
        'dob': SitterDobGenerator(),
        'email': generators.EmailGenerator(),
        'first_name': generators.FirstNameGenerator(),
        'last_name': generators.LastNameGenerator(),
        'password': make_password('password'),
        'total_exp': random.randint(1, 10),
        'pre_teen_exp': random.randint(1, 10),
        'preschool_exp': random.randint(1, 10),
        'teen_exp': random.randint(1, 10),
        'special_needs_exp': random.randint(1, 10),
        'school_age_exp': random.randint(1, 10),
        'toddler_exp': random.randint(1, 10),
        'infant_exp': random.randint(1, 10),
        'one_child_max_rate': 15,
        'one_child_min_rate': 12,
        'two_child_max_rate': 20,
        'two_child_min_rate': 15,
        'three_child_max_rate': 25,
        'three_child_min_rate': 20,
        'username': UsernameGenerator(),
    }
    generate_fk = True


class StaffUserFixture(BaseFixture):
    """
    Should only be used once.

    """
    field_values = {
        'cell': phone_number_generator,
        'email': 'test@sitterfied.com',
        'first_name': generators.FirstNameGenerator(),
        'last_name': generators.LastNameGenerator(),
        'password': make_password('password'),
        'username': 'test',
        'is_staff': True,
    }
    generate_fk = ('parent',)


register('app.Booking', BookingFixture)
register('app.Child', ChildFixture)
register('app.Parent', ParentFixture)
register('app.Sitter', SitterFixture)
register('app.User', StaffUserFixture)
