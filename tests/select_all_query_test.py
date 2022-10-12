import unittest

from querys.select_all_query import QuerySelectAll


class SelectOracleTest(unittest.TestCase):

    def setUp(self):
        self.select_query = QuerySelectAll()

    def test_create_query(self):
        expected = 'select * from STUDENT'
        actual = self.select_query.create_query('mysql',
                                                'STUDENT',
                                                {"": ""})
        self.assertEqual(expected, actual)

    def test_get_template(self):
        expected = "select * from {}"
        actual = self.select_query.get_template("mysql")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
