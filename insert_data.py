import sqlite3

conn = sqlite3.connect('hotels.db')
cursor = conn.cursor()

hotels = [
    ("Barcelona Beach Hotel", "İspanya", "Etkinlik Odaklı", "Orta", "16000 TL", "hotel1.jpg",
     "Deniz kenarında eğlence dolu tatil.", "Plaj,Gece hayatı,Su sporları", "3.6",
     "Madrid Barajas Havalimanı", "30 dk", "Madrid Estación Sur Otogarı", "20 dk",
     "Havalimanından metro, otogardan ise şehir içi toplu taşıma ile ulaşım sağlanabilir.","41.3851", "2.1734"),

    ("Madrid Culture Stay", "İspanya", "Kültür Tanıma", "Orta", "14500 TL", "hotel2.jpg",
     "Şehir merkezinde kültürel deneyim.", "Müze,Şehir turu,Yerel yemekler", "4.3",
     "Madrid Barajas Havalimanı", "30 dk", "Madrid Estación Sur Otogarı", "20 dk",
     "Havalimanından metro, otogardan ise şehir içi toplu taşıma ile ulaşım sağlanabilir.","41.3851", "2.1734"),

    ("Roma History Hotel", "İtalya", "Tarihi Gezi", "Yüksek", "29000 TL", "hotel3.jpg",
     "Tarihi yapılara yakın konforlu otel.", "Tarih turu,Rehberli geziler", "4.7",
     "Roma Fiumicino Havalimanı", "35 dk", "Roma Tiburtina Otogarı", "20 dk",
     "Havalimanından tren veya taksi ile otele ulaşım sağlanabilir.","41.3851", "2.1734"),

    ("Kyoto Zen Stay", "Japonya", "Kafa Dinleme", "Yüksek", "32000 TL", "hotel1.jpg",
     "Sakin ve huzurlu Japon tarzı konaklama.", "Meditasyon,Doğa yürüyüşü", "4.4",
     "Kansai Uluslararası Havalimanı", "90 dk", "Kyoto Station", "15 dk",
     "Havalimanından tren ile Kyoto’ya, ardından kısa taksi yolculuğu ile otele ulaşılabilir.","41.3851", "2.1734"),

    ("Istanbul Culture Hotel", "Türkiye", "Kültür Tanıma", "Orta", "11000 TL", "hotel2.jpg",
     "Tarihi yarımadada konforlu konaklama.", "Tarihi geziler,Müze,Çarşı", "3.7",
     "İstanbul Havalimanı", "50 dk", "Esenler Otogarı", "30 dk",
     "Havalimanından Havaist, otogardan metro veya taksi ile ulaşım sağlanabilir.","41.3851", "2.1734"),

    ("bubu Bungalov", "Türkiye", "Kafa Dinleme", "Düşük", "6000 TL", "hotel1.jpg",
     "Deniz kenarında sakin ve huzurlu bir vakit.", "Plaj,Doğa,Sakinlik", "3.8",
     "Antalya Havalimanı", "45 dk", "Antalya Otogarı", "35 dk",
     "Havalimanından servis veya taksi ile bungalov bölgesine ulaşım sağlanabilir.","41.3851", "2.1734"),

    ("Gua Sha", "Japonya", "Kültür Tanıma", "Orta", "14000 TL", "hotel2.jpg",
     "Kapı Zil Ding Dong, masa tenis ping pong.", "Merkeze yakın,Kültürel,Şehir Turu", "3.1",
     "Tokyo Haneda Havalimanı", "35 dk", "Tokyo Station", "20 dk",
     "Havalimanından metro ve şehir içi trenlerle otele ulaşım sağlanabilir.","41.3851", "2.1734"),

    ("Corleone Hotel", "İtalya", "Etkinlik Odaklı", "Yüksek", "31000 TL", "hotel3.jpg",
     "İtalya'nın kırsal bölgelerine bir gezi.", "Tarih turu,Rehberli geziler", "4.7",
     "Palermo Havalimanı", "40 dk", "Palermo Otogarı", "25 dk",
     "Havalimanından araç kiralama veya taksi ile ulaşım önerilir.","41.3851", "2.1734")
]

cursor.executemany('''
INSERT INTO hotels (
    name, country, type, budget, price, image, desc, activities, rating,
    airport, airport_distance, bus_station, bus_distance, transport_info,latitude, longitude
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', hotels)

conn.commit()
conn.close()

print("Veriler eklendi.")