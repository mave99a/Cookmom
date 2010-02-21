from django import template
from django.utils.html import escape
from django.contrib.auth.models import User

import urllib, hashlib

register = template.Library()

def gravatar(email, size=80, default_img = None):
        
    gravatar_url = "http://www.gravatar.com/avatar.php?"
    gravatar_url += urllib.urlencode({'gravatar_id':hashlib.md5(email).hexdigest(), 'default': default_img, 'size':str(size)})
    return gravatar_url

register.simple_tag(gravatar)
