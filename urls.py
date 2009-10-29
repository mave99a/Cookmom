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
from article import views
admin.autodiscover()

urlpatterns = patterns('',
    (r'^article/$', views.list_article), 
    (r'^article/(?P<key>.+)$', views.show_article), 
    (r'^(.*)$', directtemplate),     
) + urlpatterns
