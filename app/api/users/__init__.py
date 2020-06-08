from flask_restplus import Namespace, Resource, fields

from app.api.core import init_module

MODULE_NAME = 'users'

namespace, collection = init_module(MODULE_NAME)