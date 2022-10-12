import unittest
from unittest.mock import MagicMock

from connections.mysql_connection import MysqlConnection
from connections.orm import Orm
from tests.classes_to_test_orm.student import Student


class MysqlTest(unittest.TestCase):

    def setUp(self):
        parameters_connection = ['localhost', 3306, 'orm', 'edson', 'password']
        self.connection = MysqlConnection(parameters_connection)
        self.orm = Orm(self.connection, 'mysql', 'tests.classes_to_test_orm')

    def test_search_objects(self):
        self.connection.send_query = MagicMock(return_value=[(1, 'Bob', 'Dum', 'F', 'bob@dum.net', 4)])
        list_student = self.orm.search_objects(Student(),
                                               {'id': 1}
                                               )
        number_students = 1
        actual = len(list_student)
        self.assertEqual(number_students, actual)

        expected = "id: 1\nname: Bob\nlast name: Dum\ngender: F\ne-mail: bob@dum.net"
        actual = str(list_student[0])
        self.assertEqual(expected, actual)

    def test_search_objects_2(self):
        self.connection.send_query = MagicMock(return_value=[(1, 'Marco', 'Dum', 'F', 'bob@dum.net', 4),
                                                             (2, 'Marco', 'Polo', 'M', 'bder0@cnel.net', 1)
                                                             ])
        self.orm.set_conditional_where_select("or")
        list_student = self.orm.search_objects(Student(),
                                               {'first_name': 'Marco'}
                                               )
        number_students = 2
        actual = len(list_student)
        self.assertEqual(number_students, actual)

        expected = "id: 1\nname: Marco\nlast name: Dum\ngender: F\ne-mail: bob@dum.net"
        actual = str(list_student[0])
        self.assertEqual(expected, actual)

        expected = "id: 2\nname: Marco\nlast name: Polo\ngender: M\ne-mail: bder0@cnel.net"
        actual = str(list_student[1])
        self.assertEqual(expected, actual)

    def test_insert_object(self):
        self.connection.send_update = MagicMock(return_value=1)
        student = Student()
        student.load_attributes([0, "marco", "polo", "M", "m@p.m", 1])
        id_student = self.orm.save_object(student)
        actual = 1
        self.assertEqual(id_student, actual)

    def test_update_object(self):
        self.connection.send_update = MagicMock(return_value=1)
        student = Student()
        student.load_attributes([0, "marco", "polo", "M", "m@p.m", 1])
        id_student = self.orm.update(student)
        actual = 1
        self.assertEqual(id_student, actual)

    def test_update_with_where(self):
        self.connection.send_update = MagicMock(return_value=1)
        student = Student()
        student.load_attributes([0, "marco", "polo", "M", "m@p.m", 1])
        id_student = self.orm.update_with_conditions(student, {'first_name': 'Marco'})
        actual = 1
        self.assertEqual(id_student, actual)

    def test_delete_object(self):
        self.connection.send_update = MagicMock(return_value=1)
        student = Student()
        student.load_attributes([1, "marco", "polo", "M", "m@p.m", 1])
        id_student = self.orm.object_delete(student)
        actual = 1
        self.assertEqual(id_student, actual)

    def test_delete_with_where(self):
        self.connection.send_update = MagicMock(return_value=1)
        student = Student()
        student.load_attributes([1, "marco", "polo", "M", "m@p.m", 1])
        id_student = self.orm.delete_with_where(student, {'first_name': 'Marco'})
        actual = 1
        self.assertEqual(id_student, actual)

    def test_get_objects_from_the_table(self):
        self.connection.send_query = MagicMock(
            return_value=[(1, 'Andres', 'Dum', 'F', 'bdrummer0@cpanel.net', 4),
                          (2, 'Mateo', 'Polo', 'M', 'bder0@cnel.net', 1)])
        list_objects = self.orm.get_objects_from_the_table(Student())
        number_objects = 2
        actual = len(list_objects)
        self.assertEqual(number_objects, actual)

    def test_get_objects_from_the_table_whit_where(self):
        self.connection.send_query = MagicMock(
            return_value=[(1, 'Andres', 'Dum', 'F', 'bdrummer0@cpanel.net', 4),
                          (2, 'Mateo', 'Polo', 'M', 'bder0@cnel.net', 1)])
        list_objects = self.orm.get_objects_from_the_table_with_where(
            Student(), {"id": 1})
        number_objects = 2
        actual = len(list_objects)
        self.assertEqual(number_objects, actual)


if __name__ == '__main__':
    unittest.main()
