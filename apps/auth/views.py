# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

def login(request):
    return render_to_response('auth/login.html',
                              {},
                              context_instance=RequestContext(request))

def logout(request):
    return render_to_response('auth/logout.html',
                              {},
                              context_instance=RequestContext(request))    