from models import User

def alltop(request, num=5):
    return User.all().fetch(num)

def weeklytop(request, num=5):
    return User.all().fetch(num)