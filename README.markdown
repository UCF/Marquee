# Marquee Slide Generator #

This tool provides an interface for submitting and managing marquee slides.  Users can submit slides to be displayed on the marquee via a publicly accessible form.  The slides can then be modified via an administrative interface that requires a login.

## Requirements ##

 * Python >= 2.7
 * Django >= 1.4
 * PIL (Python Imaging Library) >= 1.1.7 (*nix) or Pillow 2.0.0 (windows http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil)

## Installation ##

Django applications can be installed on many different types of systems.  One of the most common is using the Apache HTTP Server and the wsgi module.  For more information on other installation types, please visit the django documentation covering installation, http://docs.djangoproject.com/en/1.2/howto/deployment/.

If installing this project on a *nix system please ensure the imports are correct in the apps/slides/views.py file. Pillow and PIL libraries have different import locations.


### Post install setup ###

Once apache is installed and configured properly, prepare the application itself.  Copy settings\_local.templ.py to settings\_local.py.  Make changes to that file as needed, most configuration settings are self explanatory.  Once the file is configured as needed, restart apache.  If all went well, your vhost should bring up the public form.

The settings.py file needs to be updated to include the Django admin templates using TEMPLATE_DIRS. Below is an example to include the admin templates after the custom templates:

TEMPLATE_DIRS = (
	TEMPL_FOLDER,
	'/usr/local/lib/python2.6/dist-packages/django/contrib/admin/templates'
	)


The only section which might need more explanation is the Active Directory section toward the end.  It is by default commented out, but when uncommented the settings there will be used to attempt to authenticate users against LDAP.
