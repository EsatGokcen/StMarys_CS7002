from vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, brand, model, fuel_tank_capacity, fuel_consumption):
        super().__init__(brand, model, fuel_tank_capacity, fuel_consumption)

    def load_goods(self):
        return 'Loading goods'