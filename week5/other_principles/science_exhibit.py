from exhibit import Exhibit

class ScienceExhibit(Exhibit):

    def __init__(self, title, description, curator, topic):
        super().__init__(title, description, curator)
        self.__topic = topic