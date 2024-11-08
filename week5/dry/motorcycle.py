from vehicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, brand, model, fuel_tank_capacity, fuel_consumption):
        super().__init__(brand, model, fuel_tank_capacity, fuel_consumption)

    def wheelie(self):
        return 'Performing a wheelie!'