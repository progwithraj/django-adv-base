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
from datetime import timedelta
from pathlib import Path

import dj_database_url
from corsheaders.defaults import default_headers
from dotenv import load_dotenv

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
DJANGO_ENV = os.environ.get("DJANGO_ENV")

ALLOWED_HOSTS = [
    ".railway.app",
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
]  # https://saas.prod.railway.app
if DJANGO_ENV == "DEV":
    ALLOWED_HOSTS += convert_string_to_list(os.environ.get("DJANGO_ALLOWED_HOSTS_LIST"))

# Application definition
BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# custom admin app
BASE_APPS.insert(0, "jazzmin")

THIRD_PARTY_APPS = [
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    # 'rest_framework_simplejwt.token_blacklist',
    "corsheaders",
    "allauth_ui",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "widget_tweaks",
    "django_filters",
    "anymail",
    "drf_yasg",
    "django_countries",
    "django_prose_editor",
]

LOCAL_APPS = [
    "api.apps.ApiConfig",
    "customUser.apps.CustomuserConfig",
    "userProfile.apps.UserprofileConfig",
    "post.apps.PostConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
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

ROOT_URLCONF = "coreApp.urls"

# custom user model
AUTH_USER_MODEL = "customUser.CustomUser"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "coreApp.wsgi.application"

# ALLOW AUTO APPEND SLASH
APPEND_SLASH = True

# Django Allauth Config
LOGIN_REDIRECT_URL = "/"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[CFE] "
ACCOUNT_EMAIL_REQUIRED = True

AUTHENTICATION_BACKENDS = [
    # ...
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
    # ...
]

SOCIALACCOUNT_PROVIDERS = {"github": {"VERIFIED_EMAIL": True}}

# supabase
SUPABASE_PROJECT_PASSWORD = os.environ.get("SUPABASE_PROJECT_PASSWORD")
SUPABASE_DB_URL = os.environ.get("SUPABASE_PROJECT_URI").format(
    SUPABASE_PROJECT_PASSWORD=SUPABASE_PROJECT_PASSWORD
)

# neonsql
NEON_SQL_PROJECT_USER = os.environ.get("NEON_SQL_PROJECT_USER")
NEON_SQL_PROJECT_DB = os.environ.get("NEON_SQL_PROJECT_DB")
NEON_DB_PROJECT_USER_PASSWORD = os.environ.get("NEON_DB_PROJECT_USER_PASSWORD")
NEON_DB_URL = os.environ.get("NEON_SQL_PROJECT_URI").format(
    NEON_SQL_PROJECT_USER=NEON_SQL_PROJECT_USER,
    NEON_DB_PROJECT_USER_PASSWORD=NEON_DB_PROJECT_USER_PASSWORD,
    NEON_SQL_PROJECT_DB=NEON_SQL_PROJECT_DB,
)

# Database
SUPABASE_DB_CONFIG = dj_database_url.config(
    default=SUPABASE_DB_URL, conn_max_age=600, conn_health_checks=True
)

NEON_DB_CONFIG = dj_database_url.config(
    default=NEON_DB_URL, conn_max_age=600, conn_health_checks=True
)

POSTGRES_DB_CONFIG = {
    "ENGINE": os.environ.get("DJANGO_DB_ENGINE"),
    "NAME": os.environ.get("DJANGO_DB_NAME"),
    "USER": os.environ.get("DJANGO_DB_USER"),
    "PASSWORD": os.environ.get("DJANGO_DB_PASSWORD"),
}

SQLITE_DB_CONFIG = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
}

DATABASES = {
    "default": SQLITE_DB_CONFIG,
    "supabase": SUPABASE_DB_CONFIG,
    "sqlite": SQLITE_DB_CONFIG,
    "postgres": POSTGRES_DB_CONFIG,
}

if SUPABASE_DB_CONFIG and NEON_DB_CONFIG:
    if DJANGO_ENV == "DEV":
        DATABASES["default"] = SUPABASE_DB_CONFIG
    else:
        DATABASES["default"] = NEON_DB_CONFIG

# print(
#     Fore.GREEN
#     + f"currently using {DATABASES['default']['ENGINE']} on {DATABASES["default"]["HOST"]}"
# )


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# whitenoise config
STATIC_URL = "static/"
STATICFILES_BASE_DIR = BASE_DIR / "staticfiles"
STATICFILES_BASE_DIR.mkdir(exist_ok=True, parents=True)
STATICFILES_VENDOR_DIR = STATICFILES_BASE_DIR / "vendors"

# source(s) for python manage.py collectstatic
STATICFILES_DIRS = [STATICFILES_BASE_DIR]

# output for python manage.py collectstatic
# local cdn
STATIC_ROOT = BASE_DIR / "local-cdn"

# media files
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# < Django 4.2
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT", default="587")  # 587
EMAIL_USE_TLS = os.environ.get(
    "EMAIL_USE_TLS", default=True
)  # Use EMAIL_PORT 587 for TLS
EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL", default=False)
ADMIN_USER_NAME = os.environ.get("ADMIN_USER_NAME", default="Admin user")
ADMIN_USER_EMAIL = os.environ.get("ADMIN_USER_EMAIL", default=None)

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
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    # Add these renderer classes
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}

CORS_HOSTS_LIST = convert_string_to_list(os.environ.get("CORS_HOSTS_LIST"))
# for django-cors-headers
CORS_ALLOWED_ORIGINS = [*CORS_HOSTS_LIST]
CSRF_TRUSTED_ORIGINS = [*CORS_HOSTS_LIST]
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

# jwt configuration
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
SIMPLE_JWT = {
    "SIGNING_KEY": JWT_SECRET_KEY,
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "BLACKLIST_AFTER_ROTATION": True,
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=7),
}
INTERNAL_IPS = ALLOWED_HOSTS


# Custom Admin Settings
JAZZMIN_SETTINGS = {
    "site_title": "Priyanath",
    "site_header": "Priyanath",
    "site_brand": "Modern Marketplace ",
    # "site_icon": "images/favicon.ico",
    # "site_logo": "images/logos/logo.jpg",
    "welcome_sign": "Welcome To Priyanath",
    "copyright": "Priyanath",
    "user_avatar": "images/photos/logo.jpg",
    # "topmenu_links": [
    #     {"name": "Dashboard", "url": "home", "permissions": ["auth.view_user"]},
    #     {"model": "auth.User"},
    # ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": [
        "api",
        "api.Post",
        "api.Category",
        "api.Comment",
        "api.Bookmark",
        "api.Notification",
    ],
    "icons": {
        "admin.LogEntry": "fas fa-file",
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "api.User": "fas fa-user",
        "api.Profile": "fas fa-address-card",
        "api.Post": "fas fa-th",
        "api.Category": "fas fa-tag",
        "api.Comment": "fas fa-envelope",
        "api.Notification": "fas fa-bell",
        "api.Bookmark": "fas fa-heart",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    "related_modal_active": False,
    "custom_js": None,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

# Jazzmin Tweaks
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-indigo",
    "accent": "accent-olive",
    "navbar": "navbar-indigo navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-indigo",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}

# rich text editor
