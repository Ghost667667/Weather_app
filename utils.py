# utils.py
def format_weather(data: dict) -> str:
    """Format weather data into readable text."""
    if "error" in data:
        return data["error"]

    city = data["name"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"].capitalize()
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    return (
        f"Weather in {city}:\n"
        f"🌡 Temperature: {temp}°C\n"
        f"☁ Condition: {weather}\n"
        f"💧 Humidity: {humidity}%\n"
        f"🌬 Wind Speed: {wind} m/s"
    )
