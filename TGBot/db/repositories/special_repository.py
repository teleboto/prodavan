
from db.db_client import DBClient

class SpecialRepository:

  def __init__(self, db_client: DBClient):
    self.db = db_client

  def fetchActiveSpecial(self):
    return self.db.select(f"""
        SELECT "special_id", "name", "description" FROM "special"
        WHERE "special_id" IN (
            SELECT s."special_id" FROM "special" s LEFT JOIN "products" p ON s."special_id" = p."special_id"
            GROUP BY s."special_id"
            HAVING COUNT(p."product_id") > 0
        )
    """)

  def fetchSpecial(self, special_id):
    return self.db.select(f"""
        SELECT "special_id", "name", "description" FROM "special"
        WHERE "special_id"  = {special_id}
    """)
