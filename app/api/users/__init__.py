from flask_restplus import Namespace, Resource, fields

from app.api.core import init_module

MODULE_NAME = 'users'
# init namespace and collection
namespace, collection = init_module(MODULE_NAME)

from app.api.users.core.services import UserService
from app.api.users.core.builders import UserBuilder
from app.api.users.core.facades import UserFacade