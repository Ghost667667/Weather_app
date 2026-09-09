# ui.py
from weather_service import get_weather
from utils import format_weather

def run_ui():
    print("=== Weather Application ===")
    city = input("Enter city name: ")
    data = get_weather(city)
    print(format_weather(data))
