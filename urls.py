# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import default app urlpatterns, enable automatic url from apps
from ragendja.urlsauto import urlpatterns

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from directtemplate.views import directtemplate 
import article.views
from article.models import Article, ArticleForm
from comment.models import Comment, CommentForm
from django.core.urlresolvers import reverse

import people.views
admin.autodiscover()

from people.models import User
u = User(name='Bull Shitter', img_url='http://a1.twimg.com/profile_images/205153778/Suzie_0001s_normal.jpg')
u.put()

urlpatterns = patterns('',
    (r'^people/$', people.views.list_user), 
    (r'^people/new/$', people.views.new_user), 
    (r'^people/(?P<key>.+)/edit/$', people.views.edit_user),
    (r'^people/(?P<key>.+)/dele/$', people.views.delete_user), 
    (r'^people/(?P<key>.+)$', people.views.show_user), 

    (r'^article/$', 'django.views.generic.list_detail.object_list', {'paginate_by':10, 'queryset': Article.all()}), 
    (r'^article/new/$', article.views.new_article), 
    (r'^article/(?P<key>.+)/edit/$', article.views.edit_article),
    (r'^article/(?P<key>.+)/dele/$', article.views.delete_article), 
    (r'^article/(?P<key>.+)$', article.views.show_article), 
    
    (r'^comment/$', 'django.views.generic.list_detail.object_list', {'paginate_by':10, 'queryset': Comment.all()}), 
    (r'^comment/new/$', 'generic_view_patch.create_update.create_object', {'form_class':CommentForm, 'extra_fields':{'author':u}, 'post_save_redirect': '/comment/'}), 
    
    (r'^(.*)$', directtemplate),     
) + urlpatterns
