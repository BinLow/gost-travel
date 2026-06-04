import sqlite3

# veritabanı oluştur (yoksa oluşturur)
conn = sqlite3.connect('hotels.db')
cursor = conn.cursor()

# tablo oluştur
cursor.execute('''
CREATE TABLE IF NOT EXISTS hotels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT,
    type TEXT,
    budget TEXT,
    price TEXT,
    image TEXT,
    desc TEXT,
    activities TEXT,
    rating TEXT
)
''')

conn.commit()
conn.close()

print("Veritabanı ve tablo oluşturuldu.")