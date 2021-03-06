"""
Django settings for mercury project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import logging
import logging.handlers
from django.utils.six import moves

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

CONFIG = moves.configparser.SafeConfigParser(allow_no_value=True)
CONFIG.read('%s\settings.cfg' % SETTINGS_DIR)


LOG_FILENAME = os.path.join(PROJECT_PATH, 'logs/mercury.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] | %(levelname)s [%(name)s:%(lineno)s] | %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'timedrotatingfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOG_FILENAME,
            'formatter': 'verbose',
            'when': 'midnight',
            'backupCount': 14
        },
    },
    'loggers': {
        'django': {
            'handlers': ['timedrotatingfile'],
            'propagate': True,
            'level': 'INFO',
        },
        'rest_framework': {
            'handlers': ['timedrotatingfile'],
            'propagate': True,
            'level': 'INFO',
        },
        'mercury': {
            'handlers': ['timedrotatingfile'],
            'level': 'INFO',
        },
        'mercuryservices': {
            'handlers': ['timedrotatingfile'],
            'level': 'INFO',
        },
        'merlin': {
            'handlers': ['timedrotatingfile'],
            'level': 'INFO',
        },
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('security', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CONFIG.get('general', 'DEBUG')

TEMPLATE_DEBUG = CONFIG.get('general', 'TEMPLATE_DEBUG')

ALLOWED_HOSTS = CONFIG.get('general', 'ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'rest_framework_swagger',
    'corsheaders',
    'mercuryservices',
    'merlin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF = 'mercury.urls'

WSGI_APPLICATION = 'mercury.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': CONFIG.get('databases', 'ENGINE'),
        'NAME': CONFIG.get('databases', 'NAME'),
        'USER': CONFIG.get('databases', 'USER'),
        'PASSWORD': CONFIG.get('databases', 'PASSWORD'),
        'HOST': CONFIG.get('databases', 'HOST'),
        'PORT': CONFIG.get('databases', 'PORT'),
        #'CONN_MAX_AGE': CONFIG.get('databases', 'CONN_MAX_AGE'),
        'CONN_MAX_AGE': 60,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static/staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

SWAGGER_SETTINGS = {
    "info": {
        'description': 'This is the documentation site for the MeRLIn '
                       '(Mercury Research Lab Information Management System) REST Services.',
        'title': 'MeRLIn REST Services Documentation',
    },
    "exclude_namespaces": ["mercuryauth"],
}

SUIT_CONFIG = {
    'ADMIN_NAME': 'Mercury Lab Admin',
}

CORS_ORIGIN_ALLOW_ALL = True

LOGIN_URL = '/merlin/login/'