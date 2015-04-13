from cms.menu_bases import CMSAttachMenu
from sidemenu.models import Products
from menus.base import NavigationNode
from menus.menu_pool import menu_pool


class CategoryMenu(CMSAttachMenu):
    name = "Products menu"

    def get_nodes(self, request):
        nodes = []
        for product in Products.objects.all():
            node = NavigationNode(
                product.title,
                product.url,
                product.pk,
                None,
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(CategoryMenu)
