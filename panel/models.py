from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models import CMSPlugin


# Create your models here.
class Panel(CMSPlugin):
    title = models.CharField(max_length=50, blank=True)
    content = HTMLField(blank=True)
