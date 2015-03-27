from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
# Create your models here.


class Solution(models.Model):
    title = models.CharField(max_length=60)
    content = RichTextField()
    abstract = models.CharField(max_length=200)
    img = models.ImageField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        return reverse("solutiondetail", kwargs={"pk": self.pk})
