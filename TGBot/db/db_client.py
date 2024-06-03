
import psycopg2
from psycopg2.extras import DictCursor

class DBClient:

  def __init__(
      self,
      DB_HOST,
      DB_PORT,
      DB_NAME,
      DB_USER,
      DB_PASSWORD
    ):
    self.HOST = DB_HOST
    self.PORT = DB_PORT
    self.NAME = DB_NAME
    self.USER = DB_USER
    self.PASS = DB_PASSWORD
    self.conn = None

  def connect(self):
    if self.conn is None:
      try:
        self.conn = psycopg2.connect(
          host = self.HOST,
          port = self.PORT,
          dbname = self.NAME,
          user = self.USER,
          password = self.PASS
        )
        print('Connected to database')
      except Error as e:
        print('Error connecting to database')
        print(e)

  def select(self, query):
    self.connect()
    with self.conn.cursor(cursor_factory=DictCursor) as cur:
      cur.execute(query)
      data = cur.fetchall()
    cur.close()
    return data

  def update_rows(self, query):
          """Run a SQL query to update rows in table."""
          self.connect()
          with self.conn.cursor() as cur:
              cur.execute(query)
              self.conn.commit()
              cur.close()
              return f"{cur.rowcount} rows affected."

  def insert_rows(self, query):
          """Run a SQL query to insert rows in table."""
          self.connect()
          with self.conn.cursor() as cur:
              cur.execute(query)
              new_id = cur.fetchone()[0]
              self.conn.commit()
              cur.close()
              return new_id
