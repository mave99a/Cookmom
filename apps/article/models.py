from google.appengine.ext import db
import datetime
from people.models import User
    
class Article(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True, )
    author = db.ReferenceProperty(User)
    
    # create time
    ctime = db.DateTimeProperty()   
    #last update time
    mtime = db.DateTimeProperty()    
    # language, for filtering and automatic translation support
    lang = db.StringProperty(required=True, default='en')
    
    published = db.BooleanProperty(default=False, required=True)
    
        