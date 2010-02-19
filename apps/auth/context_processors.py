from user import get_current_user

def auth(request):
    if hasattr(request, 'authuser'):
        return {'authuser': request.authuser, 'user': request.authuser.user}
    