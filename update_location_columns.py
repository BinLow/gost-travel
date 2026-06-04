import sqlite3

conn = sqlite3.connect("hotels.db")
cursor = conn.cursor()

cursor.execute("ALTER TABLE hotels ADD COLUMN latitude TEXT")
cursor.execute("ALTER TABLE hotels ADD COLUMN longitude TEXT")

conn.commit()
conn.close()

print("Harita konum sütunları eklendi.")