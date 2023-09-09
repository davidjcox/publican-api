"""Django settings for publican_api project"""

import publican_api as api

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


APP_LABEL = api.__api_app_label__
API_VERSION = api.__api_app_version__

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.publican.invocatum.net']

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ROOT_URLCONF = 'publican_api.urls'

WSGI_APPLICATION = 'publican_api.wsgi.application'

STATIC_ROOT = '/home/davidjcox/webapps/static_server_publican/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = 'https://publican.invocatum.net/static/'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'publican_api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


#rest framework settings
REST_FRAMEWORK = {
    'PAGINATE_BY': 10,                 # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Client override using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100,            # Maximum despite `?page_size=xxx`.
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
        'publican_api.throttles.BurstRateThrottle',
        'publican_api.throttles.SustainedRateThrottle',
        'publican_api.throttles.CustomListCreateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',          # Global
        'user': '1000/day',         # Global
        'burst': '60/min',          # BurstRateThrottle
        'sustained': '1000/day',    # SustainedRateThrottle
        'drinkcreate': '1/day',     # CustomListCreateThrottle
        'facilitycreate': '1/day',  # CustomListCreateThrottle
        'glasscreate': '1/hour',    # CustomListCreateThrottle
        'stylecreate': '1/day',     # CustomListCreateThrottle
        'reviewcreate': '1/week',   # CustomListCreateThrottle
    },
    'EXCEPTION_HANDLER': 'publican_api.views.custom_exception_handler',
}


# EOF - publican_api settings
