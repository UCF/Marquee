# Marquee Slide Generator #

This tool provides an interface for submitting and managing marquee slides.  Users can submit slides to be displayed on the marquee via a publicly accessible form.  The slides can then be modified via an administrative interface that requires a login.

## Requirements ##

 * Python >= 2.6
 * Django >= 1.1
 * PIL (Python Imaging Library) >= 1.1.6

## Installation ##

Django applications can be installed on many different types of systems.  One of the most common is using the Apache HTTP Server and the wsgi module.  For more information on other installation types, please visit the django documentation covering installation, http://docs.djangoproject.com/en/1.2/howto/deployment/.

### Apache and WSGI ###

Ensure that the WSGI module (mod\_wsgi) is installed and functioning on your Apache install.  On some systems, this can be as trivial as uncommenting a line in httpd.conf, for example:

	#LoadModule wsgi_module modules/mod_wsgi.so

Changes to:

	LoadModule wsgi_module modules/mod_wsgi.so

However, you may need to install mod\_wsgi separately.  Please refer to the mod\_wsgi documentation for further assistance, http://code.google.com/p/modwsgi/wiki/InstallationInstructions.

With wsgi installed and running, you need to setup the virtual host configuration for the project.  The following example config should help:

	#Example *nix vhost config
	<VirtualHost *:80>
		ServerName marquee.app.url
		# (optional)
		ServerAlias another.marquee.app.url

		# Determined by the setting MEDIA_URL defined in settings_local.py
		# Second argument is the absolute path of the static folder in the app
		Alias /static/ /srv/www/submitty/static
		
		# Determined by the value ADMIN_MEDIA_PREFIX defined in
		# settings_local.py.  The second argument is the location of django's
		# admin media.  Here we have a symlink in the static folder pointing to
		# those files.
		Alias /media/ /srv/www/submitty/static/admin
		
		
		# This value points to the location the application will be served from.
		# The second argument is the wsgi file located in the apache folder for
		# the application.
		WSGIScriptAlias / /srv/www/submitty/apache/python.wsgi
		
		<Directory /srv/www/submitty/static/admin/>
			Options Indexes
			Order allow,deny
			Allow from all
		</Directory>
	</VirtualHost>

### Post install setup ###

Once apache is installed and configured properly, prepare the application itself.  Copy settings\_local.templ.py to settings\_local.py.  Make changes to that file as needed, most configuration settings are self explanatory.  Once the file is configured as needed, restart apache.  If all went well, your vhost should bring up the public form.

The settings.py file needs to be updated to include the Django admin templates using TEMPLATE_DIRS. Below is an example to include the admin templates after the custom templates.
TEMPLATE_DIRS = (
	TEMPL_FOLDER,
	'/usr/local/lib/python2.6/dist-packages/django/contrib/admin/templates'
	)


The only section which might need more explanation is the Active Directory section toward the end.  It is by default commented out, but when uncommented the settings there will be used to attempt to authenticate users against LDAP.