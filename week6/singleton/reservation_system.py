from attendee import Attendee
from event import Event

class ReservationSystem:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self) -> None:
        self.__attendees = []
        self.__events = []

    def add_attendee(self, attendee: Attendee):
        self.__attendees.append(attendee)
        return f'{attendee.get_name()} with ID: {attendee.get_id()} has been registered.'
    
    def purchase_ticket(self, attendee: Attendee, ticket):
        # logic to check if ticket is valid
        # logic to check if attendee is registered in ticket

        return f'{attendee.get_name()} has purchased {ticket}'
    
    def schedule_event(self, event : Event):
        self.__events.append(event)
        return f'{event.get_name()} has been scheduled to take place on {event.get_schedule()}.'
    
    def retrieve_attendee_info(self):
        list = []
        for attendee in self.__attendees:
            string = f'\nAttendee:\nName: {attendee.get_name()}\nID: {attendee.get_id()}\n'
            list.append(string)
        return "".join(list)

