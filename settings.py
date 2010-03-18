# -*- coding: utf-8 -*-

from facebooksettings import *
from flickrsettings import * 

import os
import sys
import flickrsettings 
import datetime

#  add 'libs' and 'apps' to python path. 
currentpath = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(currentpath, "libs"))
sys.path.insert(0, os.path.join(currentpath, "apps"))
sys.path.insert(0, os.path.join(currentpath, "common/appenginepatch"))
ROOT_URLCONF = 'urls'

RUNNING_APP_ENGINE_LOCAL_SERVER = os.environ.get('SERVER_SOFTWARE', 'Dev').startswith('Dev') # set this to TRUE to get debug output

DEBUG = RUNNING_APP_ENGINE_LOCAL_SERVER # For now

TIME_HORIZON = datetime.timedelta(hours = 2)

APPEND_SLASH = True
 
# Increase this when you update your media on the production site, so users
# don't have to refresh their cache. By setting this your MEDIA_URL
# automatically becomes /media/MEDIA_VERSION/
MEDIA_VERSION = 1
DJANGO_STYLE_MODEL_KIND = False
# By hosting media on a different domain we can get a speedup (more parallel
# browser connections).
#if on_production_server or not have_appserver:
#    MEDIA_URL = 'http://media.mydomain.com/media/%d/'

# Combine media files
COMBINE_MEDIA = {
    # Create a combined JS file which is called "combined-en.js" for English,
    # "combined-de.js" for German, and so on
    'combined-%(LANGUAGE_CODE)s.js': (
        # Integrate morecode.js from "media" under project root folder
        'global/js/cufon-yui.js',
        'global/js/Edwardian_Script_ITC_400.font.js',
        
        # plugin for jquery
        'global/js/jquery.form.js', 
        'global/js/jquery.elastic.source.js',    #  from http://www.unwrongest.com/projects/elastic/
    ),
    # Create a combined CSS file which is called "combined-ltr.css" for
    # left-to-right text direction
    'combined-%(LANGUAGE_DIR)s.css': (
        # Load layout for the correct text direction
        'global/css/cookmom.css',
    ),
} 

# Change your email settings
    
# Make this unique, and don't share it with anybody.
SECRET_KEY = '4254425101'

#ENABLE_PROFILER = True
#ONLY_FORCED_PROFILE = True
#PROFILE_PERCENTAGE = 25
#SORT_PROFILE_RESULTS_BY = 'cumulative' # default is 'time'
# Profile only datastore calls
#PROFILE_PATTERN = 'ext.db..+\((?:get|get_by_key_name|fetch|count|put)\)'

# Enable I18N and set default language to 'en'
USE_I18N = True
LANGUAGE_CODE = 'en' 

# Restrict supported languages (and JS media generation)
LANGUAGES = (
    ('en', 'English'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'auth.context_processors.auth',
)

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), 'templates')]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

AUTHENTICATION_BACKENDS = None

MIDDLEWARE_CLASSES = (
    'appstats.recording.AppStatsDjangoMiddleware',  # appstats

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'facebook.djangofb.FacebookMiddleware',
    'auth.middleware.AuthMiddleware',
    # firepython for debug 
    #'firepython.middleware.FirePythonDjango',

)

INSTALLED_APPS = (
    # Add jquery support (app is in "common" folder). This automatically
    # adds jquery to your COMBINE_MEDIA['combined-%(LANGUAGE_CODE)s.js']
    # Note: the order of your INSTALLED_APPS specifies the order in which
    # your app-specific media files get combined, so jquery should normally
    # come first.
    # javascripts lib, css framework
    # 'jquerylib',    # we will use Google's CDN,  so won't include this app here. 
    'blueprintcss',
    'lightbox', 
          
    # tags
    'renderhelpers', 
    'paginatortag', 
    'objectlisttag', 
    
    # auth
    'auth',
     
    # app modules
    'cookmom',
    
    # general purpose apps 
    'people',   # every following app will depends on people app
    'article',
    'comment',
    'taggable', 
    'vote', 
    'search',
    
    'swfupload',        # app for swfupload integration
    'image',            # app to handle image upload and image url 
    'flickr',           # app for supportting flickr backend and flickr's auth
         
    # unit test tool app
    'gaeunit',
        
    # app engine patch    
    # 'appenginepatcher',
    'mediautils',
    'ragendja',
)

# register our tag as default, so we don't need to use "{%load ...%}" all the time
from django.template import add_to_builtins
add_to_builtins('auth.templatetags.authtags')
add_to_builtins('renderhelpers.templatetags.render')
add_to_builtins('image.templatetags.imageurl')
add_to_builtins('objectlisttag.templatetags.makeobjectlist')

