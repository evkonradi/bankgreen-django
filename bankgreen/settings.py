"""
Django settings for bankgreen project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

import django
from django.utils.encoding import force_str

from dotenv import load_dotenv


# this hack is necessary because force_text is removed from django4, but graphene < 3 requires it
django.utils.encoding.force_text = force_str

"""
The .env file should be on the same dir as this file, that is loaded through load_dotenv().
.env file is not tracked by git so in owr dev environment it will be different from prod.
Ex: in dev ALLOWED_HOSTS = [], but in prod server ALLOWED_HOSTS = [domain, IP]
"""
ENV_DIR = str(Path().cwd() / "bankgreen/.env")
load_dotenv(ENV_DIR)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "True"

ALLOWED_HOSTS = (
    os.environ.get("ALLOWED_HOSTS").split(" ") if os.environ.get("ALLOWED_HOSTS") else []
)

# Calendar URL
SEMI_PUBLIC_CALENDAR_URL = os.environ.get("CALENDAR_URL")

INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # my apps
    "datasource",
    "brand",
    # third party apps
    "graphene_django",
    "django_countries",
    "django_admin_listfilter_dropdown",
    "django_filters",
    "django_json_widget",
    "corsheaders",
    "cities_light",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bankgreen.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "bankgreen.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = ("static/admin", os.path.join(BASE_DIR, "brand/static/"))


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# This is used to delete this many objects at once
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000


USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
PASSWORD = os.environ.get("PASSWORD")

CORS_ALLOWED_ORIGIN_REGEXES = (
    os.environ.get("CORS_ALLOWED_ORIGIN_REGEXES").split(" ")
    if os.environ.get("CORS_ALLOWED_ORIGIN_REGEXES")
    else []
)

CACHE_MAX_AGE = os.environ.get("CACHE_MAX_AGE")

# lets us pull all banks at once without pagination
GRAPHENE = {"RELAY_CONNECTION_MAX_LIMIT": 10000}

CITIES_LIGHT_TRANSLATION_LANGUAGES = [""]
CITIES_LIGHT_INCLUDE_CITY_TYPES = [""]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 1,
}
