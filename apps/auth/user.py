from google.appengine.api import users
from google.appengine.ext import db
from people.models import create_new_user_profile
class AnonymousUser: 
    def is_authenticated(self):   
        return False
    def loginurl(self):
        return users.create_login_url('/')
    
    def logouturl(self):
        return users.create_logout_url('/')
    
    def user(self):        
        return None
    
    def name(self):
        return 'Guest'
    
    def email(self):
        return '@'
            
class GoogleUser(db.Model):     
    user = db.ReferenceProperty(db.Model, required=True)
    googleuser = db.UserProperty(required=True)

        
    def is_authenticated(self):   
        return True
    
    @classmethod
    def getUser(cls, request):
        googleuser = users.get_current_user() 
        if googleuser:
            result = GoogleUser.all().filter('googleuser =', googleuser).get()
            if result is None:
                newuser = create_new_user_profile(googleuser.nickname())
                result = GoogleUser(user=newuser, googleuser = googleuser)
                result.put()
            return result    
        else:
            return None
    
    def loginurl(self):
        return users.create_login_url('/')
    
    def logouturl(self):
        return users.create_logout_url('/')
    
    def name(self):
        return self.googleuser.nickname()
    
    def email(self):
        return self.googleuser.email()
    
class FacebookUser(db.Model):
    user = db.ReferenceProperty(db.Model, required=True)
    fbuid = db.StringProperty(required=True)
        
    @classmethod
    def getUser(cls, request):
        if getattr(request, 'facebook', None):
            fb = request.facebook
            if fb.check_session(request):                        
                result = FacebookUser.all().filter('fbuid =', fb.uid).get()
                if result is None:
                    newuser = create_new_user_profile(fb.uid)
                    result = FacebookUser(user=newuser, fbuid = fb.uid)
                    result.put()
                return result   
        return None
        
    def is_authenticated(self):   
        return True
             
    def loginurl(self):
        pass
    
    def logouturl(self):
        pass

    def name(self):
        return self.fbuid
    
    def email(self):
        return self.fbuid
    
def get_current_user(request):
    AuthMethods = [FacebookUser, GoogleUser]
    for method in AuthMethods:
        user = method.getUser(request)
        if user:
            return user
    return AnonymousUser()    
