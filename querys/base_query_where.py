"""this file contains the template for the query for a database"""
from abc import ABC, abstractmethod
from typing import Dict, Optional

from querys.base_query import BaseQuery


class BaseQueryWhere(BaseQuery, ABC):
    """
        contains the methods for the query that use where
    """

    @abstractmethod
    def create_query_where(self,
                           name_table: Optional[str],
                           attribute_values: Dict[str, str],
                           condition_values: Dict[str, str]
                           ) -> str:
        """
        is the template for query
        :param name_table:
        :param attribute_values:
        :param condition_values:
        :return:
        """

    @abstractmethod
    def get_template(self, name_database: str) -> str:
        """
        return the template of a database
        :param name_database:
            name of the database
        :return:
            the template of query of the database
        """
