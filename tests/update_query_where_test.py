import unittest
from querys.update_query_with_where import QueryUpdateWithWhere


class UpdateWhereTest(unittest.TestCase):

    def setUp(self):
        self.update_query = QueryUpdateWithWhere()

    def test_create_query_two_where_condition(self):
        expected = "UPDATE student SET name='marco',last_name='polo' WHERE id=1 and name='marco'"
        values_object = {'name': "'marco'", 'last_name': "'polo'"}
        where_conditions = {'id': '1', 'name': "'marco'"}
        actual = self.update_query.create_query_where('student',
                                                      values_object,
                                                      where_conditions)
        self.assertEqual(expected, actual)

    def test_create_query_three_conditions(self):
        expected = "UPDATE student SET name='marco',last_name='Polo' WHERE id=1 and name='marco' and last_name='polo'"
        values_object = {'id': '1', 'name': "'marco'", 'last_name': "'Polo'"}
        where_conditions = {'id': '1', 'name': "'marco'", 'last_name': "'polo'"}
        actual = self.update_query.create_query_where('student',
                                                      values_object,
                                                      where_conditions)
        self.assertEqual(expected, actual)

    def test_create_query_1_attribute(self):
        expected = "UPDATE student SET name='marco',last_name='polo' WHERE id=1"
        values_object = {'id': '1', 'name': "'marco'", 'last_name': "'polo'"}
        actual = self.update_query.create_query('mysql',
                                                'student',
                                                values_object)
        self.assertEqual(expected, actual)

    def test_create_query_3_attribute(self):
        expected = "UPDATE student SET name='marco',last_name='polo' WHERE id=1"
        values_object = {'id': '1', 'name': "'marco'", 'last_name': "'polo'"}
        actual = self.update_query.create_query('mysql',
                                                'student',
                                                values_object)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
