import models
from forms import AvatarForm

from django.db.models import Q


from rest_framework import serializers, viewsets, permissions
from rest_framework import serializers
from rest_framework import filters
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, link
from app.models import Language

# class MyselfSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.User
#         fields = ('first_name', 'last_name', 'username', 'email')

user_fields = ('first_name', 'last_name',
               'username', 'last_login',
               'date_joined', 'settings',
               'email', 'languages',
               'sitter_groups',
               'address1', 'address2', 'facebook_id',
               'facebook_token', 'friends',
               'city', 'state', 'avatar',
               'zip','cell' )

class OtherServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherService
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language


class UserSerializer(serializers.ModelSerializer):
    parent_or_sitter = serializers.Field(source="is_parent_or_sitter")

    class Meta:
        model = models.User
        fields = user_fields + ('parent_or_sitter',)

class SitterSerializer(serializers.ModelSerializer):

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
                                'one_child_min_rate',
                                'one_child_max_rate', 'two_child_min_rate',
                                'two_child_max_rate',  'three_child_min_rate',
                                'three_child_max_rate',  'smokers_ok',
                                'dob', 'schedlue', 'other_services',
                                'dogs_ok', 'cats_ok',
                                'other_animals_ok',
                                'gender', 'sick',
                                'has_drivers_licence', 'travel_distance',
                                'special_needs_exp', 'extra_exp', 'major',
                                'occupation', 'reviews', 'bookings'
                                )


class SitterSearchSerializer(SitterSerializer):
    in_sitter_team = serializers.SerializerMethodField('is_in_sitter_team')
    in_friends_team = serializers.SerializerMethodField('is_in_friends_team')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.friends = list(self.user.friends.all())
        return super(SitterSearchSerializer, self).__init__(*args, **kwargs)

    def is_in_sitter_team(self, sitter):
        if not self.user.is_authenticated() or self.user.is_parent_or_sitter() != 'Parent':
            return False
        return sitter in self.user.parent.sitter_teams.all()

    def is_in_friends_team(self, sitter):
        if not self.user.is_authenticated() or self.user.is_parent_or_sitter() != 'Parent':
            return False
        return sitter.sitter_teams.filter(pk__in=self.friends).exists()





    class Meta(SitterSerializer.Meta):
        fields = SitterSerializer.Meta.fields + ('in_sitter_team', 'in_friends_team')



class ParentSerializer(serializers.ModelSerializer):

    #contacts
    parent_or_sitter = "Parent"
    class Meta:
        model = models.Parent
        fields = user_fields + ('id','emergency_contact_one_name',
                                'emergency_contact_one_phone',
                                'emergency_contact_two_name',
                                'emergency_contact_two_phone',
                                'reviews', 'bookings', 'children',
                                'sitter_teams',
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

class SpecialNeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpecialNeed


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SitterReview

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Child



class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('id', 'friends')


    @link()
    def bookings(self, request, pk=None):
        queryset = models.Booking.objects.filter(Q(parent=pk) | Q(bookingrequest__sitter=pk))
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    @action()
    def avatar_upload(self, request, pk=None):
        form = AvatarForm(request.POST)
        user = request.user

        if not form.is_valid():
            return Response(status=400)

        user.avatar = form.cleaned_data['avatar']
        user.save()

        response = Response(data={'avatar':user.avatar.name})
        return response



    @link()
    def reviews(self, request, pk=None):
        queryset = models.SitterReview.objects.filter(Q(parent_id=pk)|Q(sitter_id=pk))
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def users_in_network(self, request, pk=None):
        queryset = models.User.objects.filter(users_in_network=pk)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def friends(self, request, pk=None):
        queryset = models.User.objects.filter(friends=pk)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)



class SitterViewSet(viewsets.ModelViewSet):
    queryset = models.Sitter.objects.select_related().prefetch_related('reviews',
                                                                       'languages',
                                                                       'sitter_groups',
                                                                       'friends',
                                                                       'certifications',
                                                                       'schedlue',
                                                                       'other_services',
                                                                       'bookings',
                                                                       'settings').all()
    serializer_class = SitterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('id', )

class ParentViewSet(viewsets.ModelViewSet):
    queryset = models.Parent.objects.all().select_related().prefetch_related('reviews',
                                                                             'languages',
                                                                             'settings',
                                                                             'sitter_groups',
                                                                             'bookings',
                                                                             'children',
                                                                             'friends',
                                                                             'sitter_teams',
                                                                             )
    serializer_class = ParentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_fields = ('id', )

    @link()
    def children(self, request, pk=None):
        queryset = models.Child.objects.filter(parent=pk)
        serializer = ChildSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def sitter_teams(self, request, pk=None):
        queryset = models.Sitter.objects.filter(sitter_teams=pk).prefetch_related('reviews',
                                                                       'languages',
                                                                       'sitter_groups',
                                                                       'friends',
                                                                       'certifications',
                                                                       'schedlue',
                                                                       'other_services',
                                                                       'bookings',
                                                                       'settings').all()
        serializer = SitterSerializer(queryset, many=True)
        return Response(serializer.data)



class CertificationViewSet(viewsets.ModelViewSet):
    queryset = models.Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OtherServiceViewSet(viewsets.ModelViewSet):
    queryset = models.OtherService.objects.all()
    serializer_class = OtherServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)




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
    filter_fields = ('id', )

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('id', )


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SpecialNeedViewSet(viewsets.ModelViewSet):
    queryset = models.SpecialNeed.objects.all()
    serializer_class = SpecialNeedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = models.Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('id', 'parent', 'school', 'special_needs')


#bookings
#languages
