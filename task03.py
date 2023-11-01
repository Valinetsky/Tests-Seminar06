class Person:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class Student(Person):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.type = "Student"


class Teacher(Person):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.type = "Teacher"


# Creating student list
students = [
    Student("OV", "Oleg Voropaev"),
    Student("SK", "Sergey Kazitsyn"),
    Student("MB", "Maxim Bobkov"),
    Student("EN", "Elena Nekraschevich"),
    Student("DA", "Dmitry Artemiev"),
    Student("IP", "Irina Peshkova"),
    Student("TN", "Timur Nikolaev"),
    Student("RT", "Roman Teryoshin"),
    Student("AP", "Alexandr Politov"),
]

teacher = Teacher("LB", "Leonid Badeev")

# Information output (students and teacher)
for student in students:
    print(f"Code: {student.code}, Name: {student.name}, Type: {student.type}")

print(f"Code: {teacher.code}, Name: {teacher.name}, Type: {teacher.type}")
