import sqlite3

database = sqlite3.connect("not_telegram.db")
cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)''')

#for i in range(1, 11):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"newuser{i}@gmail.com", int(f"{i}0"), 1000))

#cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = 1', (500,))

#cursor.execute('DELETE FROM Users WHERE (id - 1) % 3 = 0')

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

for user in users:
    print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")

database.commit()
database.close()