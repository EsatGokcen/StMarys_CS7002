from human import Human

class Planet():

    def __init__(self, name=""):
        self.__name = name
        self.__humans = []

    def __repr__(self):
        return f'planet(name={self.__name}, population={self.population()})'

    def __str__(self):
        return f'Planet is called {self.__name} and has a population of {self.population()}'
    
    def add(self, human):
        if isinstance(human, Human):
            self.__humans.append(human)
            return True
        return False

    def remove(self, human):
        if human in self.__humans:
            self.__humans.remove(human)
            return True
        return False

    def has(self, human):
        return human in self.__humans

    def population(self):
        return len(self.__humans)


    