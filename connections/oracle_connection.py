"""
Represent the oracle connection with database
"""
import cx_Oracle
from typing import List, Tuple
from connections.connection import ConnectionBase


class OracleConnection(ConnectionBase):
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
        self.__service_name = parameters_connection[2]
        self.__user = parameters_connection[3]
        self.__pass = parameters_connection[4]
        self.__connection = None
        self.__cursor = None
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
            send a consult to the data base and don't receive a response
        :param consult:
            is a string with the consult to the data base
        :return:
            No return
        """
        id_tuple = 0
        self._connect()
        if self.__cursor and self.__connection:
            self.__cursor.execute(consult)
            self.__connection.commit()
        self._disconnect()
        return id_tuple

    def _connect(self) -> None:
        """
            this method realize the connection to the data base
        :return:
            No return
        """
        dsn_tns = cx_Oracle.makedsn(self.__ip,
                                    self.__port,
                                    service_name=self.__service_name)
        self.__connection = cx_Oracle.connect(user=self.__user,
                                              password=self.__pass,
                                              dsn=dsn_tns)
        if isinstance(self.__connection, cx_Oracle.Connection):
            self.__cursor = self.__connection.cursor()

    def _disconnect(self) -> None:
        """
            this method realize the disconnection to the data base
        :return:
            No return
        """
        if self.__cursor and self.__connection:
            self.__cursor.close()
            self.__connection.close()
        self.__connection = None
        self.__cursor = None
