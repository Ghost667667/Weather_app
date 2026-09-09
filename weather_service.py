# weather_service.py
import requests
from config import API_KEY, BASE_URL

def get_weather(city: str) -> dict:
    """Fetch weather data from OpenWeatherMap API."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"City '{city}' not found or API error."}
