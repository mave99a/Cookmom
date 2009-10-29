# -*- coding: utf-8 -*-
from django import forms
from ragendja.forms import FormWithSets, FormSetField
from django.core.urlresolvers import reverse

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, update_object
from models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
ArticleForm = FormWithSets(ArticleForm)


def list_article(request):
    return object_list(request, Article.all(), paginate_by=10)

def show_article(request, key):
    return object_detail(request, Article.all(), key)

def new_article(request):
    return create_object(request, form_class=ArticleForm,
        post_save_redirect=reverse(show_article,
                                   kwargs=dict(key='%(key)s')))
def edit_article(request, key):
    return update_object(request, object_id=key, form_class=ArticleForm,
        post_save_redirect=reverse(show_article,
                                   kwargs=dict(key='%(key)s')))
def delete_article(request, key):
    return delete_object(request, Article, object_id=key,
        post_delete_redirect=reverse(list_article))    