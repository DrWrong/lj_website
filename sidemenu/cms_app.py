from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from sidemenu.menus import CategoryMenu


class ProductApphook(CMSApp):
    name = "产品"
    urls = ['sidemenu.urls']
    menus = [CategoryMenu]
apphook_pool.register(ProductApphook)
