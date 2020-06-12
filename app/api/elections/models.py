from flask_restplus import Namespace, Resource, fields

from app.api.elections import namespace
from app.api.restrictions.models import nested_restriction, restriction_response
from app.api.options.models import nested_option, option_response

election = namespace.model('Elections', {
    'name': fields.String(required=True, description='Election name'),
    'description': fields.String(required=False, description='Election description'),
})

election_response = namespace.inherit('ElectionResponse', election, {
    'id': fields.Integer(required=True, description='Election id')
})


election_full_model = namespace.model('ElectionFull', {
    'election': fields.Nested(election),
    'restrictions': fields.Nested(nested_restriction),
    'options': fields.List(fields.Nested(nested_option)),
})

election_full_response_model = namespace.model('ElectionFullUserResponse', {
    'election': fields.Nested(election),
    'restrictions': fields.Nested(nested_restriction),
    'options': fields.List(fields.Nested(nested_option)),
})

election_user_response_model = namespace.model('ElectionFullResponse', {
    'election': fields.Nested(election),
    'restrictions': fields.Nested(restriction_response),
    'votes_number': fields.Integer(description='Total vote number'),
    'can_vote': fields.Boolean(description=' If user can vote or revote'),
})

