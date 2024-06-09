
from db.db_client import DBClient

class ProductRepository:

  def __init__(self, db_client: DBClient):
    self.db = db_client

  def fetchProductID(self, category_id):
    return self.db.select(f"""
      SELECT
        p."product_id" as product_id,
        p."name" as name,
        p."description" as description,
        p."price" as price,
        s."name" as special_name,
        s."description" as special_description,
        s."discount" as discount,
        c."name" as category_name
      FROM "products" p
        INNER JOIN "categories" c
          ON p."category_id" = c."category_id"
        LEFT JOIN "special" s
          ON p."special_id" = s."special_id"
      WHERE p."category_id" = {category_id}
    """)

  def fetchSpecialProducts(self, special_id):
    return self.db.select(f"""
      SELECT 
        p."product_id" as product_id,
        p."name" as name,
        p."description" as description,
        p."price" as price,
        s."name" as special_name,
        s."description" as special_description,
        s."discount" as discount
      FROM "products" p
        INNER JOIN "special" s
          ON p."special_id" = s."special_id"
      WHERE p."special_id" = {special_id}
    """)

  def fetchProduct(self, product_id):
    return self.db.select(f"""
      SELECT
        p."product_id" as product_id,
        p."name" as name,
        p."description" as description,
        p."price" as price,
        s."name" as special_name,
        s."description" as special_description,
        s."discount" as discount,
        c."name" as category_name
      FROM "products" p
        INNER JOIN "categories" c
          ON p."category_id" = c."category_id"
        LEFT JOIN "special" s
          ON p."special_id" = s."special_id"
      WHERE p."product_id" = {product_id}
    """)
