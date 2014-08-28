# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _
TIME_ZONE = 'Europe/Paris'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
import dj_database_url
import sys, urlparse

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if 'HEROKU' not in os.environ:
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'testdb2.sqlite',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
         'USER': '',
         'PASSWORD': '',
         'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
         'PORT': '',                      # Set to empty string for default.
     }
    }   

else:
    pass

# DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

LANGUAGE_CODE = 'fr'
SITE_ID = 1

MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'media'))
# MEDIA_ROOT = '/app/mysite/media/'



MEDIA_URL = '/media/'

# STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static_collected'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static')),
)



STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

SECRET_KEY = 'qd@j3*it@3j2cgc#7t@m)^r1bnc53uam7o6u_+x$f5w3$b@3ix'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
)

ROOT_URLCONF = 'example_bootstrap.urls'

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'templates')),
)

LOCALE_PATHS = ("/home/enigma/django_projects/iqcars/mysite/conf/locale/",)




INSTALLED_APPS = (
    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'suit',
    'django.contrib.admin',
    
    'pure_pagination',
    'car_shop',
    'dajaxice',
    'dajax',

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'car_shop.context_processors.strings',
)




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



# gmail settings
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "redatest7dev@gmail.com"
EMAIL_HOST_PASSWORD = 'redatest7'
EMAIL_PORT = 587

# django_registration settings

ACCOUNT_ACTIVATION_DAYS = 14


THUMBNAIL_DEBUG = False




SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Carshop Administration',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group','sites',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'label':'Authorization', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15

    # rename application



}


import logging.config
 
MAIN_DIR = os.path.dirname(__file__)
PROJECT_DIR = MAIN_DIR.rsplit(os.sep, 1)[0]

logging.config.fileConfig( os.path.join(PROJECT_DIR, 'configs', 'logging.conf'))


# this part must be add to python files that needs logging
import logging
logger = logging.getLogger(__name__)
logger.info("-------------- begin to crawl ---------------")




USE_I18N = True
USE_L10N = True
LANGUAGES = (
    ('fr', _('French')),
    ('en', _('English')),
    ('ar', _('Arabic')),
)
DEFAULT_LANGUAGE = 1


















