
class FeedbackSystem:
    
    def __init__(self):
        self.__feedback = []

    def give_feedback(self, visitor, exhibit, rating, comment):
        self.__feedback.append({
            'visitor': visitor,
            'exhibit': exhibit,
            'rating': rating,
            'comment': comment
        })