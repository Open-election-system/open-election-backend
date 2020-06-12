
from flask_restplus import Namespace, Resource, fields

from app import db

def init_namespace(name, description=None):
    # Initialize namespace
    description = description if description is not None else 'Operations related to '+name
    return Namespace(name, description=description)

def init_db_collection(name):
    # Initialize db collection
    return db.collection(name)

def init_module(module_name):
    namespace = init_namespace(module_name)
    collection = init_db_collection(module_name)
    return namespace, collection