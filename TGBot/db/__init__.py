from config import config

from .db_client import DBClient
from .repositories.category_repository import CategoryRepository

db_client = DBClient(
  config["DB_HOST"],
  config["DB_PORT"],
  config["DB_NAME"],
  config["DB_USER"],
  config["DB_PASSWORD"]
)

categoryRepository = CategoryRepository(db_client)
