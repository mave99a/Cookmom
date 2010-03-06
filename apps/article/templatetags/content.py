from django.template.defaultfilters import stringfilter
from django import template
from django.template import Template
import re

register = template.Library()

r = re.compile('(?P<photo>\[photo (?P<id>\d+)\])')

def replacePhotoTags(matchobj):
    return '<img src="{% imageurl ' + matchobj.group('id') + ' medium%}" />'

@register.filter
@stringfilter
def article_content(value):
    t = Template(r.sub(replacePhotoTags, value))
    return t.render({})
    

