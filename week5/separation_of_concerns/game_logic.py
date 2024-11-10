
class Game:

    def __init__(self):
        self.__current_room = "Entrance"
        self.__player_health = 100
        self.__player_inventory = []

    def get_current_room(self):
        return self.__current_room
    
    def get_player_health(self):
        return self.__player_health
    
    def get_player_inventory(self):
        return self.__player_inventory
    
    def move(self):
        print("You move to another room.")
        # Code to handle movement logic
        pass

    def fight(self):
        print("You encounter a monster!")
        # Code to handle combat logic
        pass