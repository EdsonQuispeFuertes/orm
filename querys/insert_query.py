"""this file contains the insert query for a database"""
from typing import Dict, Optional
from helpers.functions_orm import get_list_attributes
from .base_query import BaseQuery


class QueryInsert(BaseQuery):
    """
    contains the variables and structure for the query Insert
    """
    def __init__(self) -> None:
        """
        initialize dictionary
        """
        self.__query_select = {'oracle': 'INSERT INTO {}({}) VALUES({})',
                               'mysql': 'INSERT INTO {} ({}) VALUES({})'}

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
        attributes, values = get_list_attributes(attribute_values)
        query = self.__query_select[name_data_base].format(name_table,
                                                           attributes,
                                                           values)
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
