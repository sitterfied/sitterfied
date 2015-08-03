# -*- coding: utf-8 -*-
import inspect
import random
import string
import warnings

from autofixture import AutoFixture, base, generators, get, register, signals
from autofixture.compat import GenericRelation
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

    def update_follow_fk(self, follow_fk):
        if follow_fk is not None:
            self.follow_fk = follow_fk
        if not isinstance(self.follow_fk, base.Link):
            self.follow_fk = base.Link(self.follow_fk)
        return self

    def update_follow_m2m(self, follow_m2m):
        if follow_m2m is not None:
            if not isinstance(follow_m2m, dict):
                if follow_m2m:
                    follow_m2m = base.Link({'ALL': follow_m2m})
                else:
                    follow_m2m = base.Link(False)
            self.follow_m2m = follow_m2m
        if not isinstance(self.follow_m2m, base.Link):
            self.follow_m2m = base.Link(self.follow_m2m)
        return self

    def update_generate_fk(self, generate_fk):
        if generate_fk is not None:
            self.generate_fk = generate_fk
        if not isinstance(self.generate_fk, base.Link):
            self.generate_fk = base.Link(self.generate_fk)
        return self

    def update_generate_m2m(self, generate_m2m):
        if generate_m2m is not None:
            if not isinstance(generate_m2m, dict):
                if generate_m2m:
                    generate_m2m = base.Link({'ALL': generate_m2m})
                else:
                    generate_m2m = base.Link(False)
            self.generate_m2m = generate_m2m
        if not isinstance(self.generate_m2m, base.Link):
            self.generate_m2m = base.Link(self.generate_m2m)
        return self

    def create_one(self, commit=True):
        '''
        Create and return one model instance. If *commit* is ``False`` the
        instance will not be saved and many to many relations will not be
        processed.
        Subclasses that override ``create_one`` can specify arbitrary keyword
        arguments. They will be passed through by the
        :meth:`autofixture.base.AutoFixture.create` method and the helper
        functions :func:`autofixture.create` and
        :func:`autofixture.create_one`.
        May raise :exc:`CreateInstanceError` if constraints are not satisfied.
        '''
        tries = self.tries
        instance = self.model()
        process = instance._meta.fields
        while process and tries > 0:
            for field in process:
                self.process_field(instance, field)
            process = self.check_constraints(instance)
            tries -= 1
        if tries == 0:
            raise base.CreateInstanceError(
                u'Cannot solve constraints for "%s", tried %d times. '
                u'Please check value generators or model constraints. '
                u'At least the following fields are involved: %s' % (
                    '%s.%s' % (
                        self.model._meta.app_label,
                        self.model._meta.object_name),
                    self.tries,
                    ', '.join([field.name for field in process]),
                ))

        instance = self.pre_process_instance(instance)

        if commit:
            instance.save()

            # to handle particular case of GenericRelation
            # in Django pre 1.6 it appears in .many_to_many
            many_to_many = [
                f for f in instance._meta.many_to_many
                if not isinstance(f, GenericRelation)
            ]
            for field in many_to_many:
                self.process_m2m(instance, field)

            related_objects = [
                f for f in instance._meta.get_all_related_objects()
                if isinstance(f.field.rel, related.ManyToOneRel)
            ]
            for related_object in related_objects:
                self.process_related_object(instance, related_object)

        signals.instance_created.send(
            sender=self,
            model=self.model,
            instance=instance,
            committed=commit)

        post_process_kwargs = {}
        if 'commit' in inspect.getargspec(self.post_process_instance).args:
            post_process_kwargs['commit'] = commit
        else:
            warnings.warn(
                "Subclasses of AutoFixture need to provide a `commit` "
                "argument for post_process_instance methods", DeprecationWarning)
        return self.post_process_instance(instance, **post_process_kwargs)

    def process_m2m(self, instance, field):
        # check django's version number to determine how intermediary models
        # are checked if they are auto created or not.
        auto_created_through_model = False
        through = field.rel.through
        auto_created_through_model = through._meta.auto_created

        if auto_created_through_model:
            if field.name in self.follow_m2m or field.name in self.generate_m2m:
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
            generators.MultipleInstanceGenerator(
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

    def process_related_object(self, instance, related_object):
        """
        Create objects that have a many-to-one relationship with the instance.

        """
        kwargs = {}
        field_name = related_object.name
        if field_name in self.generate_m2m:
            self_fk = related_object.field
            min_count, max_count = self.generate_m2m[field_name]
            autofixture = get(related_object.related_model)
            autofixture.add_field_value(self_fk.name, instance)
            generators.MultipleInstanceGenerator(
                autofixture,
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

register('app.Booking', BookingFixture)


class ChildFixture(BaseFixture):
    field_values = {
        'dob': ChildDobGenerator(),
        'name': NameGenerator(),
    }
    follow_fk = False
    generate_fk = False

register('app.Child', ChildFixture)


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
    generate_m2m = {
        'children': (1, 3),
        'sitter_teams': (3, 5)
    }

register('app.Parent', ParentFixture)


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

register('app.Sitter', SitterFixture)


class StaffUserFixture(BaseFixture):
    """
    Should only be used once.

    """
    field_values = {
        'cell': phone_number_generator,
        'email': generators.EmailGenerator(tlds=['sitterfied.com']),
        'first_name': generators.FirstNameGenerator(),
        'last_name': generators.LastNameGenerator(),
        'password': make_password('password'),
        'username': UsernameGenerator(),
        'is_staff': True,
    }
    follow_m2m = False
    generate_fk = ['parent', 'auth_token']

register('app.User', StaffUserFixture)
