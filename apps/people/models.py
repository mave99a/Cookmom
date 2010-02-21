from google.appengine.ext import db
from django.db import models

class User(db.Model):
    name = db.StringProperty(required=True)
    img = db.StringProperty()
    brief = db.StringProperty()
    geopt = db.GeoPtProperty()
    city = db.StringProperty()
    # create time
    ctime = db.DateTimeProperty(auto_now_add=True)   
    #last update time
    mtime = db.DateTimeProperty(auto_now=True)    
    # language, for filtering and automatic translation support
    lang = db.StringProperty(required=True, default='en')
        
    def id(self):
        return self.key().id()
    
    @models.permalink
    def get_absolute_url(self):
        return ('people.views.show_user', [self.id()])
    
    @classmethod
    def create(cls, name, imgjson):
        user = User(name=name, img=imgjson)
        user.put()
        return user
    
def create_new_user_profile(name, imgjson):
    return User.create(name, imgjson)