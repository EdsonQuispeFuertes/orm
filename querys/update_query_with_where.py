"""this file contains the update query for a database"""
from typing import Dict, Optional
from helpers.functions_orm import values_replace, match_attributes_values, search_id
from .base_query_where import BaseQueryWhere


class QueryUpdateWithWhere(BaseQueryWhere):
    """
    contains the variables and structure for the query update
    """
    def __init__(self) -> None:
        """
        initialize dictionary
        """
        self.__query_select = {'oracle': 'UPDATE {} SET {} WHERE {}',
                               'mysql': 'UPDATE {} SET {} WHERE {}'
                               }
        self.__conditional_where = 'and'

    def create_query(self, name_data_base: str, name_table: Optional[str],
                     attribute_values: Dict[str, str],
                     ) -> str:
        """
        create the query with the parameters
        :param name_data_base:
            name of the  database
        :param name_table:
            is the name of table
        :param attribute_values:
            is the list the attributes of the table
        :return:
            a query in a string
        """
        identify = search_id(attribute_values)
        del attribute_values['id']
        values_to_replace = values_replace(attribute_values)
        query = self.__query_select[name_data_base].format(name_table,
                                                           values_to_replace,
                                                           identify)
        return query

    def create_query_where(self, name_table: Optional[str],
                           attribute_values: Dict[str, str],
                           condition_values: Dict[str, str]
                           ) -> str:
        """
        create the query with the parameters
        :param name_table:
            name of the table
        :param attribute_values:
            is the list the attributes of the table
        :param condition_values:
            is the list the conditions of the table
        :return:
            a query in a string
        """
        glue_semantic: str = self.__conditional_where
        conditions = match_attributes_values(condition_values,
                                             glue_semantic)
        values_to_replace = values_replace(attribute_values)
        query = self.__query_select['mysql'].format(name_table,
                                                    values_to_replace,
                                                    conditions)
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
