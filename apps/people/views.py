# -*- coding: utf-8 -*-
from django import forms
from ragendja.forms import FormWithSets, FormSetField
from django.core.urlresolvers import reverse

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, update_object
from models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
UserForm = FormWithSets(UserForm)


def list_user(request):
    return object_list(request, User.all(), paginate_by=10)

def show_user(request, key):
    return object_detail(request, User.all(), key)

def new_user(request):
    return create_object(request, form_class=UserForm,
        post_save_redirect=reverse(show_user,
                                   kwargs=dict(key='%(key)s')))
def edit_user(request, key):
    return update_object(request, object_id=key, form_class=UserForm,
        post_save_redirect=reverse(show_user,
                                   kwargs=dict(key='%(key)s')))
def delete_user(request, key):
    return delete_object(request, User, object_id=key,
        post_delete_redirect=reverse(list_user))    