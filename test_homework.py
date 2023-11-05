import unittest
from homework import Person, Student, Teacher, addPerson


class TestUniver(unittest.TestCase):

    # Before each test
    def setUp(self):
        # Creating student list
        self.students = [
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

        self.teacher = Teacher("LB", "Leonid Badeev")

        self.teachers = [
            self.teacher
        ]


# ----------------------------------------------------

# Тест на создание объектов студента и учителя:
#
# Создайте несколько объектов студентов и учителя с разными кодами и именами.
# Убедитесь, что созданные объекты корректно хранят информацию о коде,
# имени и типе (студент или учитель).

    def test_data_code_student(self):
        self.assertEqual(self.students[0].code, "OV", "Wrong student code")

    def test_data_name_student(self):
        self.assertEqual(self.students[0].name,
                         "Oleg Voropaev", "Wrong student name")

    def test_data_type_student(self):
        self.assertEqual(self.students[0].type,
                         "Student", "Wrong student name")

    def test_data_code_teacher(self):
        self.assertEqual(self.teacher.code, "LB", "Wrong teacher code")

    def test_data_name_teacher(self):
        self.assertEqual(self.teacher.name, "Leonid Badeev",
                         "Wrong teacher name")

    def test_data_type_teacher(self):
        self.assertEqual(self.teacher.type, "Teacher", "Wrong teacher name")


# Тест на вывод информации:
# Создайте объекты студентов и учителя.
# Запустите код для вывода информации о них.
# Проверьте, что вывод информации соответствует ожидаемому формату.

    def test_output_student(self):
        real_string = f"Code: {self.students[0].code}, Name: {self.students[0].name}, Type: {self.students[0].type}"
        self.assertEqual(
            real_string, "Code: OV, Name: Oleg Voropaev, Type: Student", "Wrong string output")

    def test_output_teacher(self):
        real_string = f"Code: {self.teacher.code}, Name: {self.teacher.name}, Type: {self.teacher.type}"
        self.assertEqual(
            real_string, "Code: LB, Name: Leonid Badeev, Type: Teacher", "Wrong string output")


# Тест на обработку разных типов объектов:
#
# Попробуйте создать объекты студентов и учителя с неправильными типами данных
# (например, передать строку вместо кода).
# Проверьте, что код корректно обрабатывает такие ситуации и генерирует ошибки
# или исключения при необходимости.


    def test_new_student_wrong_code(self):
        self.new_student = Student("abercadaber", "Obi-Wan “Ben” Kenobi")
        self.assertNotEqual(len(self.new_student.code),
                            2, "Wrong code. Condition len(code) !=2 violated")

    def test_new_techear_wrong_code(self):
        self.new_teacher = Teacher("007", "Sean “Bond” Connery")
        self.assertNotEqual(len(self.new_teacher.code),
                            2, "Wrong code. Condition len(code) !=2 violated")


# Тест на уникальность кодов:
#
# Попробуйте создать объекты студентов и учителя с одинаковыми кодами.
# Убедитесь, что код обрабатывает такие ситуации и не позволяет создать объекты
# с одинаковыми кодами.

    def test_student_unique_code(self):
        init_students_list_size = len(self.students)
        new_student = Student("RT", "Roman Teryoshin")
        self.students = addPerson(self.students, new_student)
        self.assertEqual(
            init_students_list_size, len(self.students), "Wrong list(students) size")

    def test_teacher_unique_code(self):
        init_teachers_list_size = len(self.teachers)
        new_teacher = Teacher("LB", "Leonid Badeev")
        self.teachers = addPerson(self.teachers, new_teacher)
        self.assertEqual(
            init_teachers_list_size, len(self.teachers), "Wrong list(teachers) size")

# Тест на изменение информации:
#
# Создайте объект студента.
# Измените его имя или тип.
# Убедитесь, что информация об объекте корректно обновляется.

    def test_new_student_change_code(self):
        self.newStudent = Student("OB", "Obi-Wan “Ben” Kenobi")
        self.newStudent.code = "DV"
        self.assertEqual(self.newStudent.code, "DV", "Wrong Star Wars code")

    def test_new_student_change_name(self):
        self.newStudent = Student("OB", "Obi-Wan “Ben” Kenobi")
        self.newStudent.name = "Forrest"
        self.assertEqual(self.newStudent.name, "Forrest", "Wrong run-run code")
