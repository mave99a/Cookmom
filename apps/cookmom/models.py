from google.appengine.ext import db
import datetime

class Ingredient(db.Model):
    name = db.StringProperty(required = True)
    
class Reciepe(db.Model):
    # basic information
    name = db.StringProperty(required = True)
    ctime = db.DateTimeProperty()
    mtime = db.DateTimeProperty()
    
    # ingredients, many-to-many relationship, use list of db.Key 
    ingredients = db.ListProperty(db.Key)
    
    def save(self):
        now = datetime.datetime.now()
        if self.ctime is None:
            self.ctime = now
        self.mtime = now
        db.Model.save(self)
        
    