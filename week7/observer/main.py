# Client code
from weather_station import WeatherStation
from concrete_observers import *

if __name__ == "__main__":
    weather_station = WeatherStation()

    # Attach observers
    user = User()
    weather_service = WeatherService()
    emergency_service = EmergencyService()
    weather_station.add_observer(user)
    weather_station.add_observer(weather_service)
    weather_station.add_observer(emergency_service)

    # Simulate weather conditions change
    weather_station.set_weather_conditions(25, 60, "Light Rain", 20)