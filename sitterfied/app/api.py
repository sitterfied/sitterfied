import models
from forms import AvatarForm, ActiveForm, AcceptBookingForm, DeclineBookingForm
from django.contrib.auth import logout

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from rest_framework import serializers, viewsets, permissions
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
               'sitter_groups', 'avatar',
               'address1', 'address2', 'facebook_id',
               'facebook_token', 'friends',
               'city', 'state',
               'zip','cell' )

class OtherServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherService
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language


class UserSerializer(serializers.ModelSerializer):
    parent_or_sitter = serializers.Field(source="is_parent_or_sitter")
    avatar = serializers.Field(source="avatar_url")

    class Meta:
        model = models.User
        fields = user_fields + ('parent_or_sitter',)

class SitterSerializer(serializers.ModelSerializer):
    avatar = serializers.Field(source="avatar_url")
    parent_or_sitter = serializers.Field(source="is_parent_or_sitter")
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
                                'occupation', 'reviews', 'bookings',
                                'bookmarks',  'sitter_teams','parent_or_sitter'
                                )


class SitterSearchSerializer(SitterSerializer):
    in_sitter_team = serializers.SerializerMethodField('is_in_sitter_team')
    in_friends_team = serializers.SerializerMethodField('is_in_friends_team')
    rehires = serializers.IntegerField(source='rehires', read_only=True)

    @cached_property
    def is_parent(self):
        return self.user.is_authenticated() and self.user.is_parent_or_sitter() == 'Parent'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.friends = self.user.friends.select_related('parent') \
                                        .prefetch_related('parent__sitter_teams') \
                                        .filter(parent__isnull=False)
        self.friends_teams  = set()

        for friend in self.friends:
            [self.friends_teams.add(i.id) for i in friend.parent.sitter_teams.all()]

        if self.is_parent:
            self.sitter_teams = self.user.parent.sitter_teams.all()

        return super(SitterSearchSerializer, self).__init__(*args, **kwargs)

    def is_in_sitter_team(self, sitter):
        if not self.is_parent:
            return False
        return sitter in self.sitter_teams

    def is_in_friends_team(self, sitter):
        if not self.is_parent:
            return False
        return sitter.id in self.friends_teams


    class Meta(SitterSerializer.Meta):
        fields = SitterSerializer.Meta.fields + ('in_sitter_team', 'in_friends_team', 'rehires')

class ParentSerializer(serializers.ModelSerializer):
    #contacts
    avatar = serializers.Field(source="avatar_url")
    parent_or_sitter = serializers.Field(source="is_parent_or_sitter")
    class Meta:
        model = models.Parent
        fields = user_fields + ('id','emergency_contact_one_name',
                                'emergency_contact_one_phone',
                                'emergency_contact_two_name',
                                'emergency_contact_two_phone',
                                'reviews', 'bookings', 'children',
                                'bookmarks',  'sitter_teams', 'parent_or_sitter'
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
        fields = ("parent", "sitter", 'recommended', 'review', 'id')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Child

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group


class IdFilterViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = super(IdFilterViewset, self).get_queryset()
        if 'id' in self.request.GET:
            ids = self.request.GET.get('id')
            ids = ids.split(",")
            queryset = queryset.filter(id__in=ids)
        return queryset




class UserViewSet(IdFilterViewset):
    queryset = models.User.objects.all().prefetch_related('languages',
                                                          'sitter_groups',
                                                          'sitter',
                                                          'parent',
                                                          'friends',
                                                          # 'other_services',
                                                          # 'bookings',
                                                          # 'sitter_teams',
                                                          # 'bookmarks',
                                                          'settings').all()

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('friends',)


    @link()
    def bookings(self, request, pk=None):
        queryset = models.Booking.objects.filter(Q(parent=pk) | Q(sitters=pk))
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

        response = Response(data={'avatar':user.avatar.cdn_url})
        return response


    @action()
    def active(self, request, pk=None):
        form = ActiveForm(request.POST)
        user = request.user

        if not form.is_valid():
            return Response(status=400)

        user.is_active = form.cleaned_data['active']
        user.save()
        logout(request)
        return Response({})



    @link()
    def reviews(self, request, pk=None):
        queryset = models.SitterReview.objects.filter(Q(parent_id=pk)|Q(sitter_id=pk))
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def languages(self, request, pk=None):
        queryset = models.Language.objects.filter(users=pk)
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)


    @link()
    def users_in_network(self, request, pk=None):
        queryset = models.User.objects.filter(users_in_network=pk)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def friends(self, request, pk=None):
        queryset = models.User.objects.select_related('settings').prefetch_related('friends',
                                                                                   'languages',
                                                                                   'sitter_groups',
                                                                                   'parent',
                                                                                   'sitter',).filter(friends=pk)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)




class SitterViewSet(IdFilterViewset):
    queryset = models.Sitter.objects.select_related().prefetch_related('reviews',
                                                                       'languages',
                                                                       'sitter_groups',
                                                                       'friends',
                                                                       'certifications',
                                                                       'schedlue',
                                                                       'other_services',
                                                                       'bookings',
                                                                       'sitter_teams',
                                                                       'bookmarks',
                                                                       'settings').all()
    serializer_class = SitterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    @link()
    def bookings(self, request, pk=None):
        queryset = models.Booking.objects.prefetch_related('sitters'
                                                            ,'declined_sitters'
                                                            ,).filter(Q(parent=pk) | Q(sitters=pk))
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)



class ParentViewSet(IdFilterViewset):
    queryset = models.Parent.objects.all().select_related('settings').prefetch_related('reviews',
                                                                                       'languages',
                                                                                       'settings',
                                                                                       'sitter_groups',
                                                                                       'bookings',
                                                                                       'children',
                                                                                       'friends',
                                                                                       'sitter_teams',
                                                                                       'bookmarks',
                                                                                   )
    serializer_class = ParentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @link()
    def children(self, request, pk=None):
        queryset = models.Child.objects.select_related('parent').prefetch_related('special_needs').filter(parent=pk)
        serializer = ChildSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def sitter_teams(self, request, pk=None):
        queryset = models.Sitter.objects.prefetch_related('reviews',
                                                          'languages',
                                                          'sitter_teams',
                                                          'sitter_groups',
                                                          'bookmarks',
                                                           'friends',
                                                           'certifications',
                                                           'schedlue',
                                                           'other_services',
                                                            'bookings',
                                                           'settings').filter(sitter_teams=pk)

        serializer = SitterSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def bookmarks(self, request, pk=None):
        queryset = models.Sitter.objects.prefetch_related('reviews',
                                                          'languages',
                                                          'sitter_groups',
                                                          'friends',
                                                          'certifications',
                                                          'schedlue',
                                                          'other_services',
                                                          'bookings',
                                                          'bookmarks',
                                                          'sitter_teams',
                                                          'settings').filter(bookmarks=pk)
        serializer = SitterSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def bookings(self, request, pk=None):
        queryset = models.Booking.objects.select_related('parent').prefetch_related('sitters'
                                                                                    ,'declined_sitters'
                                                                                    ,).filter(Q(parent=pk) | Q(sitters=pk))
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)


import django_filters
class GroupFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type="icontains")
    class Meta:
        model = models.Group
        fields = ('name',)

class GroupViewSet(IdFilterViewset):
    queryset = models.Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = GroupFilter

class CertificationViewSet(IdFilterViewset):
    queryset = models.Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OtherServiceViewSet(IdFilterViewset):
    queryset = models.OtherService.objects.all()
    serializer_class = OtherServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SettingsViewSet(IdFilterViewset):
    queryset = models.Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SchedlueViewSet(IdFilterViewset):
    queryset = models.Schedlue.objects.all()
    serializer_class = SchedlueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ReviewViewSet(IdFilterViewset):
    queryset = models.SitterReview.objects.all().select_related('parent', 'sitter')
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BookingViewSet(IdFilterViewset):
    queryset = models.Booking.objects.all().select_related('parent').prefetch_related('sitters', 'declined_sitters')
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    @link()
    def sitters(self, request, pk=None):
        queryset = models.Sitter.objects.filter(bookings=pk)
        serializer = SitterSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def declined_sitters(self, request, pk=None):
        queryset = models.Sitter.objects.filter(declined_bookings=pk)
        serializer = SitterSerializer(queryset, many=True)
        return Response(serializer.data)

    @action()
    def accept_booking(self, request, pk=None):
        booking = get_object_or_404(models.Booking, pk=pk)
        sitter = request.user.sitter
        booking.accept(sitter)
        serializer = BookingSerializer(booking)
        response = Response(serializer.data)
        return response

    @action()
    def cancel_booking(self, request, pk=None):
        booking = get_object_or_404(models.Booking, pk=pk)
        booking.cancel()
        serializer = BookingSerializer(booking)
        response = Response(serializer.data)
        return response

    @action()
    def decline_booking(self, request, pk=None):
        booking = get_object_or_404(models.Booking, pk=pk)
        sitter = request.user.sitter
        booking.decline(sitter)
        serializer = BookingSerializer(booking)
        response = Response(serializer.data)
        return response




class LanguageViewSet(IdFilterViewset):
    queryset = models.Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SpecialNeedViewSet(IdFilterViewset):
    queryset = models.SpecialNeed.objects.all()
    serializer_class = SpecialNeedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class ChildrenViewSet(IdFilterViewset):
    queryset = models.Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('parent', 'school', 'special_needs')


#bookings
#languages
