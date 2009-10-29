from google.appengine.ext import db
import datetime

class Article(db.Model):
    title = db.StringProperty(required=True)
    content = db.StringProperty(required=True)
    