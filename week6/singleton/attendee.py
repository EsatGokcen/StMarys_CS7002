
class Attendee:

    initial_id = 1000

    def __init__(self, name):
        self.__name = name
        self.__id = Attendee.initial_id
        Attendee.initial_id += 1

