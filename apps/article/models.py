from google.appengine.ext import db
import datetime
from people.models import User
from django import forms
    
class Article(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    author = db.ReferenceProperty(User)
    
    # create time
    ctime = db.DateTimeProperty(auto_now_add=True)   
    #last update time
    mtime = db.DateTimeProperty(auto_now=True)    
    # language, for filtering and automatic translation support
    lang = db.StringProperty(required=True, default='en')
    
    published = db.BooleanProperty(default=False, required=True)
    
    slug = db.StringProperty(required=True)
    
    # some cached properties for performance improving
    read_count = db.IntegerProperty(default=0)
    comment_count = db.IntegerProperty(default=0)
    img_url_big = db.StringProperty()
    img_url_small = db.StringProperty()
    
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author', 'ctime', 'mtime', 'lang', 'published')        