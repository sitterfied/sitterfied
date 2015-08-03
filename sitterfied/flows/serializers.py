# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.utils.fields import UrlEncodedJsonField


class TextItInWebhookSerializer(serializers.Serializer):
    event = serializers.CharField(required=False, help_text='The type of the event, will always be "flow"')
    relayer = serializers.IntegerField(help_text='The id of the channel that is executing this flow')
    relayer_phone = serializers.CharField(
        required=False,
        help_text='The phone number of the channel that is executing this flow')
    phone = serializers.CharField(help_text='The phone number of the contact that has reached this point in the flow')
    flow = serializers.IntegerField(
        help_text='The id of the flow that received an event (use the URL on your flow page for reference)')
    step = serializers.CharField(help_text='The step that triggered this API call, use the flow step for reference')
    text = serializers.CharField(help_text='The text sent by the user.')
    time = serializers.DateTimeField(help_text='The time the text was received.')
    values = UrlEncodedJsonField(
        required=False,
        help_text='The values collected from the user so far through this flow, in order of collection time')
