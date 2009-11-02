from google.appengine.ext import db
import datetime
from people.models import User
    
class Comment(db.Model):
    target = db.ReferenceProperty(db.Model, collection_name='Comments')
    content = db.TextProperty(required=True, )
    author = db.ReferenceProperty(User)
    
    # create time
    ctime = db.DateTimeProperty()   
    #last update time
    mtime = db.DateTimeProperty()    
    # language, for filtering and automatic translation support
    lang = db.StringProperty(required=True, default='en')

        