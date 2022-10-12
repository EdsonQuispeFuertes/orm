import unittest
from querys.delete_query import QueryDelete


class InsertOracleTest(unittest.TestCase):

    def setUp(self):
        self.delete_query = QueryDelete()

    def test_create_query_1_attribute(self):
        expected = "DELETE FROM student WHERE id=1"
        values_object = {'id': '1'}
        actual = self.delete_query.create_query('mysql',
                                                'student',
                                                values_object
                                                )
        self.assertEqual(expected, actual)

    def test_create_query_3_attribute(self):
        expected = "DELETE FROM student WHERE id=1"
        values_object = {'id': '1', 'name': "'marco'", 'last_name': "'polo'"}
        actual = self.delete_query.create_query('mysql',
                                                'student',
                                                values_object)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
