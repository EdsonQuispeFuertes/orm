import unittest
from querys.delete_query_with_where import QueryDeleteWithWhere


class InsertOracleTest(unittest.TestCase):

    def setUp(self):
        self.delete_query = QueryDeleteWithWhere()

    def test_create_query_2_conditions(self):
        expected = "DELETE FROM student WHERE id=1 and name='marco'"
        values_object = {'id': '1', 'name': "'marco'"}
        actual = self.delete_query.create_query('mysql',
                                                'student',
                                                values_object
                                                )
        self.assertEqual(expected, actual)

    def test_create_query_3_conditions(self):
        expected = "DELETE FROM student WHERE id=1 and name='marco' and last_name='polo'"
        values_object = {'id': '1', 'name': "'marco'", 'last_name': "'polo'"}
        actual = self.delete_query.create_query('mysql',
                                                'student',
                                                values_object)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
