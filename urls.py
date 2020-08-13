from django.conf.urls import *
from django.views.generic import TemplateView
import settings

from django.contrib import admin
admin.autodiscover()
from django.contrib.sites.models import Site
admin.site.unregister(Site)

urlpatterns = []

if settings.DEBUG or settings.SERVE_STATIC_FILES:
	urlpatterns = patterns('',
		(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
			'django.views.static.serve',
			{
				'document_root': settings.MEDIA_ROOT,
				'show_indexes' : True,
			}
		),
	)
	urlpatterns += patterns('',
			(r'^admin/admin/(?P<path>.*)$',
				'django.views.static.serve',
				{
					'document_root': 'static/admin',
					'show_indexes' : True,
				}
		),
	)

urlpatterns += patterns('',
	url(r'^$', 'slides.views.home', name="home"),
	url(r'^image/$', 'slides.views.image', name="image"),
	#(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	#(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

	(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

	(r'^admin/', include(admin.site.urls)),


)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
			'django.views.static.serve',
			{
				'document_root': settings.MEDIA_ROOT,
				'show_indexes' : True,
			}
		),
	)