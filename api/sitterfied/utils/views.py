# -*- coding: utf-8 -*-
from rest_framework import mixins, viewsets


class IdFilterViewset(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = super(IdFilterViewset, self).get_queryset()
        if 'id' in self.request.GET:
            ids = self.request.GET.get('id')
            queryset = queryset.filter(id__in=ids.split(','))
        return queryset


class OutputSerializerUpdateMixin(mixins.UpdateModelMixin):
    """
    ViewSet mixin that will return the GET serializer once a resource is updated.

    """
    def update(self, request, *args, **kwargs):
        response = super(OutputSerializerUpdateMixin, self).update(request, *args, **kwargs)

        if response.status_code in [200, 201]:
            serializer = self.serializer_class(self.get_object(), context=self.get_serializer_context())
            response.data = serializer.data

        return response


class OutputSerializerCreateMixin(mixins.CreateModelMixin):
    """
    ViewSet mixin that will return the GET serializer once a resource is created

    This is useful when you want to send certain fields to create a new
    resource but return the resource as it would look from a GET request to the
    new resource.

    """
    def create(self, request, *args, **kwargs):
        response = super(OutputSerializerCreateMixin, self).create(request, *args, **kwargs)

        if response.status_code in [200, 201, 202]:
            # In order to call get_object we need to update the viewset kwargs
            # with the objects lookup field
            self.kwargs.update({self.lookup_field: response.data[self.lookup_field]})
            serializer = self.serializer_class(self.get_object(), context=self.get_serializer_context())
            response.data = serializer.data
            # Make sure the Location header gets added to the list of
            # response headers
            headers = self.get_success_headers(serializer.data)
            # The Response object expects HTTP headers to be a
            # key/value pair where the key is the lower-cased form of
            # the header and the value is a tuple containg the header
            # name and value.
            response._headers.update({key.lower(): (key, value) for key, value in headers.items()})

        return response


class OutputSerializerMixin(OutputSerializerCreateMixin, OutputSerializerUpdateMixin):
    """
    A view set mixin class for using a different serializer for output vs input.

    The default serializer (i.e., the serializer specified by the
    serializer_class attribute) will be used to serialize the output of POST,
    PATCH, and PUT requests.

    """
    pass
