from django.http      import HttpResponse, HttpResponseNotFound
from django.core.mail import send_mail
import settings

def render_to_response(request, template, dictionary={}, mimetype=None):
	""" Wrapper for django.shortcuts.render_to_response to auto populate
	RequestContext as context_instance argument.""" 
	from django.shortcuts import render_to_response as _render_to_response
	from django.template  import RequestContext
	
	context_instance = RequestContext(request, dictionary)	
	return _render_to_response(template, context_instance, mimetype)

def home(request):
	from slides.models import Slide, SlideForm
   
	template = 'form.djt'
	if request.method == 'POST':
		form = SlideForm(request.POST)
		if form.is_valid():
			slide = form.save()
			send_mail(
				settings.EMAIL_SUBJECT % (slide.name,),
				settings.EMAIL_MESSAGE % (
					slide.text,
					slide.event_start,
					slide.event_end,
					slide.location,
					slide.name,
					slide.org,
					slide.phone,
					slide.email,
					slide.additional or "None",
					request.META['HTTP_HOST'] + slide.admin_url,
				),
				settings.EMAIL_FROM,
				settings.EMAIL_MARQUEE,
				fail_silently=True
			)
			save	 = bool(slide)
			template = 'submitted.djt'
	else:
		form = SlideForm()
	return render_to_response(request, template, locals())

def image(request):
	""" Generates an image based on the GET parameters passed.
	
	Available GET Params:
	
	Name       Example            Default          Description
	text       Some text          (empty)          Text to render
	fg         000                fff              Color of text
	bg         111                000              Color of background
	size       24                 16               Font size
	font       Arial.ttf          Gotham.ttf       Font face for rendered text
	padding    10                 5                Padding around text
	width      300                96               Width of rendered image
	height     300                128              Height of rendered image
	format     JPEG               PNG              Format of created image """
	
	import txt2img, StringIO
	text	   = request.GET.get('text', '')
	color	   = '#' + request.GET.get('fg', 'fff')
	size	   = int(request.GET.get('size', 16))
	font	   = request.GET.get('font', 'Gotham.ttf')
	format	   = request.GET.get('format', 'png').lower()
	download   = True if request.GET.get('download', False) else False
	mimetype   = {
		'png' : 'image/png',
		'jpeg': 'image/jpeg',
		'jpg' : 'image/jpeg',
	}.get(format, 'image/bmp')
	padding	   = int(request.GET.get('padding', 5))
	background = {
		'color' : '#' + request.GET.get('bg', '000'),
		'x'		: int(request.GET.get('width', 128)),
		'y'		: int(request.GET.get('height', 96)),
	}
	image = txt2img.text_to_image(
		text,
		background,
		color=color,
		font=font,
		size=size,
		padding=padding
	)
	output	 = StringIO.StringIO()
	image.save(output, format=format)
	response = HttpResponse(output.getvalue(), mimetype=mimetype)
	if download:
		response['content-disposition'] = "attachment; filename=marquee_slide." + format
	return response
	