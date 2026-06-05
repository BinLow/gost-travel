from flask import Flask, render_template, request
import sqlite3
from api_hotels import get_hotels

app = Flask(__name__)

# API'den gelen otelleri geçici olarak burada tutuyoruz
event_location_cache = {
    "latitude": None,
    "longitude": None
}


def get_db_connection():
    conn = sqlite3.connect('hotels.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results')
def results():
    global api_hotels_cache, event_location_cache

    country = request.args.get('country')
    vacation_type = request.args.get('vacation_type')
    budget = request.args.get('budget')
    event_latitude = request.args.get('event_latitude')
    event_longitude = request.args.get('event_longitude')

    if not country or not vacation_type or not budget:
        return render_template(
            'results.html',
            hotels=[],
            country=country,
            vacation_type=vacation_type,
            budget=budget,
            event_latitude=event_latitude,
            event_longitude=event_longitude
        )

    hotels = get_hotels(country, event_latitude, event_longitude)
    api_hotels_cache = hotels
    event_location_cache["latitude"] = event_latitude
    event_location_cache["longitude"] = event_longitude

    return render_template(
        'results.html',
        hotels=hotels,
        country=country,
        vacation_type=vacation_type,
        budget=budget,
        event_latitude=event_latitude,
        event_longitude=event_longitude
    )


@app.route('/api-hotel/<int:hotel_index>')
def api_hotel_detail(hotel_index):
    global api_hotels_cache, event_location_cache

    if hotel_index < 0 or hotel_index >= len(api_hotels_cache):
        return "Otel bulunamadı", 404

    hotel = api_hotels_cache[hotel_index]

    return render_template(
        'hotel_detail.html',
        hotel=hotel,
        event_latitude=event_location_cache["latitude"],
        event_longitude=event_location_cache["longitude"]
    )


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True),