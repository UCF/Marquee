import os, sys
FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
ROBOT    = {
	'SUBMISSIONS_DIR' : 'img/submissions/',
	'BACKGROUND_DIR'  : 'img/bg/',
}

def fonts_tuple():
	"""Choices iterable for fonts in Django"""
	fonts = available_fonts()
	fonts.sort()
	for f in fonts:
		yield (f, f.replace('_', ' '))

def available_fonts():
	"""Generator function which describes a list of tuples representing fonts
	usable by txt2img."""
	files = os.listdir(FONT_DIR)
	files = filter(lambda f: f[-3:] == 'ttf', files)
	files = map(lambda f: f.split('.')[0], files)
	return files

def text_to_image(
		text, background, 
		padding=0, line_height=0, size=16, color="#fff", font="Gotham.ttf"
	):
	"""Given a string and a background image, will write that text to
	the image, centered vertically and horizontally.  Returns the image.
	
	Background can either be a path to an image or a dictionary describing the
	dimensions and color of a background."""
	
	from PIL import Image, ImageFont
	font = os.path.join(FONT_DIR, font)
	try:
		font = ImageFont.truetype(font, size)
	except IOError:
		font = ImageFont.truetype(font + '.ttf', size)
	image = {
		str  : lambda: Image.open(background),
		dict : lambda: Image.new(
			'RGBA',
			(background['x'], background['y']),
			background['color']
		)
	}[type(background)]()
	font.color        = color
	image.padding     = padding
	image.line_height = line_height
	image.font        = font
	lines             = list()

	for line in text.splitlines():
		lines.extend(wordwrap(line, image))
	
	image = writelines(lines, image)
	
	return image

def wordwrap(line, image):
	""" Wraps lines by segmenting them into seperate elements of a list.  Each
	item in returned list represents a line that would fit in the given image.
	Attempts to fit text on least amount of lines possible. """
	font             = image.font
	img_w, img_h     = image.size
	img_w            = img_w - image.padding * 2
	space_left       = img_w
	space_size, null = font.getsize(' ')
	words            = line.split(' ')
	lines            = list()
	line             = list()
	for word in words:
		word_size, null = font.getsize(word)
		if ((word_size + space_size) > space_left) and space_left != img_w:
			lines.append(' '.join(line))
			line       = [word,]
			space_left = img_w - word_size
		else:
			space_left = space_left - (word_size + space_size)
			line.append(word)
	lines.append(' '.join(line))
	return lines

def writelines(lines, image):
	"""Writes lines to image provided with the specified font and color.
	Currently automatically centers both horizontally and vertically.  At the
	moment there is no way to customize this."""
	from PIL import ImageDraw
	if len(lines) < 1: return image

	font         = image.font
	img_w, img_h = image.size
	start_y      = int(
		(img_h - (len(lines) * font.getsize(lines[0])[1]))/2
	) - 2 #small alteration for perception
	for line in lines:
		line_w, line_h = font.getsize(line)
		start_x = int((img_w - line_w)/2)
		dmgr    = ImageDraw.Draw(image)
		dmgr.text((start_x, start_y), line, font=font, fill=font.color)
		start_y = start_y + line_h + image.line_height
	
	return image


if __name__ == '__main__':
	for f in fonts_tuple():
		print f
