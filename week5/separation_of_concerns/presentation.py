from game_logic import Game

class UserInterface:

    def __init__(self):
        self.__game = Game()

    def get_game(self):
        return self.__game
    
    def display_welcome_message():
        print("Welcome to the Dungeon!")

    def display_current_room(self):
        print("\nCurrent Room: " + self.__game.get_current_room())
    
    def prompt_player_action(self):
        return input("Enter your action (move/fight): ").lower().strip()


