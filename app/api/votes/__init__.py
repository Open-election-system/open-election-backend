from flask_restplus import Namespace, Resource, fields

from app.api.core import init_module

MODULE_NAME = 'votes'

namespace, collection = init_module(MODULE_NAME)

from app.api.votes.core.services import VotingService
from app.api.votes.core.facades import VotingFacade