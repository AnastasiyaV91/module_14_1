import sqlite3                     # Библиотека для работы с базами данных

# Установить на компьютер DB Browser for SQLite. С официального сайта https://sqlitebrowser.org/dl/.  64-разряда

# Создаем файл not_telegram.db

connection = sqlite3.connect("not_telegram.db")  # Подключение к базе данных not_telegram.db
                                                    # с помощью SQLite браузера sqlite3
cursor = connection.cursor()  # Курсор - какая ячейка отмечена

cursor.execute("""
CREATE TABLE IF NOT EXiSTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

# Заполняем таблицу Users десятью записями

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ? , ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

# Обновляем баланс у каждой второй записи, начиная с первой, на 500

for k in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{k}"))

# Удаляем каждую третью запись, начиная с первой

for k in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{k}",))

# Делаем выборку всех записей, где возраст не равен шестидесяти

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()  #  fetchall() Метод извлекает все (или все оставшиеся) строки из набора результатов запроса и
                   # возвращает список кортежей . Если больше нет доступных строк, он возвращает пустой список.

for user in users:
    username, email, age, balance = user
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")



connection.commit()  #  Сохраняем состояние
connection.close()   #  Закрываем подключение