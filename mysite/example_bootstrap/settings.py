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
         'ENGINE': 'django.db.backends.sqlite3', 
         'NAME': 'testdb2.sqlite',               
         
         'USER': '',
         'PASSWORD': '',
         'HOST': '',
         'PORT': '',
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

INSTALLED_APPS = (
    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',
    'pure_pagination',
    'car_shop',
    'dajaxice',
    'dajax',
    'registration',
    'profile',
    'article',
    'offre',
)



TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    # 'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    # 'django.core.context_processors.request',
    # 'car_shop.context_processors.strings',
    
)

FIXTURE_DIRS = (
      os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "fixtures")),
)

LOGIN_REDIRECT_URL = '/'

EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "redatest7dev@gmail.com"
EMAIL_HOST_PASSWORD = 'redatest7'
EMAIL_PORT = 587

ACCOUNT_ACTIVATION_DAYS = 14


# email_images = ( (os.path.join('static', 'images', 'logo1.png'), 'logo'),(os.path.join('static', 'images', 'logo1.png'), 'logo') )

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



LANGUAGE_CODE = 'fr'

USE_I18N = False
USE_L10N = False


















