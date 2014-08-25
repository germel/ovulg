"""
Django settings for ovulg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#a*#xi+e2mp*@uyf-dw&=y%-7b8=%2-(z-jw6b2-u*fxn3zs4j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'bootstrap3',
    'nscan',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ovulg.urls'

WSGI_APPLICATION = 'ovulg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ovulg',
	'USER': 'vulgar',
	'PASSWORD': 'mitsos1',
	'HOST': '',
	'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# The following stanza came from http://www.djangofoo.com/35/template_dirs-project-folder
import os.path
PROJECT_DIR = os.path.dirname(__file__) # this is not Django setting.
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
    os.path.join(PROJECT_DIR, "templates"),
    # here you can add another templates directory if you wish.
)

#TEMPLATE_DIRS = 'templates'

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Configure some session related variables
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/tmp'

