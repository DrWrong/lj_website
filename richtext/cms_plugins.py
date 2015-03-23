from cms.plugin_base import CMSPluginBase
from .models import RichText
from cms.plugin_pool import plugin_pool

class RichTextPlugin(CMSPluginBase):
    model = RichText
    render_template = "richtext_plugins.html"

plugin_pool.register_plugin(RichTextPlugin)
