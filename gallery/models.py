from cms.models import CMSPlugin
from django.db import models

# Create your models here.


class PhotoGallery(CMSPlugin):
    theme = models.CharField(max_length=50, blank=True)

    def copy_relations(self, oldinstance):
        for photo in oldinstance.photos.all():
            photo.pk = None
            photo.plugin = self
            photo.save()


class Photos(models.Model):
    plugin = models.ForeignKey(
        PhotoGallery,
        related_name="photos",
    )
    photo = models.ImageField()


class PhotoSwiper(CMSPlugin):
    title = models.CharField(max_length=50, blank=True)
    config = models.CharField(max_length=100, blank=True)

    def copy_relations(self, oldinstance):
        for photo in oldinstance.photos.all():
            photo.pk = None
            photo.plugin = self
            photo.save()


class SwiperPhoto(models.Model):
    plugin = models.ForeignKey(PhotoSwiper, related_name="photos")
    photo = models.ImageField()
