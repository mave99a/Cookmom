# -*- coding: utf-8 -*-
from django import forms
from ragendja.forms import FormWithSets, FormSetField
from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import delete_object
from generic_view_patch.create_update import update_object
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import User
from auth.decorators import login_required


def list_user(request):
    return object_list(request, User.all(), paginate_by=10)

def show_user(request, id):
    return show_user_detail(request, id)

def show_user_detail(request, id, obj=None):
    try: 
        is_self = (int(id) == request.current_user.id())
    except: 
        is_self = False;
        
    if obj is not None: 
        template='people/user_detail_' + obj + '.html'
    else:
        template = None;
    return object_detail(request, User.all(), object_id=id, template_name=template, extra_context={'is_self': is_self})

@login_required
def show_myhome(request):
    return HttpResponseRedirect(reverse(show_user, args =[request.current_user.id()]))


class UserFormAbout(forms.ModelForm):    
    class Meta:
        model = User
        fields = ('name', 'brief', 'city', 'show_my_location')

class UserFormImage(forms.ModelForm):    
    class Meta:
        model = User
        fields = ('img', 'img')

@login_required
def show_settings(request):
    return update_object(request, object_id=request.current_user.id(), form_class=UserFormAbout, template_name='people/settings/about.html')

@login_required
def show_settings_profileimage(request):
    return update_object(request, object_id=request.current_user.id(), form_class=UserFormImage, template_name='people/settings/profileimage.html')

@login_required
def show_settings_linkedservices(request):
    return update_object(request, object_id=request.current_user.id(), form_class=UserFormImage, template_name='people/settings/linkedservices.html')
    