from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin
from sidemenu.models import ProductDisplay, Products
# from django.contrib import admin


# class ProductInlineAdmin(admin.StackedInline):
#     model = Products


class ProductMenuPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "product_menu_plugin.html"
    # inlines = (ProductInlineAdmin, )

    def render(self, context, instance, placeholder):
        context["products"] = Products.objects.all()
        return context


class ProductDisplayPlugin(CMSPluginBase):
    model = ProductDisplay
    render_template = "product_display_plugin.html"

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        context["products"] = Products.objects.all()
        return context


plugin_pool.register_plugin(ProductMenuPlugin)
plugin_pool.register_plugin(ProductDisplayPlugin)
