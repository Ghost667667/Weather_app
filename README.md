# 🌦 Weather App

A simple modular Python application that fetches and displays real-time weather data using the [OpenWeatherMap API](https://openweathermap.org/api).  
Built with clean separation of concerns across multiple files for maintainability and scalability.

---

## 📂 Project Structure
Weather_app/
│── main.py              # Entry point
│── ui.py                # CLI interface
│── weather_service.py   # API requests
│── utils.py             # Formatting helpers
│── config_example.py    # Example config (replace with your own key)

---

## 🚀 Features
- Fetch current weather by city name
- Display temperature, condition, humidity, and wind speed
- Modular design (easy to extend with forecasts or GUI)
- Safe configuration

---

## 🔧 Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/your-username/weather-app.git
   cd weather-app/Weather_app

2.Install dependencies:
  
  `pip install requests`
  
3. Configure your API key:

 Copy config_example.py

Replace "your_api_key_here" with your real OpenWeatherMap API key
4. Run the app

  `python main.py`
  
Developed by Massa Coulibaly  
Student project
