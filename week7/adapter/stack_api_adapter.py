# Adapter for WeatherStack API
from weather_data import WeatherData

class WeatherStackAdapter(WeatherData):
    def __init__(self, weatherstack_api):
        self.weatherstack_api = weatherstack_api

    def get_temperature(self):
        # Call WeatherStack API to fetch temperature data
        temperature = self.weatherstack_api.get_current()['temperature']
        return temperature

    def get_humidity(self):
        # Call WeatherStack API to fetch humidity data
        humidity = self.weatherstack_api.get_current()['humidity']
        return humidity

    def get_wind_speed(self):
        # Call WeatherStack API to fetch wind speed data
        wind_speed = self.weatherstack_api.get_current()['wind_speed']
        return wind_speed