# Django settings for generic project.
import os
import sys

PROJECT_FOLDER    = os.path.dirname(os.path.abspath(__file__))
APP_FOLDER        = os.path.join(PROJECT_FOLDER, 'apps')
INC_FOLDER        = os.path.join(PROJECT_FOLDER, 'third-party')
TEMPL_FOLDER      = os.path.join(PROJECT_FOLDER, 'templates')
ROOT_URLCONF      = os.path.basename(PROJECT_FOLDER) + '.urls'
MEDIA_ROOT        = os.path.join(PROJECT_FOLDER, 'static')

TIME_ZONE         = 'America/New_York'
LANGUAGE_CODE     = 'en-us'
SITE_ID           = 1
USE_I18N          = False

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_DIRS = (TEMPL_FOLDER,)

# Add local apps folder to python path
sys.path.append(APP_FOLDER)
sys.path.append(INC_FOLDER)
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'slides',
)

try:
	from settings_local import *
except ImportError:
	from django.core.exceptions import ImproperlyConfigured
	raise ImproperlyConfigured(
		'Local settings file was not found. ' +
		'Ensure settings_local.py exists in project root.'
	)
	