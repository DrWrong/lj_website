from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class KnowledgeApphook(CMSApp):
    name = "专业知识"
    urls = ["knowledge.urls"]

apphook_pool.register(KnowledgeApphook)
