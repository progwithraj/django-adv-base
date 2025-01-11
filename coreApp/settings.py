"""
Django settings for coreApp project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import sys
from pathlib import Path
from datetime import timedelta

import dj_database_url
from dotenv import load_dotenv
from corsheaders.defaults import default_headers

from .utility import convert_string_to_list

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG")
DJANGO_ENV=os.environ.get("DJANGO_ENV")

ALLOWED_HOSTS = convert_string_to_list(os.environ.get("DJANGO_ALLOWED_HOSTS"))

# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders'
]

LOCAL_APPS = [
    # 'f_exp.apps.FExpConfig',
    # 'q_exp.apps.QExpConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DJANGO_ENV == "DEV":
    # if in dev, add whitenoise to disable collectstatic
    BASE_APPS.insert(0, "whitenoise.runserver_nostatic")
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

INSTALLED_APPS = [
    *BASE_APPS,
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

ROOT_URLCONF = 'coreApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'coreApp.wsgi.application'

# ALLOW AUTO APPEND SLASH
APPEND_SLASH = True

# supabase
SUPABASE_PROJECT_PASSWORD = os.environ.get("SUPABASE_PROJECT_PASSWORD")
SUPABASE_DB_URL = os.environ.get("SUPABASE_PROJECT_URI").format(
    SUPABASE_PROJECT_PASSWORD=SUPABASE_PROJECT_PASSWORD
)

# Database
SUPABASE_DB_CONFIG = dj_database_url.config(default=SUPABASE_DB_URL, conn_max_age=600,  conn_health_checks=True)

POSTGRES_DB_CONFIG = {
    'ENGINE': os.environ.get("DJANGO_DB_ENGINE"),
    'NAME': os.environ.get("DJANGO_DB_NAME"),
    'USER': os.environ.get("DJANGO_DB_USER"),
    'PASSWORD': os.environ.get("DJANGO_DB_PASSWORD"),
}

SQLITE_DB_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

DATABASES= {
    "default": SQLITE_DB_CONFIG,
    "supabase": SUPABASE_DB_CONFIG,
    "sqlite": SQLITE_DB_CONFIG,
    "postgres": POSTGRES_DB_CONFIG
}

if SUPABASE_DB_URL:
    DATABASES['default'] = SUPABASE_DB_CONFIG


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# for django-debug-toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

TESTING = "test" in sys.argv

if not TESTING:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "debug_toolbar",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]

REST_FRAMEWORK = {
     "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ],
    # Add these renderer classes
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}
# for django-cors-headers
CORS_ALLOWED_ORIGINS = [
   *ALLOWED_HOSTS
]
CSRF_TRUSTED_ORIGINS = [
    *ALLOWED_HOSTS
]
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = (
    *default_headers,
    "my-custom-header",
)
CORS_ALLOW_CREDENTIALS = True

#jwt configuration
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
SIMPLE_JWT = {
    "SIGNING_KEY": JWT_SECRET_KEY,
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}
INTERNAL_IPS = ALLOWED_HOSTS
