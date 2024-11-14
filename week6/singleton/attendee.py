
class Attendee:

    initial_id = 1000

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__id = Attendee.initial_id
        Attendee.initial_id += 1

    def get_name(self) ->  str:
        return self.__name
    
    def get_id(self) -> int:
        return self.__id
        

