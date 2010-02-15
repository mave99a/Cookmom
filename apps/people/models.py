from google.appengine.ext import db
from django.db import models

class User(db.Model):
    name = db.StringProperty(required=True)
    slug = db.StringProperty()
    img = db.StringProperty()
    
    def id(self):
        return self.key().id()
    
    @models.permalink
    def get_absolute_url(self):
        return ('people.views.show_user', [self.id()])
    
    @classmethod 
    def get_current_user(cls):
        user = User.all().filter("name =", "Cookmom").get()
        if user is None :
            user = User(name="Cookmom", img="1")
            user.put()
        return user