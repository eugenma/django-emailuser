import os


SECRET_KEY = 'dummy'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'email_user',
]

MIDDLEWARE = [

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

DEBUG = True

BASE_DIR = os.path.dirname(__file__)

AUTH_USER_MODEL = 'email_user.EmailUser'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


DJANGO_EMAIL_USER = {
    'STORE_METHOD': 'lower',
}

USE_TZ = False  # just testing settings.
