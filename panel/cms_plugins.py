from cms.plugin_base import CMSPluginBase
from .models import Panel
from cms.plugin_pool import plugin_pool


class PanelPlugin(CMSPluginBase):
    model = Panel
    render_template = "panel_plugins.html"

plugin_pool.register_plugin(PanelPlugin)
