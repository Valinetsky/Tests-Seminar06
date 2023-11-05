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
    Student("RT", "Roman Teryoshin"),
    Student("RT", "Roman Teryoshin"),
    Student("AP", "Alexandr Politov"),
]

# Creating teacher list
teacher = Teacher("LB", "Leonid Badeev")

teachers = [
    teacher
]


def listCleanUp(persons):
    persons = list(
        {person.code: person for person in persons}.values())
    print("+++++++++++++++++++++++++++++++++++++++")
    for pers in persons:
        print(pers.code + " " + pers.name)
    return persons


unique_students = listCleanUp(students)
unique_teachers = listCleanUp(teachers)


def addPerson(persons, person):
    flag = 0
    for pers in persons:
        if pers.code == person.code:
            flag = 1
    if flag == 0:
        persons.append(person)
    return persons


print("=================")
print("unique student list before adding same student object")
for st in unique_students:
    print(st.code + " " + st.name)

# Addin copy of an existing student
unique_students = addPerson(unique_students, Student("RT", "Roman Teryoshin"))
unique_students = addPerson(unique_students, Student("RT", "Roman Teryoshin"))
unique_students = addPerson(unique_students, Student("RT", "Roman Teryoshin"))
unique_students = addPerson(unique_students, Student("TR", "Teryoshin Roman"))

# Addin new student
unique_students = addPerson(unique_students, Student("ZC", "Zero Cool"))

# Addin copy of an existing teacher
unique_teacherss = addPerson(unique_teachers, Teacher("LB", "Leonid Badeev"))

# Addin new teacher
unique_teacherss = addPerson(unique_teachers, Teacher("BL", "Badeev Leonid"))


print("=================")
print("unique student list after adding same student object")
for st in unique_students:
    print(st.code + " " + st.name)

print("=================")
print("unique teacher list")
for te in unique_teachers:
    print(te.code + " " + te.name)
