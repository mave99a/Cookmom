from user import get_current_user

class AuthMiddleware(object):
    def process_request(self, request):
        request.user = get_current_user(request)