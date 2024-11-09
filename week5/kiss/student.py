from person import Person

class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id

    def get_information(self):
        return f'Name: {self.__name}\nAge: {self.__age}\nStudent ID: {self.__student_id}'
