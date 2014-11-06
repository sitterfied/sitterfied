# -*- coding: utf-8 -*-
from drf_ujson.renderers import UJSONRenderer
from rest_framework import status, viewsets
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response


class IdFilterViewset(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, UJSONRenderer)

    def get_queryset(self):
        queryset = super(IdFilterViewset, self).get_queryset()
        if 'id' in self.request.GET:
            ids = self.request.GET.get('id')
            ids = ids.split(",")
            queryset = queryset.filter(id__in=ids)
        return queryset


class SubSerializerViewMixin(object):

    def get_sub_serializers(self, sub_data, request):
        """
        Get sub-serializers for the keys defined in the sub_serializers property.

        """
        sub_serializers = []
        for key, value in sub_data.items():
            if value:
                sub_serializer_class = self.sub_serializers.get(key)[0]
                sub_serializer_field_name = self.sub_serializers.get(key)[1]
                sub_serializer_list = [sub_serializer_class(
                    data={sub_serializer_field_name: val},
                    context={'request': request},
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
                serializer.object.parent = self.object
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
        if sub_serializers:
            for serializer in sub_serializers:
                serializer.object.parent = self.object
                serializer.save()

        response_serializer = self.serializer_class(self.get_object_or_none(), context={"request": self.request})
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_200_OK, headers=headers)
