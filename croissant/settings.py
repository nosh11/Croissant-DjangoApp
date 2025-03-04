"""
Django settings for croissant project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q710#gs0q#n!$y7apgjgf1e%%c@z%lzsg&vuv#3sd&2d+gjx$v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_ENV") == "development"

ALLOWED_HOSTS = ["*"]



CSRF_TRUSTED_ORIGINS = ['https://localhost:8000', 'https://croissantmc-cmb5drgfcpffg6bm.japaneast-01.azurewebsites.net'] 

STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'novel.apps.NovelConfig',
    'portfolio.apps.PortfolioConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
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
    'allow_cidr.middleware.AllowCIDRMiddleware'
]

ROOT_URLCONF = 'croissant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'croissant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
if os.getenv("DJANGO_ENV") == "production":
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('PGDATABASE'), # DB名
            'USER': os.getenv('PGUSER'),
            'PASSWORD': os.getenv('PGPASSWORD'),
            'HOST': os.getenv('PGHOST'),
            'PORT': os.getenv('PGPORT'),
            'OPTIONS': {
                'ssl': {'ca': "/home/site/wwwroot/ssl/DigiCertGlobalCA.crt.pem"},
            }
        }
    }
    # Azure Blob Storage
    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
    AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
    AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
    AZURE_CONTAINER = "media"
    AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
    MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_CONTAINER}/'
    
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'


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

LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

# 読み込んだファイルをまとめて出力する先
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = (
    [
        BASE_DIR / 'static'
    ]
)



# セッションの設定
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # セッションの有効期限を1週間に設定
SESSION_COOKIE_HTTPONLY = True  # クッキーをJavaScriptからアクセスできないように設定
SESSION_COOKIE_SAMESITE = 'Strict'  # クロスサイトリクエストフォージェリ (CSRF) 保護のためにStrictに設定
SESSION_COOKIE_SECURE = True  # 開発環境ではFalse、本番環境ではTrueに設定
CSRF_COOKIE_SECURE = True    # 開発環境ではFalse、本番環境ではTrueに設定