from db.db_client import DBClient
from datetime import datetime

class OrderRepository:

    def __init__(self, db_client: DBClient):
        self.db = db_client

    def fetch_all_orders(self, user_id):
        query = f"""
                SELECT
                    o.order_id,
                    o.total_amount,
                    o.date_ordered,
                    o.status
                FROM orders o
                WHERE o.user_id = {user_id}
                """
        return self.db.select(query)

    def fetch_order(self, user_id, order_id):
        query = f"""
                SELECT
                    o.order_id,
                    o.total_amount,
                    o.date_ordered,
                    o.status
                FROM orders o
                WHERE o.user_id = {user_id} AND o.order_id = {order_id}
                """
        return self.db.select(query)

    def fetch_order_items(self, user_id, order_id):
        query = f"""
                SELECT
                    oi.item_id,
                    p.name,
                    oi.price,
                    oi.quantity,
                    oi.total_amount
                FROM orders o
                    INNER JOIN orderitems oi
                        ON o.order_id = oi.order_id
                    INNER JOIN products p
                        ON oi.product_id = p.product_id
                WHERE o.user_id = {user_id} AND o.order_id = {order_id}
                """
        return self.db.select(query)

    def add_order(self, user_id, total_amount):
        current_datetime = datetime.now()
        timestamp_without_tz = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        query = f"""
            INSERT INTO orders (
                user_id,
                total_amount,
                date_ordered,
                status
            ) VALUES (
                {user_id},
                {total_amount},
                '{timestamp_without_tz}',
                'pending'
            ) RETURNING order_id
        """
        return self.db.insert_rows(query)

    def add_order_item(self, order_id, product_id, price, quantity):
        total_amount = price * quantity;
        query = f"""
            INSERT INTO orderitems (
                order_id,
                product_id,
                price,
                quantity,
                total_amount
            ) VALUES (
                {order_id},
                {product_id},
                {price},
                {quantity},
                {total_amount}
            ) RETURNING item_id
        """
        return self.db.insert_rows(query)
