import os

PROJ_ROOT = os.path.abspath(os.path.dirname(__file__))
DEV_MODE = True     # Used to control local static content serving.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.sqlite3",
        'NAME': os.path.join(PROJ_ROOT, "models.sqlite"),
    }
}
TIME_ZONE = None
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '(okqqmuqmi_%10@ob3jn&@@s-qo(lnz9x0w=rc_9z)4jz0y+tl'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'main_urls'
TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'dates',
    'sports',
)

FIXTURE_DIRS = (
    os.path.join(PROJ_ROOT, "fixtures"),
)

