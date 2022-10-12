"""this file contains the select query for a database"""
from typing import Dict, Optional

from helpers.functions_orm import match_attributes_values
from .base_query import BaseQuery


class QuerySelectAllWhitWhere(BaseQuery):
    """
    contains the variables and structure for the query select all with where
    """

    def __init__(self) -> None:
        """
        initialize dictionary
        """
        self.__query_select = {'oracle': 'select * from {} where {}',
                               'mysql': 'select * from {} where {}'}
        self.__conditional_where = 'and'

    def create_query(self, name_data_base: str, name_table: Optional[str],
                     attribute_values: Dict[str, str]) -> str:
        """create the query with the parameters
        :param name_data_base:
            name of the database
        :param name_table:
            is the name of table
        :param attribute_values:
            is the list the conditions of the table
        :return:
            a query in a string"""
        conditional: str = self.__conditional_where
        conditions = match_attributes_values(attribute_values,
                                             conditional)
        query = self.__query_select[name_data_base].format(
            name_table, conditions)
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
