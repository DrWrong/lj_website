from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class SolutionApphook(CMSApp):
    name = "解决方案"
    urls = ["solutions.urls"]


apphook_pool.register(SolutionApphook)
