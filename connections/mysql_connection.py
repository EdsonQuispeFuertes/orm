"""Represent the sql server connection with database"""
from typing import List, Tuple

import pymssql
from pymysql.connections import Connection
from pymysql.cursors import Cursor

from connections.connection import ConnectionBase


class MysqlConnection(ConnectionBase):
    """
    is the connection with database
    """

    def __init__(self, parameters_connection: List[str]) -> None:
        """
        :param parameters_connection:
            is a list of the values necessary for the connection
        """
        self.__ip = parameters_connection[0]
        self.__port = parameters_connection[1]
        self.__database = parameters_connection[2]
        self.__user = parameters_connection[3]
        self.__pass = parameters_connection[4]
        self.__cursor = None
        self.__connection = None
        ConnectionBase.__init__(self)

    def send_query(self, consult: str) -> List[Tuple[str]]:
        """
            send a consult to the database and receive a response
        :param consult:
            is a string with the consult to the database
        :return:
            return a list with tuples of the response
        """
        response_consult: List[Tuple[str]] = []
        self._connect()
        if self.__cursor:
            self.__cursor.execute(consult)
            for value in self.__cursor:
                response_consult.append(value)
            self._disconnect()
        return response_consult

    def send_update(self, consult: str) -> int:
        """
            send a consult to the database and don't receive a response
        :param consult:
            is a string with the consult to the database
        :return:
            the id of the new tuple in the table
        """
        id_of_row = 0
        self._connect()
        if self.__connection and self.__cursor:
            print(consult)
            self.__cursor.execute(consult)
            id_of_row = self.__cursor.lastrowid
            self.__connection.commit()  # type: ignore
            self._disconnect()
        return id_of_row

    def _connect(self) -> None:
        """
        Makes the connection to the database
        :return:
        """
        try:
            self.__connection = pymssql.connect(host=self.__ip,
                                                user=self.__user,
                                                password=self.__pass,
                                                database=self.__database)
            self.__cursor = self.__connection.cursor(as_dict=True)
        except Exception as error:
            raise error

    def _disconnect(self) -> None:
        """
        Disconnect the connection to the database
        :return:
        """
        if self.__connection and self.__cursor:
            self.__cursor.close()
            self.__connection.close()
