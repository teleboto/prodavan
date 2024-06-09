
from .router import Router
from .handlers.list_goods_handler import list_goods_handler
from .handlers.list_categories_handler import list_categories_handler
from .handlers.product_details_handler import product_details_handler
from .handlers.add_to_cart_handler import add_to_cart_handler
from .handlers.show_cart_handler import show_cart_handler
from .handlers.clear_cart_handler import clear_cart_handler
from .handlers.list_orders_handler import list_orders_handler
from .handlers.place_order_handler import place_order_handler
from .handlers.order_details_handler import order_details_handler
from .handlers.list_special_handler import list_special_handler
from .handlers.list_special_goods_handler import list_special_goods_handler

router = Router()
router.add_route('list_goods', list_goods_handler)
router.add_route('catg', list_categories_handler)
router.add_route('prod_details', product_details_handler)
router.add_route('add_to_cart', add_to_cart_handler)
router.add_route('show_cart', show_cart_handler)
router.add_route('clear_cart', clear_cart_handler)
router.add_route('list_orders', list_orders_handler)
router.add_route('place_order', place_order_handler)
router.add_route('order_details', order_details_handler)
router.add_route('list_special', list_special_handler)
router.add_route('list_special_goods', list_special_goods_handler)
