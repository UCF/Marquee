from django.contrib.auth.models   import User, Permission
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
import ldap


def ldap_connect(username, password):
	l = ldap.initialize(settings.LDAP['URL'])
	b = ''.join([username, '@', settings.LDAP['DOMAIN']])
	l.simple_bind_s(b, password)
	return l

def valid_ldap_user(username, password):
	try:
		l = ldap_connect(username, password)
		return user_in_search_base(l, username)
	except ldap.INVALID_CREDENTIALS:
		return False

def user_in_search_base(l, username):
	r = l.search_s(
		settings.LDAP['SEARCH'],
		ldap.SCOPE_ONELEVEL,
		"SamAccountName=%s" % username
	)
	return bool(len(r))

def new_user(username):
	user = User(username=username)
	user.is_staff     = True
	user.is_superuser = False
	user.save()
	permissions = [
		Permission.objects.get(codename="add_slide"),
		Permission.objects.get(codename="change_slide"),
		Permission.objects.get(codename="delete_slide"),
	]
	user.user_permissions.add(*permissions)
	user.save()
	return user


class ActiveDirectoryBackend(ModelBackend):
	''' http://djangosnippets.org/snippets/501/ '''
	def authenticate(self, username=None, password=None):
		from django.contrib.auth.models import check_password
		
		if valid_ldap_user(username, password):
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				user = new_user(username)
			return user
		else:
			try:
				user = User.objects.get(username=username)
				if user.password and check_password(password, user.password):
					return user
			except User.DoesNotExist:
				return None
	
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
	
	def is_valid (self, username=None, password=None):
		## Disallowing null or blank string as password
		## as per comment: http://www.djangosnippets.org/snippets/501/#c868
		from django.contrib.auth.models import check_password
		
		if password == None or password == '':
			return False
		
		if valid_ldap_user(username, password):
			return True
		else:
			try:
				user = User.objects.get(username=username)
				return user.password and check_password(password, user.password)
			except User.DoesNotExist: pass
		
		return False