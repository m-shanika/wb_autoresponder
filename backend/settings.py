import os
from pathlib import Path


MODE = os.environ.get("MODE", "LOCAL")
if MODE == "LOCAL":
    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv("env/.env.local"))
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = bool(int(os.environ.get("DEBUG", True)))
MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
MEDIA_URL = "/media/"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "autoresponder.apps.AutoresponderConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

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

WSGI_APPLICATION = "backend.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": os.environ.get("DATABASE", BASE_DIR / "db.sqlite3"),
#         "USER": os.environ.get("POSTGRES_USER", "user"),
#         "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
#         "HOST": os.environ.get("SQL_HOST", "localhost"),
#         "PORT": os.environ.get("SQL_PORT", "5432"),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
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

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# celery
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:6379/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:6379"
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "visibility_timeout": 18000,
    "max_retries": 2,
}
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps.clicker': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

OPENAPI_KEY = os.environ.get("OPENAPI_KEY", "")

BASE_DOMAIN = os.environ.get("BASE_DOMAIN", "http://localhost:8000")

