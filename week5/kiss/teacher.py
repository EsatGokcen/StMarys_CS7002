from person import Person

class Teacher(Person):

    def __init__(self, name, age, employee_id, address, email, phone):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__address = address
        self.__email = email
        self.__phone = phone

    def get_information(self):
        large_string =  f'''Name: {self.__name}\nAge: {self.__age}\nEmployee ID: {self.__employee_id}
                            \nAddress: {self.__address}\nEmail: {self.__email}\nPhone Number: {self.__phone}'''
        return large_string
