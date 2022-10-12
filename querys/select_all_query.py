"""this file contains the select query for a database"""
from typing import Dict, Optional

from .base_query import BaseQuery


class QuerySelectAll(BaseQuery):
    """
    contains the variables and structure for the query select all
    """

    def __init__(self) -> None:
        """
        initialize dictionary
        """
        self.__query_select = {'oracle': 'select * from {}',
                               'mysql': 'select * from {}'}

    def create_query(self, name_data_base: str, name_table: Optional[str],
                     attribute_values: Dict[str, str]) -> str:
        """
        This method creates a query with the parameters entered, returning a query
        :param name_data_base:
            name of the database
        :param name_table:
            is the name of table
        :param attribute_values:
            is the list the attributes of the table
        :return:
            a query in a string
        """
        query = self.__query_select[name_data_base].format(name_table)
        return query

    def get_template(self, name_database: str) -> str:
        """
        return the template of a database
        :param name_database:
            name of the database
        :return:
            the template of query of the database
        """
        return self.__query_select[name_database]
