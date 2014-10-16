# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy as _
TIME_ZONE = 'Europe/Paris'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
import dj_database_url
import sys, urlparse

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# settings for heroku database
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}


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
    'suit',
    'django.contrib.admin',
    'pure_pagination',
    'car_shop',
    'dajaxice',
    'dajax',
    'registration',
    'profile',
    'article',
    'offre',
    'django_forms_bootstrap',
    'crispy_forms',
    'payments',
    'main',
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
     # "payments.settings",
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


SUIT_CONFIG = {
    'ADMIN_NAME': 'SpeedJob administration',
    'SHOW_REQUIRED_ASTERISK': True,

    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },

    'MENU_OPEN_FIRST_CHILD': True, 

    # 'MENU_EXCLUDE': ('auth.group','sites',),

    'MENU': (
        'sites',
        '-',
        {'app': 'auth',     'label':'Utilisateurs avancés', 'icon':'icon-lock',     'models': ('user', 'group')},
        '-',
        {'app': 'profile',  'label':'Profiles',             'icon':'icon-user',     'models': ('profile_emp','profile_candid', 'application') },
        '-',
        {'app': 'offre',    'label':'Offres',               'icon':'icon-envelope', 'models': ('offer',) },
        '-',
        {'app': 'article',  'label':'Article',              'icon':'icon-book',     'models': ('article',) },
        '-',
        
    ),

}


CACHE_TIMEOUT = 60*60

# CACHE_TABLE = 'db://cached_results'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cached_results',
    }
}


TEST_SECRET_KEY      = "sk_test_mopWUvH81IrewEKfXKN9e6rq"
TEST_PUBLISHABLE_KEY = "pk_test_v9t1PMYuYgsUM5Zsoj3uFn2b"

STRIPE_SECRET_KEY    = "sk_live_BFVMgVwzXLBU8CniUPILuLyo"
STRIPE_PUBLIC_KEY    = "pk_test_v9t1PMYuYgsUM5Zsoj3uFn2b"
# STRIPE_PUBLIC_KEY = "pk_live_vB5KieclNbIxLgERKibtEvH8"


# LIVE_SECRET_KEY      = "sk_live_BFVMgVwzXLBU8CniUPILuLyo"
# LIVE_PUBLISHABLE_KEY = "pk_live_vB5KieclNbIxLgERKibtEvH8"




# PAYMENTS_PLANS = {
#     "yearly": {
#         "stripe_plan_id": "yearly",
#         "name": "yearly",
#         # "description": "The monthly subscription plan to WebApp",
#         "price": 0.99,
#         "currency": "usd",
#         "interval": "month",
#         "trial_period_days": 15
#     }
# }

# PAYMENTS_PLANS = {
#     "monthly": {
#         "stripe_plan_id": "pro-monthly",
#         "name": "Web App Pro ($25/month)",
#         # "description": "The monthly subscription plan to WebApp",
#         "price": 25,
#         "currency": "usd",
#         "trial_period_days": 15,
#         "interval": "month"
#     },
#     "yearly": {
#         "stripe_plan_id": "pro-yearly",
#         "name": "Web App Pro ($199/year)",
#         # "description": "The annual subscription plan to WebApp",
#         "price": 199,
#         "currency": "usd",
#         "trial_period_days": 15,
#         "interval": "year"
#     }
# }

PAYMENTS_PLANS = {
    "normal": {
        "stripe_plan_id": "normal",
        "name": "Monthly Potato Delivery",
        "description": "Monthly potato delivery to your door.",
        "price": 15,
        "currency": "gbp",
        "trial_period_days": 0,
        "interval": "month"
    },

    "premier": {
        "stripe_plan_id": "premier",
        "name": "Monthly Premier Potato Delivery",
        "description": "Monthly PREMIER potato delivery to your door.",
        "price": 30,
        "currency": "gbp",
        "trial_period_days": 0,
        "interval": "month",
    },
}


TRIAL_PERIOD_FOR_USER_CALLBACK = 15


# Set these, or include them in an untracked locals.py
# STRIPE_PUBLISHABLE = None
# STRIPE_SECRET = None

try:
    from local_settings import *
except ImportError:
    pass
