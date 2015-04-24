from base import *
from os.path import abspath, basename, dirname, join, normpath
from sys import path

DEBUG = False
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'


ALLOWED_HOSTS = ['localhost','aw.eatsleepcode.in']
DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	    'NAME': 'analyst_db',                      # Or path to database file if using sqlite3.
	    # The following settings are not used with sqlite3:
	    'USER': 'analyst',
	    'PASSWORD': 'analyst',
	    'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
	    'PORT': '',                      # Set to empty string for default.
	}
}

AW_EMAIL_TO = ['mohammed.nawaz2@wipro.com', 'anirban.chakraborty1@wipro.com','reshma.rahi@wipro.com']