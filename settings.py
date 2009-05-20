# -*- coding: utf-8 -*-
import os
import sys

#  add 'libs' and 'apps' to python path. 
currentpath = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(currentpath, "libs"))
sys.path.insert(0, os.path.join(currentpath, "apps"))

from ragendja.settings_pre import *

#####################################################################
# combine media

# Set default language without country code
# (LANGUAGE_CODE must be contained in LANGUAGES)
LANGUAGE_CODE = 'en'

# Only generate media files for English and German
LANGUAGES = (
    ('en', 'English'),
)

# Combine media files
COMBINE_MEDIA = {
    # Create a combined JS file which is called "combined-en.js" for English,
    # "combined-de.js" for German, and so on
    'combined-%(LANGUAGE_CODE)s.js': (
        # Integrate morecode.js from "media" under project root folder
        'global/js/cufon-yui.js',
        'global/js/Edwardian_Script_ITC_400.font.js',
    ),
    # Create a combined CSS file which is called "combined-ltr.css" for
    # left-to-right text direction
    'combined-%(LANGUAGE_DIR)s.css': (
        # Load layout for the correct text direction
        'global/css/cookmom.css',
    ),
}

# Increase this when you update your media on the production site, so users
# don't have to refresh their cache. By setting this your MEDIA_URL
# automatically becomes /media/MEDIA_VERSION/
MEDIA_VERSION = 1

#####################################################################
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

#####################################################################
# Database 
DATABASE_ENGINE = 'appengine'  # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.

DATABASE_OPTIONS = {
    # Override remoteapi handler's path (default: '/remote_api').
    # This is a good idea, so you make it not too easy for hackers. ;)
    # Don't forget to also update your app.yaml!
    'remote_url': '/secret_remote_api',

    # !!!Normally, the following settings should not be used!!!

    # Always use remoteapi (no need to add manage.py --remote option)
    'use_remote': True,

    # Change appid for remote connection (by default it's the same as in your app.yaml)
    'remote_id': 'cookmom-app',

    # Change domain (default: <remoteid>.appspot.com)
    'remote_id': 'cookmom-app',
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'cookmom.com secret key'

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates')
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'ragendja.template.app_prefixed_loader',
#     'django.template.loaders.eggs.load_template_source',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',  
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Django authentication
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Google authentication
    'ragendja.auth.middleware.GoogleAuthenticationMiddleware',
    # Hybrid Django/Google authentication
    #'ragendja.auth.middleware.HybridAuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

# Google authentication
AUTH_USER_MODULE = 'ragendja.auth.google_models'
AUTH_ADMIN_MODULE = 'ragendja.auth.google_admin'
# Hybrid Django/Google authentication
#AUTH_USER_MODULE = 'ragendja.auth.hybrid_models'

GLOBALTAGS = (
    'ragendja.templatetags.ragendjatags',
    'ragendja.templatetags.googletags',    
    'django.templatetags.i18n',
    'sitemesh.templatetags.sitemesh',
)

LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sites',
    'appenginepatcher',
    'mediautils',
    
    # javascripts lib, css framework
    'jquerylib',
    'blueprintcss',
          
    'directtemplate',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
)

from ragendja.settings_post import *
