
import psycopg2

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
        print('Connected to databse')
      except Error as e:
        print('Error connecting to database')
        print(e)

  def select(self, query):
    self.connect()
    with self.conn.cursor() as cur:
      cur.execute(query)
      data = cur.fetchall()
    cur.close()
    return data

