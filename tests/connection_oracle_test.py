import unittest

from unittest.mock import MagicMock, patch
from connections.oracle_connection import OracleConnection


class ConnectionOracleTest(unittest.TestCase):

    @patch('source_orm.oracle_connection.cx_Oracle.connect.cursor')
    @patch('source_orm.oracle_connection.cx_Oracle.connect')
    def test_search_objects(self, connect_mock, cursor_mock):
        parameters_connection = ['localhost', 3306, 'hangman', 'hangman', 'password']
        my_connection = OracleConnection(parameters_connection)
        connect_mock.connect = MagicMock(return_value=connect_mock)
        connect_mock.cursor = MagicMock(return_value=cursor_mock)
        cursor_mock.execute = MagicMock(return_value=[])
        connect_mock().cursor().lastrowid = 0
        lastid = my_connection.send_update("select * from STUDENT WHERE id = 1")
        my_connection.send_query("select * from STUDENT WHERE id = 1")
        self.assertEqual(lastid, 0)


if __name__ == '__main__':
    unittest.main()
