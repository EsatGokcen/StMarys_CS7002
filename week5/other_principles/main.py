from museum import Museum
from art_exhibit import ArtExhibit
from history_exhibit import HistoryExhibit
from science_exhibit import ScienceExhibit
from visitor import Visitor
from analytics import Analytics

def main():

    museum = Museum()

    # Creating exhibits
    mona_lisa = ArtExhibit("Mona Lisa", "Famous painting by Leonardo da Vinci", "Lisa Gherardini", "Leonardo da Vinci")
    egypt_exhibit = HistoryExhibit("Ancient Egypt", "Exhibit showcasing artifacts from ancient Egypt", "Dr. Smith", "Ancient Egypt")
    robotics_exhibit = ScienceExhibit("Robotics", "Exhibit demonstrating advancements in robotics", "Dr. Johnson", "Robotics")

    museum.add_exhibit(mona_lisa)
    museum.add_exhibit(egypt_exhibit)
    museum.add_exhibit(robotics_exhibit)

    # Creating visitors
    visitor1 = Visitor("John")
    visitor2 = Visitor("Alice")

    museum.add_visitor(visitor1)
    museum.add_visitor(visitor2)

    # Giving feedback
    museum.receive_feedback(visitor1, mona_lisa, 5, "Absolutely stunning!")
    museum.receive_feedback(visitor2, egypt_exhibit, 4, "Very informative.")

    # Analysing feedback
    analytics = Analytics(museum._Museum__feedback_system)
    analytics.analyse_feedback()

if __name__ == '__main__':
    main()