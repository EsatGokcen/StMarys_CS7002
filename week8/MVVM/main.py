from music_model import MusicModel
from music_view_model import MusicViewModel
from music_view import MusicView

def main():
    model = MusicModel()
    view_model = MusicViewModel(model)
    view = MusicView(view_model)

    while True:
        view.show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view.add_song()
        elif choice == '2':
            view.view_songs()
        elif choice == '3':
            view.delete_song()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()