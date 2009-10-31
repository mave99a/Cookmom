from google.appengine.ext import db
import datetime
from people.models import User
    
class Article(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True, )
    author = db.ReferenceProperty(User)