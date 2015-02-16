from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from gallery.models import PhotoGallery, Photos
from django.contrib import admin


class PhotoInlineAdmin(admin.StackedInline):
    model = Photos


class GalleryPlugin(CMSPluginBase):
    model = PhotoGallery
    render_template = "gallery_plugin.html"
    inlines = (PhotoInlineAdmin,)

plugin_pool.register_plugin(GalleryPlugin)
