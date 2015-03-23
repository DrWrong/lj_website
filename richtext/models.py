from ckeditor.fields import RichTextField
# Create your models here.
from cms.models import CMSPlugin


class RichText(CMSPlugin):
    content = RichTextField(blank=True)
