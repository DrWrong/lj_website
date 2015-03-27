from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class NewsApphook(CMSApp):
    name = "新闻"
    urls = ['news.urls']

apphook_pool.register(NewsApphook)
