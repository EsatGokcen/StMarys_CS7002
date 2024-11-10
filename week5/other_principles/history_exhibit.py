from exhibit import Exhibit

class HistoryExhibit(Exhibit):
    
    def __init__(self, title, description, curator, era):
        super().__init__(title, description, curator)
        self.__era = era