"""This object contains basic methods for all classes that work with the orm"""
from typing import Optional, List, Any


class OrmBaseObject:
    """
        this class contains information for the orm
    """
    def __init__(self) -> None:
        """
        initialize the variables
        """
        self._id = 0
        self._name_table: Optional[str] = None

    def name_table(self) -> Optional[str]:
        """
        :return:
            the name of table
        """
        return self._name_table

    def set_name_table(self, name_table: str) -> None:
        """
            set name of the table
        :param name_table:
            name table
        """
        self._name_table = name_table

    def load_attributes(self, list_arguments: List[Any]) -> None:
        """
            set name of the table
        :param list_arguments:
            list of the values
        """

    def get_id(self) -> int:
        """
        This method returns the object's id
        :return: id
        """
        return self._id
