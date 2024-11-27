class MusicModel:
    
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_songs(self):
        return self.songs

    def delete_song(self, index):
        del self.songs[index]