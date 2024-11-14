
class Event:

    def __init__(self, name, schedule):
        self.__name = name
        self.__schedule = schedule

    def get_name(self) -> str:
        return self.__name
    
    def get_schedule(self) -> str:
        return self.__schedule