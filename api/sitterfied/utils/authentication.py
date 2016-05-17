# -*- coding: utf-8 -*-
from rest_framework import authentication, exceptions


class TokenAuthentication(authentication.TokenAuthentication):

    def _get_authorization_header(self, request):
        auth = authentication.get_authorization_header(request)
        if not auth:
            token = request.query_params.get('token', None)
            if token:
                auth = 'Token {}'.format(token)
        return auth

    def authenticate(self, request):
        auth = self._get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(auth[1])
