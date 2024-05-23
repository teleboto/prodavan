from db.db_client import DBClient

class OrderRepository:

    def __init__(self, db_client: DBClient):
        self.db = db_client

    def fetch_all_orders(self, user_id):
        query = """
                SELECT order_table.order_id, order_table.user_id, product_table.name, order_table.total_amount, order_table.date_ordered, order_table.status
                FROM orders AS order_table
                JOIN products AS product_table ON order_table.product_id = product_table.id
                WHERE order_table.user_id = %s
                """
        return self.db.select(query, (user_id,))