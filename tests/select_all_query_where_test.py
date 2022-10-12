import unittest

from querys.select_all_query_with_where import QuerySelectAllWhitWhere


class SelectOracleTest(unittest.TestCase):

    def setUp(self):
        self.select_query = QuerySelectAllWhitWhere()

    def test_create_query(self):
        expected = 'select * from STUDENT where id=1'
        actual = self.select_query.create_query('mysql',
                                                'STUDENT',
                                                {"id": "1"})
        self.assertEqual(expected, actual)

    def test_create_query_2_conditions(self):
        expected = "select * from STUDENT where id=1 and state='for buying'"
        actual = self.select_query.create_query('mysql',
                                                'STUDENT',
                                                {"id": "1",
                                                 "state": "'for buying'"})
        self.assertEqual(expected, actual)

    def test_get_template(self):
        expected = "select * from {} where {}"
        actual = self.select_query.get_template("mysql")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
