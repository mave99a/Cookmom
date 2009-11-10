from google.appengine.ext import db
import datetime
from people.models import User
from django import forms
    
class Article(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True, )
    author = db.ReferenceProperty(User)
    
    # create time
    ctime = db.DateTimeProperty(auto_now_add=True)   
    #last update time
    mtime = db.DateTimeProperty(auto_now=True)    
    # language, for filtering and automatic translation support
    lang = db.StringProperty(required=True, default='en')
    
    published = db.BooleanProperty(default=False, required=True)
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author', 'ctime', 'mtime', 'lang', 'published')        