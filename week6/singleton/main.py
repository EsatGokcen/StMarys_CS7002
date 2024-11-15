from reservation_system import ReservationSystem
from attendee import Attendee

def main():
    
    res1 = ReservationSystem()
    res2 = ReservationSystem()

    attendee1 = Attendee('Esat')
    attendee2 = Attendee('Taha')

    print(res1 is res2) #if output True, singleton works

    res1.add_attendee(attendee1)
    res1.add_attendee(attendee2)
    
    res2.add_attendee(attendee2)
    
    print(res1.retrieve_attendee_info())

if __name__ == '__main__':
    main()