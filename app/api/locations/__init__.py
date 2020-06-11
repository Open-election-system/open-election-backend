from flask_restplus import Namespace, Resource, fields

from app.api.core import init_module

MODULE_NAME = 'locations'
# init namespace and collection
namespace, collection = init_module(MODULE_NAME)

from app.api.locations.core.services import LocationService