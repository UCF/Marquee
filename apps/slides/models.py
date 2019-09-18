from django.db import models
from datetime import datetime
from txt2img import fonts_tuple
class Slide(models.Model):
	STATUS		 = (
		('Approved', 'Approved'),
		('Rejected', 'Rejected'),
		('Pending', 'Pending'),
	)
	FONTSIZES     = (
	    (16, '16 px'),
	    (18, '18 px')
	)
	created		  = models.DateTimeField(default=datetime.now())
	text		  = models.TextField("Enter Event Info (as it should appear on marquee):", default="Event")
	font		  = models.CharField(default='Gotham', max_length='255', choices=fonts_tuple())
	font_size     = models.IntegerField("Font Size", default=16, choices=FONTSIZES)
	color_bg	  = models.CharField("Background Color", max_length="6", default="000000")
	color_font	  = models.CharField("Font Color", max_length="6", default="EBB700")
	display_start = models.DateField()
	display_end	  = models.DateField()
	event_start	  = models.DateTimeField(null=True)
	event_end	  = models.DateTimeField(null=True)
	location	  = models.CharField("Event Location", max_length='255', blank=True)
	org			  = models.CharField("Name of UCF Organization / Unit", max_length=255)
	name		  = models.CharField("Contact Name", max_length=255)
	phone		  = models.CharField("Phone", max_length=50)
	email		  = models.EmailField()
	additional	  = models.TextField(blank=True)
	status		  = models.CharField(default='Pending', max_length='16', choices=STATUS)

	@property
	def admin_url(self):
		"""Returns admin url for this object"""
		from django.core.urlresolvers           import reverse
		from django.contrib.contenttypes.models import ContentType

		content_type = ContentType.objects.get_for_model(self.__class__)
		return reverse(
			"admin:%s_%s_change" % (
				content_type.app_label, content_type.model,
			), args=(self.id,))

	def __str__(self):
		return self.text

	def __repr__(self):
		return self.__str__()

	def __unicode__(self):
		return unicode(self.__str__())


# front-end form
from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField
class SlideForm(forms.ModelForm):
	display_start = forms.DateField(label="Display Start Date", input_formats=('%m/%d/%Y',))
	display_end = forms.DateField(label="Display End Date", input_formats=('%m/%d/%Y',))
	event_start = forms.DateField(label="Event Start Date/Time", input_formats=('%m/%d/%Y %H:%M %p',),)
	event_end = forms.DateField(label="Event End Date/Time", input_formats=('%m/%d/%Y %H:%M %p',),)
	phone = USPhoneNumberField()
	class Meta:
		model = Slide
		exclude = ('status','created', 'font', 'color_bg', 'color_font')
