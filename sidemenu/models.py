from django.db import models
from cms.models import CMSPlugin

# Create your models here.


class ProductMenu(CMSPlugin):

    def copy_relations(self, oldinstance):
        for p in oldinstance.products.all():
            p.pk = None
            p.plugin = self
            p.save()


class Products(models.Model):
    plugin = models.ForeignKey(ProductMenu, related_name="products")
    url = models.CharField(max_length=256)
    title = models.CharField(max_length=20)
