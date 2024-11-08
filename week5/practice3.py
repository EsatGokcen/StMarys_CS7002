# Improve the code using KISS principles 
# (Keep It Simple, Stupid)

class Person:
    def __init__(self, name, age, address=None, email=None, phone=None):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__email = email
        self.__phone = phone

class Student(Person):
    def __init__(self, name, age, student_id_number, address=None, email=None, phone=None):
        super().__init__(name, age, address, email, phone)
        self.__student_id_number = student_id_number

    def get_information_for_the_student(self):
        return f"Name: {self.__name}, Age: {self.__age}, ID Number: {self.__student_id_number}"

class Teacher(Person):
    def __init__(self, name, age, employee_id, address=None, email=None, phone=None):
        super().__init__(name, age, address, email, phone)
        self.__employee_id = employee_id

    def get_information_for_the_teacher(self):
        return f"Name: {self.__name}, Age: {self.__age}, Employee ID: {self.__employee_id}"

class AbstractClassroom:
    def future_operation(self):
        raise NotImplementedError()

class Classroom(AbstractClassroom):
    def __init__(self, students=None, teacher=None):
        self.__students = students if students else []
        self.__teacher = teacher

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        self.__students.remove(student)

    def assign_teacher(self, teacher):
        self.__teacher = teacher

    def display_information_for_the_class(self):
        print("Teacher Information:")
        print(self.__teacher.get_information_for_the_teacher())
        print("Students Information:")
        for student in self.__students:
            print(student.get_information_for_the_student())

# Example usage:
teacher = Teacher("John Doe", 35, "T123", "123 Main St", "john@example.com", "123-456-7890")
students = [Student("Alice", 18, "S001"), Student("Bob", 17, "S002")]
classroom = Classroom(students, teacher)
classroom.display_information_for_the_class()