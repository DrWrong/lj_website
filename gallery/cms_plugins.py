from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from gallery.models import PhotoGallery, Photos, PhotoSwiper, SwiperPhoto
from django.contrib import admin


class PhotoInlineAdmin(admin.StackedInline):
    model = Photos


class GalleryPlugin(CMSPluginBase):
    model = PhotoGallery
    render_template = "gallery_plugin.html"
    inlines = (PhotoInlineAdmin,)

plugin_pool.register_plugin(GalleryPlugin)


class SwiperPhotoInlineAdmin(admin.StackedInline):
    model = SwiperPhoto


class PhotoSwiperPlugin(CMSPluginBase):
    model = PhotoSwiper
    render_template = "photo_swiper.html"
    inlines = (SwiperPhotoInlineAdmin, )

plugin_pool.register_plugin(PhotoSwiperPlugin)
