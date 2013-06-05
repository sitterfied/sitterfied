import models

from rest_framework import serializers, viewsets, permissions
from rest_framework import viewsets

# class MyselfSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.User
#         fields = ('first_name', 'last_name', 'username', 'email')

user_fields = ('first_name', 'last_name', 'username', 'last_login', 'date_joined')


class SitterSerializer(serializers.HyperlinkedModelSerializer):

    #todo general availablity
    class Meta:
        model = models.Sitter
        fields = user_fields + ('biography', 'live_zip',
                  'work_zip', 'smoker',
                  'will_transport', 'total_exp',
                  'infant_exp',  'toddler_exp',
                  'preschool_exp', 'school_age_exp',
                  'pre_teen_exp', 'teen_exp',
                  'highest_education', 'last_school',
                  'current_student','certification',
                  'other_services','one_child_min_rate',
                  'one_child_max_rate', 'two_child_min_rate',
                  'two_child_max_rate',  'three_child_min_rate',
                  'three_child_max_rate',  'smokers_ok',
                  'dogs_ok', 'cats_ok',
                  'other_animals_ok',
                  )


class ParentSerializer(serializers.HyperlinkedModelSerializer):

    #contacts
    class Meta:
        model = models.Parent
        fields = user_fields + ('emergency_contact', 'physician_contact',
                  'parking_area', 'parking_for_sitter'
                  )

class SitterViewSet(viewsets.ModelViewSet):
    queryset = models.Sitter.objects.all()
    serializer_class = SitterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ParentViewSet(viewsets.ModelViewSet):
    queryset = models.Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


#bookings
#languages
