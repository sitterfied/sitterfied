# -*- coding: utf-8 -*-
from rest_framework import serializers


class ExcludeM2MValidationMixin(serializers.Serializer):
    """
    Mixin for providing writable M2M validation.

    The reason for this mixin is that attempting to access an m2m attribute of
    a new instance will cause Django to throw a ValueError because the model
    has not been saved yet.

    get_validation_exclusions should not try to access the value of the
    instance in these cases.
    """
    def get_validation_exclusions(self, instance=None):
        """
        Return a list of field names to exclude from model validation.

        This code is almost directly lifted from DRF but delays the check for
        an attribute on the instance if the field is m2m. This keeps the
        accessor from causing Django to throw a ValueError.
        """
        cls = self.opts.model
        opts = cls._meta.concrete_model._meta
        # Seperate m2m_fields since we need to check it separately
        m2m_fields = [field.name for field in opts.many_to_many]
        exclusions = [field.name for field in opts.fields] + m2m_fields

        for field_name, field in self.fields.items():
            field_name = field.source or field_name
            if (
                field_name in exclusions
                and not field.read_only
                # Check that field is not in m2m_fields before trying to access the attribute
                # hasattr was causing django to throw a ValueError when a model was not saved yet.
                # Prefacing the hasattr call with the check for m2m means that
                # if the field is m2m, we never check if the instance has the
                # attribute.
                and (field.required or (field_name not in m2m_fields and hasattr(instance, field_name)))
                and not isinstance(field, serializers.Serializer)
            ):
                exclusions.remove(field_name)
        return exclusions
