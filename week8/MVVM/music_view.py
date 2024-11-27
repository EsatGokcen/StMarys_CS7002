class MusicView:
    
    def __init__(self, view_model):
        self.view_model = view_model

    def show_menu(self):
        print("Music Library Management")
        print("1. Add Song")
        print("2. View Songs")
        print("3. Delete Song")
        print("4. Exit")

    def add_song(self):
        title = input("Enter title of the song: ")
        artist = input("Enter artist of the song: ")
        genre = input("Enter genre of the song: ")
        self.view_model.add_song(title, artist, genre)
        print("Song added successfully.")

    def view_songs(self):
        songs = self.view_model.songs
        if songs:
            print("Your Music Library:")
            for index, song in enumerate(songs):
                print(f"{index + 1}. {song.title} - {song.artist} ({song.genre})")
        else:
            print("Your music library is empty.")

    def delete_song(self):
        self.view_songs()
        if self.view_model.songs:
            index = int(input("Enter the index of the song to delete: ")) - 1
            if 0 <= index < len(self.view_model.songs):
                self.view_model.delete_song(index)
                print("Song deleted successfully.")
            else:
                print("Invalid index.")
        else:
            print("Your music library is empty.")