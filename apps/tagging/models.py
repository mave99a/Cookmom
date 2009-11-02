from google.appengine.ext import db
import datetime
from people.models import User
    
class Taggable(db.Model):
    target = db.ReferenceProperty(db.Model, collection_name='Taggable')
    content = db.TextProperty(required=True, )
    tags = db.ListProperty(db.Key, required=True)


class Tag(db.Model):
    name = db.StringProperty(required = True)        
    
