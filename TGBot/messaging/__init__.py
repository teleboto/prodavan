
from .router import Router
from .handlers.list_goods_handler import list_goods_handler
from .handlers.list_categories_handler import list_categories_handler
from .handlers.product_details_handler import product_details_handler
from .handlers.add_to_cart_handler import add_to_cart_handler

router = Router()
router.add_route('list_goods', list_goods_handler)
router.add_route('catg', list_categories_handler)
router.add_route('prod_details', product_details_handler)
router.add_route('add_to_cart', add_to_cart_handler)
