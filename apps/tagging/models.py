from google.appengine.ext import db
    
class Taggable():
    tags = db.StringListProperty()


class Tag(db.Model):
    name = db.StringProperty(required = True)      
    count = db.IntegerProperty(default = 0)
    # create time
    ctime = db.DateTimeProperty(auto_now_add=True)   
    #last update time
    mtime = db.DateTimeProperty(auto_now=True)    
    # language, for filtering and automatic translation support
    lang = db.StringProperty(required=True, default='en')    
    
class UserTag(Tag):
    pass
