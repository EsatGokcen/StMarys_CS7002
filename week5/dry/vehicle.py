
class Vehicle:

    def __init__(self, brand, model, fuel_tank_capacity, fuel_consumption):
        self.__brand = brand
        self.__model = model
        self.__fuel_tank_capacity = fuel_tank_capacity
        self.__fuel_consumption = fuel_consumption

    def calculate_fuel_efficiency(self):
        return self.__fuel_tank_capacity / self.__fuel_consumption