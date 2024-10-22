from week4 import living_thing as lv

class Planet():

    def __init__(self, name=""):
        self.__name = name
        self.__living_things = []

    def __repr__(self):
        return f'planet(name={self.__name}, population={self.population()})'

    def __str__(self):
        return f'Planet is called {self.__name} and has a population of {self.population()}'
    
    def add(self, living_thing):
        if isinstance(living_thing, lv.LivingThing):
            self.__living_things.append(living_thing)
            return True
        return False

    def remove(self, human):
        if human in self.__living_things:
            self.__living_things.remove(human)
            return True
        return False

    def has(self, human):
        return human in self.__living_things

    def population(self):
        return len(self.__living_things)


    