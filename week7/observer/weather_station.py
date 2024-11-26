# Subject: WeatherStation

class WeatherStation:
    
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.precipitation = ""
        self.wind_speed = 0

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.precipitation, self.wind_speed)

    def set_weather_conditions(self, temperature, humidity, precipitation, wind_speed):
        self.temperature = temperature
        self.humidity = humidity
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.notify_observers()