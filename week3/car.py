
class Car():

    def __init__(self, colour, model, year, fuel_level=100, engine_on=False):
        self.__colour = colour
        self.__model = model
        self.__year = year
        self.__fuel_level = fuel_level
        self.__engine_on = engine_on

    def start_engine(self):
        ''' 
        if self.engine_on:
            print('engine is on')

        else:
            if self.fuel_level > 0:
                print('The car engine started')
            else:
                print('no fuel')
        ''' #Shadi's code above

        if self.__engine_on == True:
            print("The engine is already on.")
        else:
            if self.__fuel_level > 0:
                self.__engine_on = True
                print("The car engine has started.")
            else:
                print("No fuel. Cannot start engine.")

    def stop_engine(self):
        if self.__engine_on == True:
            self.__engine_on = False
            print("Engine is turned off.")
        else:
            print("The engine was already turned off.")

    def refuel(self, amount):
        self.__fuel_level += amount
        print(f"Refueling with {amount} litres of fuel.")

    def drive(self, distance):
        fuel_needed = distance/10
        if fuel_needed < self.__fuel_level and self.__engine_on == True:
            self.__fuel_level -= fuel_needed
            print(f"Driving {distance} km.")
        elif self.__engine_on == False:
            print("You need to turn on the engine to be able to drive.")
        else:
            print("Not enough fuel to drive.")
            print(f"Current fuel level: {self.__fuel_level}")

    def display_info(self):
        if self.__engine_on == True: 
            engine_status = "Turned on"
        else:
            engine_status = "Turned off"

        print(f"Year: {self.__year}\nColour: {self.__colour}\nModel: {self.__model}")
        print(f"\nFuel Level: {self.__fuel_level}\nEngine: {engine_status}")

if __name__ == "__main__":
    car1 = Car("Blue", "Ferrari", 2018)

    car1.start_engine()
    car1.drive(800)
    car1.drive(300)
    car1.refuel(11)
    car1.drive(300)
    car1.stop_engine()
    car1.display_info()


