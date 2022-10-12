"""
This file contains a abstract class of the connection
"""
from typing import List, Tuple
from abc import ABC, abstractmethod


class ConnectionBase(ABC):
    """
    Is the class abstract connection
    """
    def __init__(self) -> None:
        """
        :return:
            No return
        """

    @abstractmethod
    def send_query(self, consult: str) -> List[Tuple[str]]:
        """
            send a consult to the data base
        :param consult:
            is a string with the consult to the data base
        :return:
            return a list with tuples of the response
        """

    @abstractmethod
    def send_update(self, consult: str) -> int:
        """
            send a consult to the data base and don't receive a response
        :param consult:
            is a string with the consult to the data base
        :return:
            No return
        """

    @abstractmethod
    def _connect(self) -> None:
        """
            this method realize the connection to the data base
        :return:
            No return
        """

    @abstractmethod
    def _disconnect(self) -> None:
        """
            this method realize the disconnection to the data base
        :return:
            No return
        """
