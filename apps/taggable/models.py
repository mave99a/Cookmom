from google.appengine.ext import db
    
class Taggable(db.Model):
    target = db.ReferenceProperty(db.Model)
    tags = db.StringListProperty()

    @classmethod
    def get_by_tag(cls, tag):
       return Taggable.all().filter('tags =', tag) 

    @classmethod
    def add_tags(cls, obj, tags):
       try: 
           taggable = (obj.taggable_set)[0]
           taggable.tags = tags
       except: 
           taggable = Taggable(target = obj, tags = tags)
       taggable.put()
       
    @classmethod
    def remove_tags(cls, obj, tags):
        try:
            taggable = (obj.taggable_set)[0]
            taggable.tags = []
            
            if len(taggable.tags) == 0 : 
                taggable.delete()
            else:
                taggable.put()
        except:
            pass
   
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
