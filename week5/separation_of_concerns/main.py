from presentation import UserInterface

def main():
    ui = UserInterface()
    ui.display_welcome_message()
    game = ui.get_game

    while game.get_player_health() > 0:
        ui.display_current_room()
        action = ui.prompt_player_action()
        if action == 'move':
            game.move()
        elif action == 'fight':
            game.fight()
        else:
            print("Invalid action! Please try again.")

if __name__ == '__main__':
    main()

