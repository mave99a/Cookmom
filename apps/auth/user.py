from google.appengine.api import users

class AnonymousUser: 
    def is_authenticated(self):   
        return False
    def loginurl(self):
        return users.create_login_url('/')
    
    def logouturl(self):
        return users.create_logout_url('/')
    
    def profile(self):        
        return None
    
    def name(self):
        return 'Guest'
    
    def email(self):
        return '@'
            
class GoogleUser:     
    def __init__(self, user):
        self.user = user
        
    def is_authenticated(self):   
        return True
    
    @classmethod
    def getUser(cls, request):
        user = users.get_current_user() 
        if user:
            return GoogleUser(user)
        else:
            return None
    
    def loginurl(self):
        return users.create_login_url('/')
    
    def logouturl(self):
        return users.create_logout_url('/')
    
    def profile(self):        
        pass
    
    def name(self):
        return self.user.nickname()
    
    def email(self):
        return self.user.email()
    
class FacebookUser():
    @classmethod
    def getUser(cls, request):
        if getattr(request, 'facebook', None):
            if request.facebook.check_session(request):        
                return FacebookUser(request.facebook)
        return None

    def __init__(self, fb):
        self.fb = fb
        
    def is_authenticated(self):   
        return True
             
    def loginurl(self):
        pass
    
    def logouturl(self):
        pass
    
    def profile(self):        
        pass
    
    def name(self):
        return self.fb.uid
    
    def email(self):
        return self.fb.uid
    
def get_current_user(request):
    AuthMethods = [FacebookUser, GoogleUser]
    for method in AuthMethods:
        user = method.getUser(request)
        if user:
            return user
    return AnonymousUser()    
