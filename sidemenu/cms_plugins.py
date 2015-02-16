from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from sidemenu.models import ProductMenu, Products
from django.contrib import admin


class ProductInlineAdmin(admin.StackedInline):
    model = Products


class ProductMenuPlugin(CMSPluginBase):
    model = ProductMenu
    render_template = "product_menu_plugin.html"
    inlines = (ProductInlineAdmin, )
plugin_pool.register_plugin(ProductMenuPlugin)
