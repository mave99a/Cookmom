from google.appengine.ext import db
import datetime
        
# main recipe table        
class Recipe(db.Model):
    # basic information
    name = db.StringProperty(required = True)
    ctime = db.DateTimeProperty()
    mtime = db.DateTimeProperty()
    
    #
    author = db.StringProperty()
    photo = db.StringProperty()
    
    # should be commentable, taggable, rankable
    
    def save(self):
        now = datetime.datetime.now()
        if self.ctime is None:
            self.ctime = now
        self.mtime = now
        db.Model.save(self)
        
 # the ingredients in a recipe
class Ingredient(db.Model):
    recipe = db.ReferenceProperty(Recipe, collection_name='Ingredients')
    name = db.StringProperty(required = True)
    unit = db.StringProperty()
    volume = db.FloatProperty(default = 0.0)

# detail description of recipe contents
class Details(db.Model):
    recipe = db.ReferenceProperty(Recipe)
    # content of the recipe
    content = db.StringProperty() 
    
    # photos of recipe  
    photos = db.ListProperty(db.Key)
    
    # video   
    # links
    # References
    
# wiki photo module:  a module allow user upload photos, and each photo will have an id, can be used as {{photo:id}} anywhere else. 
    