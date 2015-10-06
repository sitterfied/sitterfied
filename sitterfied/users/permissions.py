# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsStaffOrSelf(permissions.IsAuthenticatedOrReadOnly):
    """
    Allow anonymous HEAD requests.

    Allows either a staff user or the current account to make modifications.

    Fallback to authentication if the first two checks do not pass.

    @see sitterfied.utils.permissions.IsStaffOrOwner

    """
    def has_permission(self, request, view):
        """
        Only allow anonymous HEAD requests.

        """
        if view.action == 'head' and request.method == 'HEAD':
            return True

        # Don't block requests to detail routes. The
        # has_object_permission method will prevent unauthorized
        # requests to those routes.
        if view.action in [
            'bookings',
            'avatar_upload',
            'active',
            'reviews',
            'languages',
            'users_in_network',
            'friends',
        ]:
            return True

        if request.user.is_anonymous():
            return False

        return super(IsStaffOrSelf, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if view.action == 'head' and request.method == 'HEAD':
            return True

        return request.user.is_staff or getattr(obj, obj.is_parent_or_sitter().lower(), None) == request.user
