from rest_framework_simplejwt.authentication import JWTAuthentication


class AuthJWT(object):
    """
    If is anonymous, this middleware authenticate user with JWT Token.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            user_auth_tupple = JWTAuthentication().authenticate(request)
            if user_auth_tupple is not None:
                request.user, request.auth = user_auth_tupple

        response = self.get_response(request)

        return response
