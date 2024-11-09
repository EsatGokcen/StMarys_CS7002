from person import Person

class Teacher(Person):

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.__employee_id = employee_id

    def get_information(self):
        return f'Name: {self.__name}\nAge: {self.__age}\nEmployee ID: {self.__employee_id}'
