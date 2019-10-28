# admin interface
from models import *
from django import forms
from django.contrib import admin
from widgets import SlideSchemeWidget

class SlideAdminForm(forms.ModelForm):
	slide_scheme = forms.CharField(widget=SlideSchemeWidget(), required=False)
	class Meta:
		model = Slide


class SlideAdmin(admin.ModelAdmin):
	list_display = ('created', 'org', 'text', 'display_start', 'status',)
	search_fields = ['org', 'text']
	change_form_template = 'admin/slide.djt';
	form = SlideAdminForm
	fields = (
		'created',
		'text',
		'slide_scheme',
		'color_bg',
		'color_font',
		'font',
		'font_size',
		'display_start',
		'display_end',
		'org',
		'name',
		'phone',
		'email',
		'additional',
		'status')
	readonly_fields = ('created',)

	ordering = ['-created']

admin.site.register(Slide, SlideAdmin)
