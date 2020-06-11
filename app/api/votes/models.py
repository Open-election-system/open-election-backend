from flask_restplus import Namespace, Resource, fields

from app.api.votes import namespace

vote = namespace.model('Voting', {
    'election_id': fields.Integer(required=True, description='The vote election_id'),
    'option_id': fields.Integer(required=True, description='The vote option_id'),
    'user_id': fields.Integer(required=True, description='The vote user_id'),
})

vote_response = namespace.inherit('VotingResponse', vote, {
    'id': fields.Integer(required=True, description='Restriction id')
})