from config import config

from .db_client import DBClient
from .repositories.category_repository import CategoryRepository
from .repositories.product_repository import ProductRepository
from .repositories.user_repository import UserRepository
from .repositories.cart_repository import CartRepository
from .repositories.orders import OrderRepository  


db_client = DBClient(
    host=config["DB_HOST"],
    port=config["DB_PORT"],
    database=config["DB_NAME"],
    user=config["DB_USER"],
    password=config["DB_PASSWORD"]
)
categoryRepository = CategoryRepository(db_client)
productRepository = ProductRepository(db_client)
userRepository = UserRepository(db_client)
cartRepository = CartRepository(db_client)