from song import Song

class MusicViewModel:
    
    def __init__(self, model):
        self.model = model
        self.songs = model.get_songs()

    def add_song(self, title, artist, genre):
        song = Song(title, artist, genre)
        self.model.add_song(song)
        self.songs = self.model.get_songs()

    def delete_song(self, index):
        self.model.delete_song(index)
        self.songs = self.model.get_songs()