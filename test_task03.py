import unittest
from task03 import Person, Student, Teacher


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

    def test_data(self):
        # for student in self.students:
        #     print(
        #         f"Code: {student.code}, Name: {student.name}, Type: {student.type}")
        self.assertEqual(self.students[0].code, "OV", "Wrong student code")
        self.assertEqual(self.teacher.code, "LB", "Wrong teacher code")

    def test_output(self):
        real_string = f"Code: {self.students[0].code}, Name: {self.students[0].name}, Type: {self.students[0].type}"
        self.assertEqual(
            real_string, "Code: OV, Name: Oleg Voropaev, Type: Student", "Wrong string output")

    def test_new_student_change_name(self):
        self.newStudent = Student("OB", "Obi-Wan “Ben” Kenobi")
        self.newStudent.code = "DV"
        self.assertEqual(self.newStudent.code, "DV", "Wrong Star Wars code")

# Тест на создание объектов студента и учителя:
#
# Создайте несколько объектов студентов и учителя с разными кодами и именами.
# Убедитесь, что созданные объекты корректно хранят информацию о коде,
# имени и типе (студент или учитель).

# Тест на вывод информации:
# Создайте объекты студентов и учителя.
# Запустите код для вывода информации о них.
# Проверьте, что вывод информации соответствует ожидаемому формату.


# Тест на обработку разных типов объектов:
#
# Попробуйте создать объекты студентов и учителя с неправильными типами данных
# (например, передать строку вместо кода).
# Проверьте, что код корректно обрабатывает такие ситуации и генерирует ошибки
# или исключения при необходимости.
# Тест на уникальность кодов:
#
# Попробуйте создать объекты студентов и учителя с одинаковыми кодами.
# Убедитесь, что код обрабатывает такие ситуации и не позволяет создать объекты
# с одинаковыми кодами.


# Тест на изменение информации:
#
# Создайте объект студента.
# Измените его имя или тип.
# Убедитесь, что информация об объекте корректно обновляется.
