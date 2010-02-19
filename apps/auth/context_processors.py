from user import get_current_user

def auth(request):
    return {'user': request.user}
    