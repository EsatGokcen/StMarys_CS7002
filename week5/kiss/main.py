from student import Student
from teacher import Teacher
from classroom import Classroom

def main():

    student1 = Student('Esat', 23, 'ID01')
    student2 = Student('Muto', 32, 'ID02')
    student3 = Student('Taha', 24, 'ID03')

    teacher1 = Teacher('Prins', 40, 'SID01', 'Somewhere IDK', 'prins@hot.com' , '07391347123')
    teacher2 = Teacher('Harshil', 42, 'SID02', 'Somewhere else IDK', 'harshil@hot.com' , '03995367424')

    classroom1 = Classroom()
    classroom2 = Classroom()

    classroom1.assign_teacher(teacher1)
    classroom1.add_student(student1)
    classroom1.add_student(student2)
    classroom1.add_student(student3)

    classroom2.assign_teacher(teacher2)
    classroom2.add_student(student1)
    classroom2.add_student(student2)
    classroom2.add_student(student3)

    classroom1.display_information()
    classroom2.display_information()

if __name__ == '__main__':
    main()