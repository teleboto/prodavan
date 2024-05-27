from db.db_client import DBClient
from datetime import datetime

class CartRepository:

  def __init__(self, db_client: DBClient):
    self.db = db_client

  def add_to_cart(self, user_id, product_id):
    current_datetime = datetime.now()
    timestamp_without_tz = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    existing_line = self.db.select(f"""
                                     SELECT * FROM cart 
                                     WHERE user_id = {user_id} 
                                     AND product_id = '{product_id}'
                                     """)
    if existing_line:
      new_quantity = int(existing_line[0][3]) + 1
      return self.db.update_rows(f"""
                                 UPDATE cart
                                 SET quantity = {new_quantity}
                                 WHERE user_id = {user_id}
                                 AND product_id = '{product_id}'
                                 """)
    else:
      return self.db.update_rows(f"""
                                 INSERT INTO cart (
                                 user_id,
                                 product_id,
                                 quantity,
                                 date_added
                              ) VALUES (
                                 {user_id},
                                '{product_id}',
                                '1',
                                '{timestamp_without_tz}'
                                 )""")
    
  def get_cart_products(self, user_id):
    query = f"""
      SELECT 
        c.cart_id,
        p.product_id,
        p.name,
        p.price,
        c.quantity
      FROM cart c
        INNER JOIN products p
          ON c.product_id = p.product_id
      WHERE 
        c.user_id = {user_id}
    """
    return self.db.select(query)

  def clear(self, user_id):
    query = f"""
      DELETE 
      FROM cart
      WHERE 
        user_id = {user_id}
    """
    return self.db.update_rows(query)
