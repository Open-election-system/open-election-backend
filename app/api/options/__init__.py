from flask_restplus import Namespace, Resource, fields

from app.api.core import init_module

MODULE_NAME = 'options'

namespace, collection = init_module(MODULE_NAME)

from app.api.options.core.services import OptionService
from app.api.options.core.facades import OptionFacade