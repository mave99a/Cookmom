# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import delete_object, update_object
from django.contrib.auth.decorators import login_required
from generic_view_patch.create_update import create_object
from models import Article, ArticleForm

from people.models import User

def list_article(request):
    return object_list(request, Article.all(), paginate_by = 10)

def show_article(request, key):
    return object_detail(request, Article.all(), key)

@login_required
def new_article(request):
    return create_object(request, form_class=ArticleForm,
        extra_fields = {'author': User.get_current_user()}, 
        post_save_redirect=reverse(show_article,
                                   kwargs=dict(key='%(key)s')))
@login_required
def edit_article(request, key):
    return update_object(request, object_id=key, form_class=ArticleForm,
        post_save_redirect=reverse(show_article,
                                   kwargs=dict(key='%(key)s')))
@login_required
def delete_article(request, key):
    return delete_object(request, Article, object_id=key,
        post_delete_redirect=reverse(list_article))    