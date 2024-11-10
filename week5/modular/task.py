
class Task:

    def __init__(self, title, description):
        self.__title = title
        self.__description = description
        self.__status = "New"
        self.__assigned_to = None

    def assign_to_user(self, user):
        self.__assigned_to = user
        self.__status = "Assigned"

    def complete(self):
        self.__status = "Complete"

    def display_info(self):
        print("Title:", self.__title)
        print("Description:", self.__description)
        print("Assigned To:", self.__assigned_to)
        print("Status:", self.__status)

    