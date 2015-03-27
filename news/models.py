from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse

# Create your models here.


class News(models.Model):

    """docstring for News"""
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True)
    abstract = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("newsdetail", kwargs={"pk": self.pk})
        # pass
