
class Planet():

    def __init__(self, name="", humans=[]):
        self.__name = name
        self.__humans = humans

    def __repr__(self):
        return f'planet(name={self.__name}, humans={self.__humans})'

    def __str__(self):
        return f'Planet is called {self.__name} and is home to {self.__humans}'