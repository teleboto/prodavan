
from db.db_client import DBClient

class UserRepository:

  def __init__(self, db_client: DBClient):
    self.db = db_client

  def createUser(self, user_id, first_name, last_name):
    return self.db.update_rows(f"""INSERT INTO
                            users (
                              user_id,
                              first_name,
                              last_name,
                              email
                            ) VALUES (
                              {user_id},
                              '{first_name}',
                              '{last_name}',
                              ''
                            )""")

  def fetchUser(self, user_id):
    return self.db.select(f"SELECT * FROM users WHERE user_id = {user_id}")
