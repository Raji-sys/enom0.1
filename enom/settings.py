from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','@#$%nth_h&&d0merta8080mali-=4f5xdk*_xljm%+5svi*7-xqng$8rm4mgp0o&h+fdhp0w)pp9(^*=_=/,````~~~~;')


DEBUG=os.environ.get('DJANGO_DEBUG','') != 'False'

ALLOWED_HOSTS = ['*']

# SECURE_HSTS_SECONDS=31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS=True
# SECURE_SSL_REDIRECT=True
# SECURE_HSTS_PRELOAD=True
# SESSION_COOKIE_SECURE=True
# CSRF_COOKIE_SECURE=True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ems.apps.EmsConfig',
    'staff.apps.StaffConfig',
    'tailwind',
    'theme',
    'django_browser_reload',
    'django_filters',
    'django_fastdev',
    'widget_tweaks',
    'fontawesomefree',

]

TAILWIND_APP_NAME='theme'
INTERNAL_IPS=['127.0.0.1']
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

ROOT_URLCONF = 'enom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
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

WSGI_APPLICATION = 'enom.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',

#         'NAME': 'enom',

#         'USER': 'super_root',

#         'PASSWORD': '8080malintkheedomerta',

#         'HOST': 'localhost',

#         'PORT': '5432',
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = False

USE_L10N=False

USE_TZ = True

DATE_INPUT_FORMATS = ['%d-%m-%Y'] 
DATETIME_INPUT_FORMAT=['%d-%m-%Y']


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'