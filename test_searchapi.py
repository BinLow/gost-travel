import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SEARCHAPI_KEY")

url = "https://www.searchapi.io/api/v1/search"

params = {
    "engine": "google_hotels",
    "q": "Istanbul hotels",
    "check_in_date": "2026-06-10",
    "check_out_date": "2026-06-12",
    "adults": "1",
    "currency": "TRY",
    "gl": "tr",
    "hl": "tr",
    "api_key": API_KEY
}

response = requests.get(url, params=params)

print("Status:", response.status_code)
print(response.text[:1000])