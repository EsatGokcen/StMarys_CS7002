from exhibit import Exhibit

class ArtExhibit(Exhibit):

    def __init__(self, title, description, curator, artist):
        super().__init__(title, description, curator)
        self.__artist = artist
        