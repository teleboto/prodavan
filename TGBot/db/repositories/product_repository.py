
from db.db_client import DBClient

class ProductRepository:

  def __init__(self, db_client: DBClient):
    self.db = db_client

  def fetchProductID(self, category_id):
    return self.db.select(f"SELECT * FROM products WHERE category_id = {category_id}")

  def fetchProduct(self, product_id):
    return self.db.select(f"SELECT * FROM products WHERE product_id = {product_id}")
