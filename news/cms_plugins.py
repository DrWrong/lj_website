from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin
from news.models import News


class NewsIndexPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "news_plugin.html"

    def render(self, context, instance, placeholder):
        context["news"] = News.objects.all()[0:10]
        return context

plugin_pool.register_plugin(NewsIndexPlugin)
