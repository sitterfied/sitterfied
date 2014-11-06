# -*- coding: utf-8 -*-
from django.utils.functional import cached_property
from rest_framework import serializers

from sitterfied.sitters.models import Sitter, SitterReview
from sitterfied.users.serializers import default_fields


class SitterSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.Field(source='avatar_url')
    languages = serializers.PrimaryKeyRelatedField(many=True)
    parent_or_sitter = serializers.Field(source='is_parent_or_sitter')

    class Meta:
        model = Sitter
        fields = default_fields + (
            'biography',
            'bookings',
            'bookmarks',
            'cats_ok',
            'certifications',
            'current_student',
            'dob',
            'dogs_ok',
            'extra_exp',
            'gender',
            'has_drivers_licence',
            'highest_education',
            'infant_exp',
            'last_school',
            'major',
            'occupation',
            'one_child_max_rate',
            'one_child_min_rate',
            'other_animals_ok',
            'other_services',
            'parent_or_sitter',
            'pre_teen_exp',
            'preschool_exp',
            'reviews',
            'schedule',
            'school_age_exp',
            'sick',
            'sitter_teams',
            'smoker',
            'smokers_ok',
            'special_needs_exp',
            'teen_exp',
            'three_child_max_rate',
            'three_child_min_rate',
            'toddler_exp',
            'total_exp',
            'travel_distance',
            'two_child_max_rate',
            'two_child_min_rate',
            'will_transport',
        )


class SitterSearchSerializer(SitterSerializer):
    in_sitter_team = serializers.SerializerMethodField('is_in_sitter_team')
    in_friends_team = serializers.SerializerMethodField('is_in_friends_team')
    rehires = serializers.IntegerField(read_only=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.friends = self.user.friends \
            .select_related('parent') \
            .prefetch_related('parent__sitter_teams') \
            .filter(parent__isnull=False)

        self.friends_teams = set()

        for friend in self.friends:
            [self.friends_teams.add(i.id) for i in friend.parent.sitter_teams.all()]

        if self.is_parent:
            self.sitter_teams = self.user.parent.sitter_teams.all()

        return super(SitterSearchSerializer, self).__init__(*args, **kwargs)

    def is_in_friends_team(self, sitter):
        return False if not self.is_parent else sitter.id in self.friends_teams

    def is_in_sitter_team(self, sitter):
        return False if not self.is_parent else sitter in self.sitter_teams

    @cached_property
    def is_parent(self):
        return self.user.is_authenticated() and self.user.is_parent_or_sitter() == 'Parent'

    class Meta(SitterSerializer.Meta):
        fields = SitterSerializer.Meta.fields + (
            'in_friends_team',
            'in_sitter_team',
            'rehires',
        )


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SitterReview
        fields = (
            'id',
            'parent',
            'recommended',
            'rehire',
            'review',
            'sitter',
            'url',
        )
