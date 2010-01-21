from google.appengine.ext import db

class User(db.Model):
    name = db.StringProperty(required=True)
    img = db.StringProperty()
    
    @classmethod 
    def get_current_user(cls):
        user = User.all().filter("name =", "Cookmom").get()
        if user is None :
            user = User(name="Cookmom", img="1")
            user.put()
        return user