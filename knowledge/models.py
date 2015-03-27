from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
# Create your models here.


class Knowledge(models.Model):
    title = models.CharField(max_length=60)
    content = RichTextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("knowledgedetail", kwargs={"pk": self.pk})
