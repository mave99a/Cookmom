from google.appengine.ext import db
import datetime
from people.models import User
from django import forms
from django.core.urlresolvers import reverse
from django.db import models
    
class Article(db.Model):
    title = db.StringProperty()
    content = db.TextProperty()
    author = db.ReferenceProperty(User, required=True)
    
    # create time
    ctime = db.DateTimeProperty(auto_now_add=True)   
    #last update time
    mtime = db.DateTimeProperty(auto_now=True)    
    # language, for filtering and automatic translation support
    lang = db.StringProperty(required=True, default='en')
    
    published = db.BooleanProperty(default=False, required=True)
        
    # some cached properties for performance improving
    read_count = db.IntegerProperty(default=0)
    comment_count = db.IntegerProperty(default=0)
    
    images_list = db.StringListProperty()
    
    def id(self):
        return self.key().id()
    
    def image(self):
        '''return the main image of this article'''
        try:
            return self.images_list[0] 
        except:
            return '0'
        
    @models.permalink
    def get_absolute_url(self):
        return ('article.views.show_article', [self.id(), self.title])
        
    @classmethod
    def get_featured(cls):
        featured = Article.all().fetch(1)
        return featured
    
    @classmethod
    def get_top(cls):
        top = Article.all().fetch(6)
        return top
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author', 'ctime', 'mtime', 'lang', 'published', 'read_count', 'comment_count')        