"""
This file contains a representation of the
table database.
"""
from typing import List, Any
from connections.orm_base_object import OrmBaseObject


class Student(OrmBaseObject):
    def __init__(self):
        super().__init__()
        self.__first_name = ""
        self.__last_name = ""
        self.__gender = ''
        self.__email = ''
        self.__id_university = 0

    def __str__(self) -> str:
        """
            representation of student object
        :return:
            the values of the object
        """
        return 'id: ' + str(self._id) + '\nname: ' \
               + self.__first_name + '\nlast name: ' \
               + self.__last_name + '\ngender: ' \
               + self.__gender + '\ne-mail: ' \
               + self.__email

    def load_attributes(self, list_arguments: List[Any]) -> None:
        """
            this function load the values
            in the variables in this object
        :param list_arguments:
            is a list of values
        """
        self._id = list_arguments[0]
        self.__first_name = list_arguments[1]
        self.__last_name = list_arguments[2]
        self.__gender = list_arguments[3]
        self.__email = list_arguments[4]
