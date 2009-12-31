from google.appengine.ext import db

class User(db.Model):
    name = db.StringProperty(required=True)
    img_url = db.StringProperty()
    
    @classmethod 
    def get_current_user(cls):
        user = User.all().filter("name =", "Test").get()
        if user is None :
            user = User(name="Test", img_url="http://a3.twimg.com/profile_images/374652761/IMG_6122_2_bigger.JPG")
            user.put()
        return user