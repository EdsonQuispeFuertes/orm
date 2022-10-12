import unittest
from querys.select_query import QuerySelect


class SelectOracleTest(unittest.TestCase):

    def setUp(self):
        self.select_query = QuerySelect()

    def test_create_query_1_attribute(self):
        list_attributes = {'id': '1'}
        expected = 'select {} from student where id=1'
        actual = self.select_query.create_query('mysql',
                                                'student',
                                                list_attributes,
                                                )
        self.assertEqual(expected, actual)

    def test_create_query_3_attribute(self):
        list_attributes = {'id': '1', 'name': "'marco'", 'last_name': "'polo'"}
        expected = "select {} from student where id=1 or name='marco' or last_name='polo'"
        actual = self.select_query.create_query('mysql',
                                                'student',
                                                list_attributes,
                                                )
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()