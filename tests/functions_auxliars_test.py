import unittest
from helpers.functions_orm import *
from tests.classes_to_test_orm.student import Student


class InsertOracleTest(unittest.TestCase):

    def test_match_attributes(self):
        list_attributes = {'a': '1', 'b': '2', 'c': "'3'", 'd': "'4'", 'e': "'5'"}
        expected = "a=1 and b=2 and c='3' and d='4' and e='5'"
        actual = match_attributes_values(list_attributes, 'and')
        self.assertEqual(expected, actual)

    def test_get_name_class(self):
        std = Student()
        expected = 'STUDENT'
        actual = get_name_table(std)
        self.assertEqual(expected, actual)

    def test_get_name_class_setting(self):
        std = Student()
        std.set_name_table('student_1')
        expected = 'student_1'
        actual = get_name_table(std)
        self.assertEqual(expected, actual)

    def test_list_attributes_values(self):
        std = Student()
        std.load_attributes([1, 'marco', 'polo', 'm', 'c@c', 1])
        expected_attributes = {"id": '1', "first_name": "'marco'", "last_name": "'polo'", "gender": "'m'", "email": "'c@c'", "id_university": "1", "name_table": "None"}
        actual_attributes = list_attributes_values(std)
        self.assertEqual(expected_attributes, actual_attributes)

    def test_search_id(self):
        list_attributes = {"id": "1", "first_name": "'marco'", "last_name": "'polo'", "gender": "'m'", "email": "'c@c'", "id_university": "1"}
        expected = 'id=1'
        actual = search_id(list_attributes)
        self.assertEqual(expected, actual)

    def test_values_replace(self):
        list_attributes = {"id": "1", "first_name": "'marco'", "last_name": "'polo'", "gender": "'m'", "email": "'c@c'", "id_university": "1"}
        expected = "first_name='marco',last_name='polo',gender='m',email='c@c',id_university=1"
        actual = values_replace(list_attributes)
        self.assertEqual(expected, actual)

    def test_parameter_configuration_mysql(self):
        actual = get_parameters_file("../tests/", "mysql")
        expected = ['localhost', 3306, 'orm', 'edson', 'password']
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
