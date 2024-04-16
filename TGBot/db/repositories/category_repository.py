
from db.db_client import DBClient

class CategoryRepository:

  def __init__(self, db_client: DBClient):
    self.db = db_client

  def fetchAll(self):
    return self.db.select("SELECT * FROM categories")
