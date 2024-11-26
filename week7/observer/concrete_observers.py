# Concrete Observers
from weather_observer import WeatherObserver

class User(WeatherObserver):
    def update(self, temperature, humidity, precipitation, wind_speed):
        print(f"User received weather update: Temperature is {temperature}°C, Humidity is {humidity}%")

class WeatherService(WeatherObserver):
    def update(self, temperature, humidity, precipitation, wind_speed):
        print(f"Weather Service received weather update: Temperature is {temperature}°C, Precipitation is {precipitation}")

class EmergencyService(WeatherObserver):
    def update(self, temperature, humidity, precipitation, wind_speed):
        print(f"Emergency Service received weather update: Temperature is {temperature}°C, Wind Speed is {wind_speed} km/h")