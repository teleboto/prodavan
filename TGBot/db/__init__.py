from config import config

from .db_client import DBClient
from .repositories.category_repository import CategoryRepository
from .repositories.product_repository import ProductRepository
from .repositories.user_repository import UserRepository
from .repositories.cart_repository import CartRepository
from .repositories.orders_repository import OrderRepository

db_client = DBClient(
  config["DB_HOST"],
  config["DB_PORT"],
  config["DB_NAME"],
  config["DB_USER"],
  config["DB_PASSWORD"]
)

categoryRepository = CategoryRepository(db_client)
productRepository = ProductRepository(db_client)
userRepository = UserRepository(db_client)
cartRepository = CartRepository(db_client)
orderRepository = OrderRepository(db_client)
