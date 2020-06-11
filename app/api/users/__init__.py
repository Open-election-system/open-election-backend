from flask_restplus import Namespace, Resource, fields

from app.api.core import init_module

MODULE_NAME = 'users'
USER_INFO = 'user_info'
# init namespace and collection
namespace, collection = init_module(MODULE_NAME)
user_info_namespace, user_info_collection = init_module(USER_INFO)

from app.api.users.core.services import UserService, UserInfoService
from app.api.users.core.builders import UserBuilder
from app.api.users.core.facades import UserFacade