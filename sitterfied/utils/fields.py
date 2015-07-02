# -*- coding: utf-8 -*-
import json

from rest_framework import serializers
from urllib import unquote


class UrlEncodedJsonField(serializers.Field):
    """
    A serializer field that will take urlencoded json string and convert it to a
    python object.

    """

    def to_internal_value(self, data):
        """
        Decode the string and then load it as json.

        """
        return json.loads(unquote(data).decode('utf8'))
