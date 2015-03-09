from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ProductApphook(CMSApp):
    name = "产品"
    urls = ['sidemenu.urls']

apphook_pool.register(ProductApphook)
