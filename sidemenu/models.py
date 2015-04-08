from django.db import models
from cms.models import CMSPlugin
# from copy import deepcopy
# from djangocms_text_ckeditor.fields import HTMLField
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
# Create your models here.


# class ProductMenu(CMSPlugin):

#     # def copy_relations(self, oldinstance):
#     #     for p in oldinstance.products.all():
#     #         new_p = deepcopy(p)
#     #         if p.publish_p is None:
#     #             new_p.pk = None
#     #             new_p.plugin = self
#     #             new_p.save()
#     #             p.publish_p = new_p
#     #             p.save()
#     #         else:
#     #             p.publish_p.plugin = self
#     #             p.publish_p.save()


class ProductDisplay(CMSPlugin):
    title = models.CharField(max_length=20)

    # def copy_relations(self, oldinstance):
    #     for p in oldinstance.products.all():
    #         new_p = deepcopy(p)
    #         if p.publish_p is None:
    #             new_p.pk = None
    #             new_p.productdisplay = self
    #             new_p.save()
    #             p.publish_p = new_p
    #             p.save()
    #         else:
    #             p.publish_p.productdisplay = self
    #             p.publish_p.save()


class Products(models.Model):
    # url = models.CharField(max_length=256)
    title = models.CharField(max_length=20)
    img = models.ImageField()
    slug = models.SlugField(unique=True)
    description = RichTextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-order"]

    @property
    def url(self):
        return reverse("productdetail", kwargs={"slug": self.slug})
