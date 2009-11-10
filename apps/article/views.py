# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import delete_object, update_object
from generic_view_patch.create_update import create_object
from models import Article, ArticleForm

from people.models import User

u = User(name='Stupider', img_url='http://a3.twimg.com/profile_images/374652761/IMG_6122_2_bigger.JPG')
u.put()

def show_article(request, key):
    return object_detail(request, Article.all(), key)

def new_article(request):
    return create_object(request, form_class=ArticleForm,
        extra_fields = {'author': u}, 
        post_save_redirect=reverse(show_article,
                                   kwargs=dict(key='%(key)s')))
def edit_article(request, key):
    return update_object(request, object_id=key, form_class=ArticleForm,
        post_save_redirect=reverse(show_article,
                                   kwargs=dict(key='%(key)s')))
def delete_article(request, key):
    return delete_object(request, Article, object_id=key,
        post_delete_redirect=reverse(list_article))    