import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '4bum0=r2=*0vh75=sre-&0=&5=_ouwnfxn7c4ho_e2n-2li8yl'

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'tastypie',
    'sw_plannets'
]

MIDDLEWARE = [
]

ROOT_URLCONF = 'sw_plannets.urls'

TEMPLATES = [
]

WSGI_APPLICATION = 'sw_plannets.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': "sw_plannets",
    }
}


AUTH_PASSWORD_VALIDATORS = [
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
