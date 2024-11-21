# Adapter for OpenWeatherMap API
from weather_data import WeatherData

class OpenWeatherMapAdapter(WeatherData):
    def __init__(self, openweathermap_api):
        self.openweathermap_api = openweathermap_api

    def get_temperature(self):
        # Call OpenWeatherMap API to fetch temperature data
        temperature = self.openweathermap_api.get_temperature()
        return temperature['temp']

    def get_humidity(self):
        # Call OpenWeatherMap API to fetch humidity data
        humidity = self.openweathermap_api.get_humidity()
        return humidity['humidity']

    def get_wind_speed(self):
        # Call OpenWeatherMap API to fetch wind speed data
        wind_speed = self.openweathermap_api.get_wind_speed()
        return wind_speed['wind_speed']