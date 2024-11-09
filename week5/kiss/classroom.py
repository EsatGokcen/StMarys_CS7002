class Classroom:

    def __init__(self, teacher=None):
        self.__teacher = teacher
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        self.__students.remove(student)

    def assign_teacher(self, teacher):
        self.__teacher = teacher

    def display_information(self):
        print("Teacher Information:")
        if self.__teacher:
            print(self.__teacher.get_information())
        print("Students Information:")
        for student in self.__students:
            print(student.get_information())