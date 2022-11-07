"""
Django settings for ProjectAutomation project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w6d87uzs=5e()6i$d_*g1cpt)7^dpjtwnub&e&oy5y3l=3wutr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AutomationApp',
    'whitenoise.runserver_nostatic',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'ProjectAutomation.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                

            ],
        },
    },
]



WSGI_APPLICATION = 'ProjectAutomation.wsgi.application'
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
import dj_database_url
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'firstapp',
        'USER': 'postgres',
        'PASSWORD': '0918382947kJ',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
#db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'] = dj_database_url.parse('postgres://postgres:0918382947kJ@localhost:5432/firstapp', conn_max_age=600)

#DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
    ]

STATIC_ROOT = os.path.join(BASE_DIR,'assets')


MEDIA_URL = '/media/'
MEDIAFILES_DIRS=[
    os.path.join(BASE_DIR,'media')
    ]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
django_heroku.settings(locals())
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKEND = {
#needed to login with username in django admin, regardless of allauth
'django.contrib.auth.backends.ModelBackend',

# 'allauth' specific application methods, such as login by email
'allauth.account.auth_backends.AUTHENTICATION_BACKEND',

}


SITE_ID=1
ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'
ACCOUNT_LOGOUT_REDIRECT_URL ='../../index/onlineorder/4' 
#ACCOUNT_ADAPTER = 'app.my_adapter.MyAccountAdapter'
#LOGIN_REDIRECT_URL = 'next'
#LOGIN_REDIRECT_URL = 'request.path_info'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'js_sdk',
        'SCOPE': ['public_profile, email'],
        'AUTH_PARAMS': {'auth_type': 'reauthorize'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'name',
            'email',
            'short_name',
            'first_name',
            'last_name',
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
    }
}
