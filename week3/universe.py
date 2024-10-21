from planet import Planet
from non_planet import Non_Planet
import random

class Universe():

    def __init__(self):
        self.__planets = []
        self.__non_planets = []

    def generate(self):
        if random.choice( [True, False] ):
            self.__planets.append(Planet())
        else:
            self.__non_planets.append(Non_Planet())

    def display(self):
        print("Planets: ")
        for planet in self.__planets:
            print(planet)
        print("Non-Planets: ")
        for non_planet in self.__non_planets:
            print(non_planet)
    