from django.db import models
from ckeditor.fields import RichTextField
from cms.models import CMSPlugin


# Create your models here.
class Panel(CMSPlugin):
    title = models.CharField(max_length=50, blank=True)
    content = RichTextField(blank=True)
