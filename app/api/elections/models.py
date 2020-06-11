from flask_restplus import Namespace, Resource, fields

from app.api.elections import namespace
from app.api.restrictions.models import nested_restriction, restriction_response
<<<<<<< HEAD
from app.api.options.models import nested_option
=======
from app.api.options.models import nested_option, option_response
>>>>>>> 6252f97... changed a response model of the election view.

election = namespace.model('Elections', {
    'name': fields.String(required=True, description='Election name'),
    'description': fields.String(required=False, description='Election description'),
})

election_response = namespace.inherit('ElectionResponse', election, {
    'id': fields.Integer(required=True, description='Election id')
})

<<<<<<< HEAD
election_full_model = namespace.model('ElectionFull', {
=======

election_full_response_model = namespace.model('ElectionFull', {
    'election': fields.Nested(election_response),
    'restrictions': fields.Nested(restriction_response),
    'options': fields.List(fields.Nested(option_response)),
})

election_user_response_model = namespace.model('ElectionFullResponse', {
>>>>>>> 6252f97... changed a response model of the election view.
    'election': fields.Nested(election),
    'restrictions': fields.Nested(nested_restriction),
    'options': fields.List(fields.Nested(nested_option)),
})

election_full_response_model = namespace.model('ElectionFullResponse', {
    'election': fields.Nested(election),
    'restrictions': fields.Nested(restriction_response),
    'votes_number': fields.Integer(description='Total vote number'),
    'can_vote': fields.Boolean(description=' If user can vote or revote'),
})

