
from pathlib import Path
import os, sys
from decouple import config
from pythonjsonlogger.jsonlogger import JsonFormatter


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True

ALLOWED_HOSTS = ['website555.herokuapp.com', 'localhost']

CSRF_TRUSTED_ORIGINS = ['https://website555.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'django_celery_beat',

    # 'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

    'ckeditor',
    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_auth',
    # 'drf_yasg',
    'rest_framework_swagger',
    'users',
    'posts',
    'api_view',
    'api_url',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',  # <-- Here
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR/ 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',

                # 'social_django.context_processors.backends',  # <-- Here
                # 'social_django.context_processors.login_redirect', # <-- Here
            ],
            'libraries' : {
                'staticfiles': 'django.templatetags.static',
            } #rest_framework_swagger
        },
    },
]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'website.wsgi.application'

SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Swagger

REST_FRAMEWORK = { 
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' ,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
# STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "home"

# SOCIAL_AUTH_FACEBOOK_KEY = '414125360753045'
# SOCIAL_AUTH_FACEBOOK_SECRET = '7bda9ffc206ea80864a917731d8eccc8'


MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'prithvi.thoughtwin@gmail.com'
EMAIL_HOST_PASSWORD = 'cxlhjoivnqsrjaeu'
EMAIL_USE_TLS = True

# Loggers

import os
from posts.logger_jsonformat import CustomJsonFormatter

# LOGGING = {
#     'version' : 1,
#     'disable_existing_loggers': False,
#     'loggers' : {
#         'django' : {
#             'handlers' : ['debughandler', 'infohandler', 'warninghandler', 'errorhandler'],
#             'level' : 'DEBUG',
#             'filters' : ['require_debug_true'],
#         },
#         'main' : {
#             'handlers' : ['file'],
#             'level' : 'INFO',
#             'filters' : ['require_debug_true'],
#         },
#         'django.request' : {
#             'handlers' : ['debughandler2'],
#             'level' : 'INFO',
#             'propagate': False,
#         },
#     },
#     'handlers' : {
#         'debughandler' : {
#             'level' : 'DEBUG',
#             'class' : 'logging.FileHandler',
#             'filename' : './website/logs/debug.log',
#             'formatter' : 'verbose'
#         },
#         'debughandler2' : {
#             'level' : 'INFO',
#             'class' : 'logging.StreamHandler', #Printing the logs on Console
#             'formatter' : 'verbose'
#         },
#         'file' : {
#             'level' : 'INFO',
#             'class' : 'logging.FileHandler',
#             'filename' : './website/logs/websiteinfo.log',
#             'formatter' : 'json'
#         },
#         'infohandler' : {
#             'level' : 'INFO',
#             'class' : 'logging.FileHandler',
#             'filename' : './website/logs/info.log',
#             'formatter' : 'verbose'
#         },
#         'warninghandler' : {
#             'level' : 'WARNING',
#             'class' : 'logging.FileHandler',
#             'filename' : './website/logs/warning.log',
#             'formatter' : 'verbose'
#         },
#         'errorhandler' : {
#             'level' : 'ERROR',
#             'class' : 'logging.FileHandler',
#             'filename' : './website/logs/error.log',
#             'formatter' : 'verbose'
#         }
#     },
#     'filters': {
#         'require_debug_true': {
#         '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'formatters' : {
#         'verbose' : {
#             'format' : '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style' : '{',
#         },
#         'simple' : {
#             'format' : '{levelname} - {asctime} - {module} - {message}',
#             'style' : '{',
#         },
#         'json' : {
#             '()' : CustomJsonFormatter,
#         },
#     }
# }


# Sentry

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# sentry_sdk.init(
#     dsn="https://eb8c503d9a364e9887d952fdb3a640cc@o1335090.ingest.sentry.io/6602536",
#     integrations=[
#         DjangoIntegration(),
#     ],

#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0,

#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )


# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#     },
#     'facebook': {
#         'METHOD': 'oauth2',
#         # 'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
#         'SCOPE': ['email', 'public_profile'],
#         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#         'INIT_PARAMS': {'cookie': True},
#         'FIELDS': [
#             'id',
#             'first_name',
#             'last_name',
#             'middle_name',
#             'name',
#             'name_format',
#             'picture',
#             'short_name'
#         ],
#         'EXCHANGE_TOKEN': True,
#         # 'LOCALE_FUNC': 'path.to.callable',
#         'VERIFIED_EMAIL': False,
#         'VERSION': 'v13.0',
#     },
#     'github': {
#         'SCOPE': [
#             'user',
#             'repo',
#             'read:org',
#         ],
#     },
# }

# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'


# # CELERY STUFF
# BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Kolkata'