# Client code

from open_weather_app_api import OpenWeatherMapAPI
from weather_stack_api import WeatherStackAPI
from open_api_adapter import OpenWeatherMapAdapter
from stack_api_adapter import WeatherStackAdapter

def main():
    # Initialize API clients
    openweathermap_api = OpenWeatherMapAPI()
    weatherstack_api = WeatherStackAPI()

    # Create adapters for weather APIs
    openweathermap_adapter = OpenWeatherMapAdapter(openweathermap_api)
    weatherstack_adapter = WeatherStackAdapter(weatherstack_api)

    # Fetch and display weather data from OpenWeatherMap
    print("Weather Data from OpenWeatherMap:")
    print("Temperature:", openweathermap_adapter.get_temperature(), "°C")
    print("Humidity:", openweathermap_adapter.get_humidity(), "%")
    print("Wind Speed:", openweathermap_adapter.get_wind_speed(), "km/h\n")

    # Fetch and display weather data from WeatherStack
    print("Weather Data from WeatherStack:")
    print("Temperature:", weatherstack_adapter.get_temperature(), "°C")
    print("Humidity:", weatherstack_adapter.get_humidity(), "%")
    print("Wind Speed:", weatherstack_adapter.get_wind_speed(), "km/h")

if __name__ == "__main__":
    main()