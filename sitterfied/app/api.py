import models

from django.db.models import Q


from rest_framework import serializers, viewsets, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, link

# class MyselfSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.User
#         fields = ('first_name', 'last_name', 'username', 'email')

user_fields = ('first_name', 'last_name',
               'username', 'last_login',
               'date_joined', 'settings',
               'sitters_in_network', 'email',
               'parents_in_network', 'sitter_groups',
               'address1', 'address2',
               'city', 'state', 'avatar',
               'zip','bookings', 'cell' )


class SitterSerializer(serializers.ModelSerializer):

    #todo general availablity
    parent_or_sitter = "Sitter"

    parents_in_network = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = models.Sitter
        fields = user_fields + ('id', 'biography', 'live_zip',
                                'work_zip', 'smoker',
                                'will_transport', 'total_exp',
                                'infant_exp',  'toddler_exp',
                                'preschool_exp', 'school_age_exp',
                                'pre_teen_exp', 'teen_exp',
                                'highest_education', 'last_school',
                                'current_student','certifications',
                                'other_services','one_child_min_rate',
                                'one_child_max_rate', 'two_child_min_rate',
                                'two_child_max_rate',  'three_child_min_rate',
                                'three_child_max_rate',  'smokers_ok',
                                'dob', 'schedlue',
                                'dogs_ok', 'cats_ok',
                                'other_animals_ok',
                                'gender', 'sick',
                                'has_drivers_licence', 'travel_distance',
                                'special_needs_exp', 'extra_exp', 'major',
                                'occupation', 'reviews'
                                )



class ParentSerializer(serializers.ModelSerializer):

    #contacts
    parent_or_sitter = "Parent"
    class Meta:
        model = models.Parent
        fields = user_fields + ('id', 'emergency_contact', 'physician_contact',
                  'parking_area', 'parking_for_sitter', 'reviews'
                  )


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings

class SchedlueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedlue

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certification

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SitterReview


class UserViewSet(object):

    @link()
    def reviews(self, request, pk=None):
        queryset = models.SitterReview.objects.filter(Q(parent_id=pk)|Q(sitter_id=pk))
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)


    @link()
    def parents_in_network(self, request, pk=None):
        queryset = models.User.objects.get(pk=pk).parents_in_network.all()
        serializer = ParentSerializer(queryset, many=True)
        return Response(serializer.data)


class SitterViewSet(viewsets.ModelViewSet, UserViewSet):
    queryset = models.Sitter.objects.all()
    serializer_class = SitterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('id', )

class ParentViewSet(viewsets.ModelViewSet, UserViewSet):
    queryset = models.Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_fields = ('id', )

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = models.Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('id', )




class SettingsViewSet(viewsets.ModelViewSet):
    queryset = models.Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SchedlueViewSet(viewsets.ModelViewSet):
    queryset = models.Schedlue.objects.all()
    serializer_class = SchedlueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.SitterReview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


#bookings
#languages
