
from .router import Router
from .handlers.list_goods_handler import list_goods_handler
from .handlers.list_categories_handler import list_categories_handler

router = Router()
router.add_route('list_goods', list_goods_handler)
router.add_route('catg', list_categories_handler)
