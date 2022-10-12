"""this file contains the template for the query for a database"""
from abc import ABC, abstractmethod
from typing import Dict, Optional


class BaseQuery(ABC):
    """
        contains the methods for the query
    """

    @abstractmethod
    def create_query(self,
                     name_data_base: str,
                     name_table: Optional[str],
                     attribute_values: Dict[str, str],
                     ) -> str:
        """
        is the template for query
        :param name_data_base:
        :param name_table:
        :param attribute_values:
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
