# -*- coding: utf-8 -*-
from google.appengine.ext import db
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail
from django.http import HttpResponse
from models import *

def tagcloud(request):
    return object_list(request, Tag.cloud(100))
    
def show_by_tag(request, tag):
    return object_list(request, Taggable.get_by_tag(tag), paginate_by = 10, 
                       extra_context={'tag':tag})

@login_required
def add_tags(request):
    key = request.REQUEST["target"]
    tags = request.REQUEST["tags"].split(',')
    obj = db.get(key)
    Taggable.add_tags(obj, tags)
    return HttpResponse('[]')

@login_required
def remove_tags(request):
    key = request.REQUEST["target"]
    tags = request.REQUEST["tags"].split(',')
    obj = db.get(key)
    Taggable.remove_tags(obj, tags)
    return HttpResponse('ok')


@login_required
def my_tags(request):
   return  HttpResponse('ok')