import unittest
from querys.insert_query import QueryInsert


class InsertOracleTest(unittest.TestCase):

    def setUp(self):
        self.insert_query = QueryInsert()

    def test_create_query_1_attribute(self):
        list_attributes = {'id': '1'}
        expected = "INSERT INTO student(id) VALUES(1)"
        actual = self.insert_query.create_query('mysql',
                                                'student',
                                                list_attributes)
        self.assertEqual(expected, actual)

    def test_create_query_3_attribute(self):
        list_attributes = {'id': '1', 'name': "'marco'", 'last_name': "'polo'"}
        expected = "INSERT INTO student(id,name,last_name) VALUES(1,'marco','polo')"
        actual = self.insert_query.create_query('mysql',
                                                'student',
                                                list_attributes)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
