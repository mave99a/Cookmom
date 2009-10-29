from google.appengine.ext import db
import datetime

class Author(db.Model):
    name = db.StringProperty(required=True)
    
class Article(db.Model):
    title = db.StringProperty(required=True)
    content = db.StringProperty(required=True)
    author = db.ReferenceProperty(Author)