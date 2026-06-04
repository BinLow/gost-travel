import sqlite3

conn = sqlite3.connect('hotels.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM hotels")

conn.commit()
conn.close()

print("Tüm otel kayıtları silindi.")