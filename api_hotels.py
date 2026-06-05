import os
import math
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SEARCHAPI_KEY")


def calculate_distance(lat1, lon1, lat2, lon2):
    r = 6371

    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(r * c)


def rating_value(hotel):
    try:
        return float(hotel["rating"])
    except:
        return 0


def get_price(hotel):
    total_price = hotel.get("total_price")
    if isinstance(total_price, dict):
        price = total_price.get("price_before_taxes")
        if price:
            return price

    price_per_night = hotel.get("price_per_night")
    if isinstance(price_per_night, dict):
        price = price_per_night.get("price_before_taxes")
        if price:
            return price

    return None


def get_hotels(country, event_latitude=None, event_longitude=None):
    url = "https://www.searchapi.io/api/v1/search"

    params = {
        "engine": "google_hotels",
        "q": f"{country} hotels",
        "check_in_date": "2026-06-10",
        "check_out_date": "2026-06-12",
        "adults": "1",
        "currency": "TRY",
        "gl": "tr",
        "hl": "tr",
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    hotels = []

    for hotel in data.get("properties", []):

        price = get_price(hotel)
        rating = hotel.get("rating")
        
        reviews = hotel.get("reviews", 0)
        hotel_class = hotel.get("extracted_hotel_class", 0)

        images = hotel.get("images", [])
        image = ""

        if images:
         image = (
        images[0].get("original")
        or images[0].get("thumbnail")
        or ""
    )

        gps = hotel.get("gps_coordinates", {})
        hotel_latitude = gps.get("latitude")
        hotel_longitude = gps.get("longitude")

        if not image or not price or not rating:
         continue

        if reviews < 100:
             continue

        if hotel_class and hotel_class < 3:
         continue

        distance = None

        if event_latitude and event_longitude and hotel_latitude and hotel_longitude:
            distance = calculate_distance(
                event_latitude,
                event_longitude,
                hotel_latitude,
                hotel_longitude
            )

        hotels.append({
            "api_id": len(hotels),
            "name": hotel.get("name", "Otel"),
            "price": price,
            "rating": rating if rating else "Puan yok","reviews": reviews,
            "hotel_class": hotel.get("hotel_class", "Otel"),
            "reviews": reviews,
            "image": image,
            "link": hotel.get("link", "#"),
            "latitude": hotel_latitude,
            "longitude": hotel_longitude,
            "distance": distance,
            "country": country,
            "type": "Otel",
            "activities": ["Konaklama", "Şehir keşfi", "Ulaşım kolaylığı"]
        })

    if event_latitude and event_longitude:
        hotels.sort(
         key=lambda hotel: (
         hotel["distance"] if hotel["distance"] is not None else 999999,
         -rating_value(hotel),
         -hotel.get("reviews", 0)
    )
)
    else:
        hotels.sort(key=lambda hotel: (-rating_value(hotel), -hotel.get("reviews", 0)))

    hotels = hotels[:12]

    for index, hotel in enumerate(hotels):
        hotel["api_id"] = index

    return hotels
