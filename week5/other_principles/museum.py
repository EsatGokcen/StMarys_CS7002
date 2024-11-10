from feedback_system import FeedbackSystem

class Museum:

    def __init__(self):
        self.__exhibits = []
        self.__visitors = []
        self.__feedback_system = FeedbackSystem()

    def add_exhibit(self, exhibit):
        self.__exhibits.append(exhibit)

    def add_visitor(self, visitor):
        self.__visitors.append(visitor)

    def receive_feedback(self, visitor, exhibit, rating, comment):
        self.__feedback_system.give_feedback(visitor, exhibit, rating, comment)

    def get_exhibits(self):
        return self.__exhibits

    def get_visitors(self):
        return self.__visitors