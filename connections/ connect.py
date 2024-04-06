import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('Prodavan.sql')
cursor = connection.cursor()

# Выбираем всех пользователей
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

# Выводим результаты
for user in users:
  print(user)

# Закрываем соединение
connection.close()
