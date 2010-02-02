# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from models import upload_to_flickr

#
def upload(request):
    path = upload_to_flickr(str(request.FILES['Filedata'].name), request.FILES['Filedata'].read(), request.FILES['Filedata'].content_type)     
    return HttpResponse(path)

