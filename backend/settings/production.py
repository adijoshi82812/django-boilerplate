from .base import *

DEBUG = False

ALLOWED_HOSTS = ["ip-address", "website"]

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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postfresql_psycopg2",
        "NAME": "db-name",
        "USER": "db-user-name",
        "PASSWORD": "db-password",
        "HOST": "localhost",
        "PORT": "",
    }
}
