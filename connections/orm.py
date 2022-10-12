"""
This file contains an orm.
"""
from typing import List, Dict


from connections.connection import ConnectionBase
from connections.orm_base_object import OrmBaseObject
from helpers.functions_orm import create_objects, \
    get_name_table, \
    list_attributes_values, \
    convert_dict_to_str, \
    get_list_attributes
from querys.delete_query import QueryDelete
from querys.insert_query import QueryInsert
from querys.select_all_query import QuerySelectAll
from querys.select_all_query_with_where import QuerySelectAllWhitWhere
from querys.select_query import QuerySelect
from querys.update_query_with_where import QueryUpdateWithWhere
from querys.delete_query_with_where import QueryDeleteWithWhere


class Orm:
    """
    Is the class of the orm
    """

    def __init__(self, connection: ConnectionBase, db_name: str,
                 dir_source_code: str = 'class_to_try') -> None:
        """
        :param connection:
            is the manager to the database
        """
        self.__connection = connection
        self.__operations = \
            {'select': QuerySelect(),
             'select*': QuerySelectAll(),
             'select*where': QuerySelectAllWhitWhere(),
             'insert': QueryInsert(),
             'delete': QueryDelete(),
             'delete where': QueryDeleteWithWhere()
             }
        self.__operation_update = QueryUpdateWithWhere()
        self.__dir_source_code = dir_source_code
        self.__db_name = db_name

    def search_objects(self, new_object: OrmBaseObject,
                       list_conditions: Dict[str, object],
                       ) -> List[OrmBaseObject]:
        """
            execute the sentences in the data base
        :param new_object:
            necessary for get the name of the class and name of the table
        :param list_conditions:
            list the attribute for search the tuples in the data base
        :return:
            list of the objects
        """
        name_table = get_name_table(new_object)
        name_object = new_object.__class__.__name__
        operation = self.__operations['select']
        attributes_values = convert_dict_to_str(list_conditions)
        query = operation.create_query(self.__db_name,
                                       name_table,
                                       attributes_values)
        # list of attributes of table
        list_attributes = list_attributes_values(new_object)
        del list_attributes["name_table"]
        attributes, values = get_list_attributes(list_attributes)
        del values
        query = query.format(attributes)
        response_query = self.__connection.send_query(query)
        list_object = create_objects(self.__dir_source_code,
                                     name_table,
                                     name_object,
                                     response_query)
        return list_object

    def save_object(self, object_to_save: OrmBaseObject) -> int:
        """
        save the attributes of the object in the database
        :param object_to_save:
            object
        :return:
            the id autoincrement of the tuple in the table
        """
        name_table = get_name_table(object_to_save)
        operation = self.__operations['insert']
        attributes_values = list_attributes_values(object_to_save)
        del attributes_values['name_table']
        del attributes_values['id']
        query = operation.create_query(self.__db_name,
                                       name_table,
                                       attributes_values)
        id_tuple = self.__connection.send_update(query)
        return id_tuple

    def update(self, modified_object: OrmBaseObject) -> int:
        """
            update a tuple of the data base from its id
        :param modified_object:
            object
        :return:
            id of last insert
        """
        name_table = get_name_table(modified_object)
        attributes_values = list_attributes_values(modified_object)
        del attributes_values['name_table']
        consult = self.__operation_update.create_query(self.__db_name,
                                                       name_table,
                                                       attributes_values)
        id_tuple = self.__connection.send_update(consult)
        return id_tuple

    def update_with_conditions(self, modified_object: OrmBaseObject,
                               list_conditions: Dict[str, object]) -> int:
        """
            update a tuple of the data base from its id
        :param modified_object:
            object
        :param list_conditions
            list the attribute for search the tuples in the data base
        :return:
            id of last insert
        """
        name_table = get_name_table(modified_object)
        attributes_values = list_attributes_values(modified_object)
        del attributes_values['name_table']
        conditional_values = convert_dict_to_str(list_conditions)
        consult = self.__operation_update.\
            create_query_where(name_table,
                               attributes_values,
                               conditional_values)
        id_tuple = self.__connection.send_update(consult)
        return id_tuple

    def object_delete(self, object_delete: OrmBaseObject) -> int:
        """
            delete a tuple with the id of the object
        :param object_delete:
            object
        :return:
            id of last insert
        """
        operation = self.__operations['delete']
        name_table = get_name_table(object_delete)
        attributes_values = list_attributes_values(object_delete)
        # del attributes_values['name_table']
        consult = operation.create_query(self.__db_name,
                                         name_table,
                                         attributes_values)
        id_tuple = self.__connection.send_update(consult)
        return id_tuple

    def delete_with_where(self, object_delete: OrmBaseObject,
                          list_conditions: Dict[str, object]) -> int:
        """
            delete a tuple with the id of the object
        :param object_delete:
            object
        :param list_conditions
            list the attribute for search the tuples in the data base
        :return:
            id of last insert
        """
        operation = self.__operations['delete where']
        name_table = get_name_table(object_delete)
        conditional_values = convert_dict_to_str(list_conditions)
        consult = operation.create_query(self.__db_name,
                                         name_table,
                                         conditional_values)
        id_tuple = self.__connection.send_update(consult)
        return id_tuple

    def set_conditional_where_select(self, conditional: str) -> None:
        """
            set the conditional between conditionals
        :param conditional:
            this can be "and" "or"
        :return:
            None
        """
        select = self.__operations['select']
        if isinstance(select, QuerySelect):
            select.set_conditional_where(conditional)

    def get_objects_from_the_table(
            self, orm_object: OrmBaseObject) -> List[OrmBaseObject]:
        """This method according to the entered parameter
        returns a list of objects."""
        name_table = get_name_table(orm_object)
        name_object = orm_object.__class__.__name__
        operation = self.__operations['select*']
        query = operation.create_query(self.__db_name, name_table, {"": ""})
        response_query = self.__connection.send_query(query)
        list_object = create_objects(
            self.__dir_source_code, name_table, name_object, response_query)
        return list_object

    def get_objects_from_the_table_with_where(
            self, orm_object: OrmBaseObject,
            list_conditions: Dict[str, object]) -> List[OrmBaseObject]:
        """This method according to the entered parameter
        returns a list of objects."""
        name_table = get_name_table(orm_object)
        name_object = orm_object.__class__.__name__
        operation = self.__operations['select*where']
        conditional_values = convert_dict_to_str(list_conditions)
        query = operation.create_query(self.__db_name, name_table,
                                       conditional_values)
        response_query = self.__connection.send_query(query)
        list_object = create_objects(
            self.__dir_source_code, name_table, name_object, response_query)
        return list_object
