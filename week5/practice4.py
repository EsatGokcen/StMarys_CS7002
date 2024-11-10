
# Separation of Concerns 

# is a fundamental design principle in software engineering 
# that advocates breaking a system into distinct sections, 
# each addressing a separate concern or responsibility. 
# This principle helps in managing complexity, 
# improving maintainability, and promoting reusability

#Practice: Use Separation of Concerns and rewrite the code below:

class Game:

    def __init__(self):
        self.__current_room = "Entrance"
        self.__player_health = 100
        self.__player_inventory = []

    def play_game(self):
        print("Welcome to the Dungeon!")
        while self.__player_health > 0:
            print("\nCurrent Room:", self.__current_room)
            action = input("Enter your action (move/fight): ").lower().strip()
            if action == "move":
                self.move()
            elif action == "fight":
                self.fight()
            else:
                print("Invalid action! Please try again.")

    def move(self):
        print("You move to another room.")
        # Code to handle movement logic
        pass

    def fight(self):
        print("You encounter a monster!")
        # Code to handle combat logic
        pass

# Instantiate and play the game
game = Game()
game.play_game()