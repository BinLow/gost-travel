import sqlite3

conn = sqlite3.connect("hotels.db")
cursor = conn.cursor()

# Yeni sütunlar ekleniyor
cursor.execute("ALTER TABLE hotels ADD COLUMN airport TEXT")
cursor.execute("ALTER TABLE hotels ADD COLUMN airport_distance TEXT")

cursor.execute("ALTER TABLE hotels ADD COLUMN bus_station TEXT")
cursor.execute("ALTER TABLE hotels ADD COLUMN bus_distance TEXT")

cursor.execute("ALTER TABLE hotels ADD COLUMN transport_info TEXT")

conn.commit()
conn.close()

print("Ulaşım sütunları eklendi.")