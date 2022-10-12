"""
This file contains functions used in the orm.
"""
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from importlib import import_module
from connections.orm_base_object import OrmBaseObject


def list_attributes_values(object_save: object) -> Dict[str, str]:
    """
        generate two list of attributes and values
    :param object_save:
        object
    :return:
        list of the attributes and values of the object
    """
    dict_variables = vars(object_save)
    values_object = {}
    for name_variable, value in dict_variables.items():
        name_of_variable = name_variable.split('__')[-1]
        name_of_variable = name_of_variable.lstrip("_")
        if isinstance(value, str):
            value = "\'" + value + "\'"
        if isinstance(value, datetime):
            value = value.strftime('%Y-%m-%d %H-%M-%S')
            value = "\'" + value + "\'"
        value = str(value)
        values_object[name_of_variable] = value
    return values_object


def match_attributes_values(attributes: Dict[str, str],
                            condition: str) -> str:
    """
    match the element with th list attributes and list values.
    :param attributes:
        names attributes
    :param condition:
        condition between the parameters
    :return:
        the condition for the consult
    """
    attributes_values = []
    condition = " " + condition + " "
    for key, value in attributes.items():
        attributes_values.append(key + "=" + value)
    values_response = condition.join(attributes_values)
    return values_response


def match_attribute_values_list(attribute: str,
                                condition: str,
                                values: List[int]) -> str:
    """
    match the element with the attribute and list values.
    :param attribute:
        name attribute
    :param condition:
        the condition between values
    :param values:
        value of the attributes
    :return:
        the condition for the consult
    """
    attributes_values = []
    condition = " " + condition + " "
    for value in values:
        attributes_values.append(attribute + "!=" + str(value))
    values_response = condition.join(attributes_values)
    return values_response


def values_replace(attributes: Dict[str, str]) -> str:
    """
        structure and match the attributes with
        the values.
    :param attributes:
        list attributes
    :return:
        a string with the matching of the attributes and values
    """
    attributes_values = []
    for attribute, value in attributes.items():
        if attribute != "id":
            attributes_values.append(attribute+"=" + value)
    values_response = ",".join(attributes_values)
    return values_response


def get_list_attributes(dictionary: Dict[str, str]) -> Tuple[str, str]:
    """
        get a list of the keys of dictionary
    :param dictionary:
        is the dictionary
    :return:
        a list of keys
    """
    list_attributes = []
    list_values_attributes = []
    for key, value in dictionary.items():
        list_attributes.append(key)
        list_values_attributes.append(value)
    attributes = ",".join(list_attributes)
    values_attributes = ",".join(list_values_attributes)
    return attributes, values_attributes


def create_objects(dir_source_code: str,
                   name_file: Optional[str],
                   name_object: str,
                   response_consult: List[Tuple[str]]) \
        -> List[OrmBaseObject]:
    """
    with the name of table find the name of class and instance the objects
    :param dir_source_code:
        name of table
    :param name_file:
        name of table
    :param name_object:
        name of table
    :param response_consult:
        list of the tuples on the data base
    :return:
        list of object
    """
    list_object = []
    name_file = str(name_file)
    module = import_module(dir_source_code + "." + name_file.lower())
    class_of_table = getattr(module, name_object)
    for tuple_table in response_consult:
        new_object = class_of_table()
        new_object.load_attributes(tuple_table)
        list_object.append(new_object)
    return list_object


def search_id(attributes: Dict[str, str]) -> str:
    """
        get the id with its object value
    :param attributes:
        list attributes of the object
    :return:
        the id with the value
    """
    id_object = 'id='+attributes['id']
    return id_object


def get_name_table(new_object: OrmBaseObject) -> Optional[str]:
    """
    obtain the name of class of the object
    :param new_object:
        object
    :return:
        name of class
    """
    if new_object.name_table() is None:
        type_object = str(type(new_object))
        name_class = type_object.split('\'')[1]
        name_table = name_class.split('.')[-1]
        name_table = name_table.upper()
        return name_table
    return new_object.name_table()


def convert_dict_to_str(dict_variables: Dict[str, object]) -> Dict[str, str]:
    """
        convert the values of the object in str
    :param dict_variables:
        dict with values of the object
    :return:
        dict with the values converted in str
    """
    values_object = {}
    for name_variable, value in dict_variables.items():
        if isinstance(value, str):
            value = "\'" + value + "\'"
        value = str(value)
        values_object[name_variable] = value
    return values_object


def get_parameters_file(dir_file: str, db_name: str) -> List[Any]:
    """
        this function return a list of parameters
        of the configuration file json
    :param dir_file
        direction of the file
    :param db_name:
        name of the database
    :return:
        list of the parameters for the connection database
    """
    list_parameters = []
    with open(dir_file + "configuration.json") as file:
        data = json.load(file)
        for parameter in data[db_name].items():
            list_parameters.append(parameter[1])
    return list_parameters
