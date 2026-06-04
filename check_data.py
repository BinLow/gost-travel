import sqlite3

conn = sqlite3.connect('hotels.db')
cursor = conn.cursor()

cursor.execute("SELECT id, name FROM hotels")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()