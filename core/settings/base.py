
import os
from pathlib import Path
from datetime import timedelta

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv
from celery.schedules import crontab

from core.settings.jazzmin import JAZZMIN_SETTINGS


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

IS_PRODUCTION = os.getenv("PRODUCTION", "False").lower() == "true"


if IS_PRODUCTION:
    from core.settings.production import *
else:
    from core.settings.development import *


# =========================
# APPS
# =========================

THEME_APPS = [
    'jazzmin',
]

MY_APPS = [
    'apps.testapp',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LIBRARY_APPS = [
    'rest_framework',
    'drf_yasg',
    'django_ckeditor_5',
    'modeltranslation',
    'corsheaders',
]

INSTALLED_APPS = [
    *THEME_APPS,
    *DJANGO_APPS,
    *LIBRARY_APPS,
    *MY_APPS,
]


# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]


# =========================
# URL / WSGI
# =========================

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


# =========================
# TEMPLATES
# =========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =========================
# PASSWORD VALIDATION
# =========================

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


# =========================
# LANGUAGE / TIME
# =========================

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LANGUAGES = [
    ('ru', _('Russian')),
    ('ky', _('Kyrgyz')),
    ('en', _('English')),
]


# =========================
# MODELTRANSLATION
# =========================

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

MODELTRANSLATION_CUSTOM_FIELDS = ('CKEditor5Field',)


# =========================
# MEDIA
# =========================

MEDIA_URL = '/back_media/'

MEDIA_ROOT = BASE_DIR / 'back_media/'


# =========================
# STATIC
# =========================

STATIC_URL = '/back_static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'back_static')


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}


# =========================
# CKEDITOR
# =========================

CKEDITOR_5_CONFIGS = {
    'extends': {
        'blockToolbar': [
            'paragraph',
            'heading1',
            'heading2',
            'heading3',
            '|',
            'bulletedList',
            'numberedList',
            'alignment'
        ],

        'toolbar': [
            'heading',
            '|',
            'bold',
            'italic',
            'underline',
            'strikethrough',
            'code',
            '|',
            'fontSize',
            'fontColor',
            'fontBackgroundColor',
            '|',
            'link',
            'imageUpload',
            'mediaEmbed',
            'insertTable',
            'blockQuote',
            '|',
            'alignment',
            'outdent',
            'indent',
            '|',
            'sourceEditing',
            'removeFormat'
        ],

        'upload_url': '/ckeditor5/image_upload/',

        'heading': {
            'options': [
                {
                    'model': 'paragraph',
                    'title': 'Paragraph',
                    'class': 'ck-heading_paragraph'
                },
                {
                    'model': 'heading1',
                    'view': 'h1',
                    'title': 'Heading 1',
                    'class': 'ck-heading_heading1'
                },
                {
                    'model': 'heading2',
                    'view': 'h2',
                    'title': 'Heading 2',
                    'class': 'ck-heading_heading2'
                },
                {
                    'model': 'heading3',
                    'view': 'h3',
                    'title': 'Heading 3',
                    'class': 'ck-heading_heading3'
                }
            ]
        },

        'table': {
            'contentToolbar': [
                'tableColumn',
                'tableRow',
                'mergeTableCells',
                'tableProperties',
                'tableCellProperties'
            ]
        },

        'image': {
            'toolbar': [
                'imageTextAlternative',
                '|',
                'imageStyle:alignLeft',
                'imageStyle:alignCenter',
                'imageStyle:alignRight',
                '|',
                'imageStyle:full',
                'imageStyle:side'
            ]
        }
    },

    'minimal': {
        'toolbar': [
            'bold',
            'italic',
            'link'
        ],
    },
}


# =========================
# CUSTOM USER
# =========================

AUTH_USER_MODEL = "testapp.CustomUser"


# =========================
# DRF
# =========================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# =========================
# SIMPLE JWT
# =========================

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}


# =========================
# GOOGLE OAUTH
# =========================

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")


# =========================
# REDIS CACHE
# =========================

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv(
            "REDIS_URL",
            "redis://127.0.0.1:6379/1"
        ),
    }
}


# =========================
# CELERY
# =========================

CELERY_BROKER_URL = os.getenv(
    "REDIS_URL",
    "redis://127.0.0.1:6379/0"
)

CELERY_RESULT_BACKEND = os.getenv(
    "REDIS_URL",
    "redis://127.0.0.1:6379/0"
)

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'Asia/Bishkek'


# =========================
# CELERY BEAT
# =========================

CELERY_BEAT_SCHEDULE = {

    # Каждые 5 минут
    'run-stats-every-5-minutes': {
        'task': 'apps.testapp.tasks.monthly_user_stats_task',
        'schedule': 300.0,
    },

    # Каждый день в 00:00
    'run-daily-midnight-task': {
        'task': 'apps.testapp.tasks.monthly_user_stats_task',
        'schedule': crontab(
            hour=0,
            minute=0
        ),
    },
}

