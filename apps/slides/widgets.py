from django.contrib.admin.widgets import AdminTextInputWidget
from django.template.loader import render_to_string

class SlideSchemeWidget(AdminTextInputWidget):
  """ 
  Choose a slide color scheme
  """
  def render(self, name, value, attrs=None):
    return render_to_string("admin/slide_scheme_widget.djt", locals())
