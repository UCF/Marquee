DEBUG          = True
TEMPLATE_DEBUG = DEBUG
ADMINS         = (
	#('Your Name', 'your_email@domain.com'),
)
MANAGERS       = ADMINS

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'thisisasecretsecretsecretsecretkey'

EMAIL_HOST          = 'localhost'
EMAIL_PORT          = 1025
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS       = False

if DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#Configurables for slide submission email notification
EMAIL_FROM          = 'noreply@mail.ucf.edu'
EMAIL_MARQUEE       = ['marquee@mail.ucf.edu',]
EMAIL_SUBJECT       = "A New Marquee Request has been submitted by %s"
EMAIL_MESSAGE       = """The following slide was recently submitted:

--Event Information--
Text / Name  : %s

--Contact Information--
Contact Name : %s
Organization : %s
Phone        : %s
Email        : %s
Additional   : %s


You may preview or edit the submission by visiting http://%s
"""

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'marquee.sqlite3.db',                      # Or path to database file if using sqlite3.
		'USER': '',                      # Not used with sqlite3.
		'PASSWORD': '',                  # Not used with sqlite3.
		'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	}
}

DATABASE_ENGINE   = 'sqlite3'
DATABASE_NAME     = 'data/marquee.sqlite3.db'
DATABASE_HOST     = ''
DATABASE_PORT	  = ''
DATABASE_USER     = ''
DATABASE_PASSWORD = ''

### ACTIVE DIRECTORY SETTINGS
# AD_DNS_NAME should set to the AD DNS name of the domain (ie; example.com)
# If you are not using the AD server as your DNS, it can also be set to
# FQDN or IP of the AD server.
'''
AUTHENTICATION_BACKENDS = ('auth.ActiveDirectoryBackend',)
LDAP = {
	'SERVER' : 'www.ldap.url.com',
	'PORT'   : 389,
	'DOMAIN' : 'CRAZYDOMAIN',
	'SEARCH' : 'DC=ldap,DC=url,DC=com',
}
LDAP['URL'] = 'ldap://%s:%s' % (LDAP['SERVER'], LDAP['PORT'])
'''
