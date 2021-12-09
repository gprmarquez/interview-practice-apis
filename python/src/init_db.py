import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO activities (name, duration, date, distance) VALUES (?, ?, ?, ?)",
            ('First Activity', 20, '2021-12-08', 40)
            )

cur.execute("INSERT INTO activities (name, duration, date, distance) VALUES (?, ?, ?, ?)",
            ('Second Activity', 10, '2021-12-09', 30)
            )

connection.commit()
connection.close()