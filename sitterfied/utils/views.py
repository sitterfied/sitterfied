# -*- coding: utf-8 -*-
from rest_framework import status, viewsets
from rest_framework.response import Response

from sitterfied.utils import NODATA


class IdFilterViewset(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = super(IdFilterViewset, self).get_queryset()
        if 'id' in self.request.GET:
            ids = self.request.GET.get('id')
            queryset = queryset.filter(id__in=ids.split(','))
        return queryset


class SubSerializerViewMixin(object):

    def get_sub_serializers(self, sub_data, request):
        """
        Get sub-serializers for the keys defined in the sub_serializers property.

        The expected behavior from a client on an update for a given `key` value is:
        {key: null} -> clear key
        {key: []} -> clear key
        {key: [<value>] -> replace
        {} -> no modification (NODATA)

        Because of this, there is a difference between null -> None and not passing a value (NODATA).

        """
        sub_serializers = []
        for key, value in sub_data.items():
            # Value that should not modify the artists
            if value == NODATA:
                return None
            # Values that should replace the artists with an empty []
            elif value in (None, []):
                return []

            sub_serializer_dict = self.sub_serializers.get(key)
            sub_serializer_class = sub_serializer_dict.get('serializer')
            sub_serializer_field_name = sub_serializer_dict.get('to_field')
            sub_serializer_from_field = sub_serializer_dict.get('from_field')
            sub_serializer_related_name = sub_serializer_dict.get('related_name')

            def get_object(id):
                try:
                    return getattr(self.object, sub_serializer_related_name).get(**{sub_serializer_field_name: id})
                except Exception:
                    return None

            sub_serializer_list = [sub_serializer_class(
                get_object(val),
                data={sub_serializer_field_name: val},
                context={
                    'request': request,
                    'from_field': sub_serializer_from_field,
                    'related_name': sub_serializer_related_name,
                }
            ) for val in value]
            sub_serializers.extend(sub_serializer_list)

        return sub_serializers

    def sub_serializers_are_valid(self, sub_serializers):
        """
        Validate the sub serializer array to a single Boolean value

        """
        if not sub_serializers:  # Empty array or None is valid
            return True
        return all([ser.is_valid() for ser in sub_serializers])

    def handle_invalid(self, serializer, sub_serializers):
        """
        Handle creating an invalid serializer response for all serializers.

        """
        errors = serializer.errors
        if sub_serializers:
            errors.update({
                'sub_errors': {s.init_data[s.init_data.keys()[0]]: 'Invalid sub serializer' for s in filter(
                    lambda x: not x.is_valid(), sub_serializers)}
            })
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """
        Create a new entity on POST

        """
        data = request.DATA.copy()
        sub_data = {key: value for key, value in data.items() if key in self.sub_serializers.keys()}

        # Remove any sub-serializer key/value pairs
        for key in sub_data.keys():
            data.pop(key)

        serializer = self.get_serializer_class()(data=data, context={'request': request})
        sub_serializers = self.get_sub_serializers(sub_data, request)

        if not (
            serializer.is_valid() and
            self.sub_serializers_are_valid(sub_serializers)
        ):
            return self.handle_invalid(serializer, sub_serializers)

        self.pre_save(serializer.object)
        self.object = serializer.save(force_insert=True)
        self.post_save(self.object, created=True)
        if sub_serializers is not None:
            for serializer in sub_serializers:
                from_field = serializer.context.get('from_field', None)
                if from_field:
                    setattr(serializer.object, from_field, self.object)
                serializer.save()

        response_serializer = self.serializer_class(self.object, context={'request': request})
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Update processing for both PUT and PATCH

        """
        partial = kwargs.pop('partial', False)
        self.object = self.get_object_or_none()

        data = request.DATA.copy()
        sub_data = {key: value for key, value in data.items() if key in self.sub_serializers.keys()}

        # Remove any sub-serializer key/value pairs
        for key in sub_data.keys():
            data.pop(key)

        serializer = self.get_serializer_class()(
            self.object,
            data=data,
            context={'request': request},
            partial=partial,
        )
        sub_serializers = self.get_sub_serializers(sub_data, request)

        if not (
            serializer.is_valid() and
            # Only check for valid subserializers if we have any
            self.sub_serializers_are_valid(sub_serializers)
        ):
            return self.handle_invalid(serializer, sub_serializers)

        self.pre_save(serializer.object)
        self.object = serializer.save()
        self.post_save(self.object, created=False)

        # Delete sub_serializers if we explicitly set it to an empty array
        # or are passing in new values. Also delete sub_serialziers on a PUT
        # with no value.
        if (
            sub_serializers == [] or
            sub_serializers or
            (
                not partial and
                sub_serializers is None
            )
        ):
            if not sub_serializers:
                for data in self.sub_serializers.values():
                    related_name = data.get('related_name', None)
                    if hasattr(self.object, related_name):
                        getattr(self.object, related_name).all().delete()
            else:
                for key, data in self.sub_serializers.items():
                    pks = sub_data.get(key)
                    related_name = data.get('related_name', None)
                    to_field = data.get('to_field')
                    if hasattr(self.object, related_name):
                        exclude_args = {'{}__in'.format(to_field): pks}
                        getattr(self.object, related_name).exclude(**exclude_args).delete()

        if sub_serializers:
            for sub_serializer in sub_serializers:
                from_field = sub_serializer.context.get('from_field', None)
                if from_field:
                    setattr(sub_serializer.object, from_field, self.object)
                sub_serializer.save()

        response_serializer = self.serializer_class(self.get_object_or_none(), context={"request": self.request})
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_200_OK, headers=headers)
