# -*- coding: utf-8 -*-
from django.http import HttpResponse
from models import upload_to_flickr

from google.appengine.api import memcache


def upload(request):
    path = upload_to_flickr('test', request.FILES['Filedata'].read(), request.FILES['Filedata'].content_type)     
    return HttpResponse(path)
