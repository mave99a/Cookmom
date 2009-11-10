from google.appengine.ext import db

class User(db.Model):
    name = db.StringProperty(required=True)
    img_url = db.StringProperty()