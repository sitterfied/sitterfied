# -*- coding: utf-8 -*-
from rest_framework import permissions

from sitterfied.children.models import Child
from sitterfied.children.serializers import ChildSerializer
from sitterfied.utils.views import IdFilterViewset, OutputSerializerMixin


class ChildViewSet(OutputSerializerMixin, IdFilterViewset):
    filter_fields = ('parent', 'school', 'special_needs')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'id'
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
