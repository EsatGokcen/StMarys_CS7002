from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, brand, model, fuel_tank_capacity, fuel_consumption):
        super().__init__(brand, model, fuel_tank_capacity, fuel_consumption)

    def honk(self):
        return 'Beep, Beep!'