import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-q710#gs0q#n!$y7apgjgf1e%%c@z%lzsg&vuv#3sd&2d+gjx$v")
DEBUG = os.getenv("DJANGO_ENV") != "production"

if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']
else:
    ALLOWED_HOSTS = ["localhost", 
                     "www.croissantmc.net",
                     "croissantmc-cmb5drgfcpffg6bm.japaneast-01.azurewebsites.net"]
    CSRF_TRUSTED_ORIGINS = ['https://localhost:8000', 
                            'https://croissantmc-cmb5drgfcpffg6bm.japaneast-01.azurewebsites.net',
                            'https://www.croissantmc.net']

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
    'allow_cidr',
    'colorfield'
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
if not DEBUG:
    # Production environment
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
else:
    # Development environment
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# Media and static files (CSS, JavaScript, images)

account_name = os.getenv('AZURE_ACCOUNT_NAME')
account_key = os.getenv('AZURE_ACCOUNT_KEY')

if account_key and account_name:# and not DEBUG:
    # 本番環境の場合
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.azure_storage.AzureStorage",
            "OPTIONS": {
                "account_name": account_name,
                "account_key": account_key,
                "azure_container": "media",
            }
        },
        "staticfiles": {
            "BACKEND": "storages.backends.azure_storage.AzureStorage",
            "OPTIONS": {
                "account_name": account_name,
                "account_key": account_key,
                "azure_container": "static",
            }
        }
    }
    DEFAULT_FILE_STORAGE = "storages.backends.azure_storage.AzureStorage"
    STATICFILES_STORAGE = "storages.backends.azure_storage.AzureStorage"
    MEDIA_URL = f"https://{account_name}.blob.core.windows.net/media/"
    STATIC_URL = f"https://{account_name}.blob.core.windows.net/static/"
    MEDIA_ROOT = BASE_DIR / 'media'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]

else:
    # 開発環境の場合
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    MEDIA_ROOT = BASE_DIR / 'media'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

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

# セッションの設定
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # セッションの有効期限を1週間に設定
SESSION_COOKIE_HTTPONLY = True  # クッキーをJavaScriptからアクセスできないように設定
SESSION_COOKIE_SAMESITE = 'Strict'  # クロスサイトリクエストフォージェリ (CSRF) 保護のためにStrictに設定
SESSION_COOKIE_SECURE = not DEBUG  # Set to False in development, True in production
CSRF_COOKIE_SECURE = not DEBUG    # Set to False in development, True in production

LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'