from flask_restplus import Namespace, Resource, fields

from app.api.core import init_module

MODULE_NAME = 'elections'

namespace, collection = init_module(MODULE_NAME)

from app.api.elections.core.services import ElectionService
from app.api.elections.core.builders import ElectionBuilder
from app.api.elections.core.facades import ElectionFacade