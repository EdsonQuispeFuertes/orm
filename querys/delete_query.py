"""this file contains the delete query for a database"""
from typing import Dict, Optional
from helpers.functions_orm import search_id
from .base_query import BaseQuery


class QueryDelete(BaseQuery):
    """
    contains the variables and structure for the query Delete
    """
    def __init__(self) -> None:
        """
        initialize dictionary
        """
        self.__query_select = {'oracle': 'DELETE FROM {} WHERE {}',
                               'mysql': 'DELETE FROM {} WHERE {}'}

    def create_query(self, name_data_base: str,
                     name_table: Optional[str],
                     attribute_values: Dict[str, str],
                     ) -> str:
        """
        create the query with the parameters
        :param name_data_base:
            name of the database
        :param name_table:
            is the name of table
        :param attribute_values:
            is the list the attributes of the table
        :return:
            a query in a string
        """
        id_object = search_id(attribute_values)
        query = self.__query_select[name_data_base].format(name_table,
                                                           id_object)
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
