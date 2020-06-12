from flask_restplus import Namespace, Resource, fields

from app.api.core import init_module

MODULE_NAME = 'organizations'
# init namespace and collection
namespace, collection = init_module(MODULE_NAME)

from app.api.organizations.core.services import OrganizationService