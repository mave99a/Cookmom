from google.appengine.ext import db
from django.db import models

class User(db.Model):
    name = db.StringProperty(required=True)
    img = db.StringProperty()
    brief = db.StringProperty()
    geopt = db.GeoPtProperty()
    city = db.StringProperty()
    
    def id(self):
        return self.key().id()
    
    @models.permalink
    def get_absolute_url(self):
        return ('people.views.show_user', [self.id()])
    
    @classmethod
    def create(cls, name):
        user = User(name=name, img='2')
        user.put()
        return user
    
def create_new_user_profile(name):
    return User.create(name)