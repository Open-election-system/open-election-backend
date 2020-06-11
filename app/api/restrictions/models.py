from flask_restplus import Namespace, Resource, fields

from app.api.restrictions import namespace

restriction = namespace.model('Restriction', {
    'election_id': fields.Integer(required=True, description='Election restrictions'),
    'age_from': fields.Integer(required=False, description='Restriction age from'),
    'age_to': fields.Integer(required=False, description='Restriction age to'),
    'votes_number': fields.Integer(required=False, description='Restriction of votes to use'),
    'reatract': fields.Boolean(required=False, description='Restriction is reatract'),
    'start': fields.Integer(required=False, description='Restriction start date (timestamp)'),
    'end': fields.Integer(required=False, description='Restriction end date (timestamp)'),
    'organization': fields.String(required=False, description='Restriction organization'),
})

restriction_response = namespace.inherit('RestrictionResponse', restriction, {
    'id': fields.Integer(required=True, description='Restriction id')
})

nested_restriction = namespace.model('RestrictionNested', {
    'age_from': fields.Integer(required=False, description='Restriction age from'),
    'age_to': fields.Integer(required=False, description='Restriction age to'),
    'votes_number': fields.Integer(required=False, description='Restriction of votes to use'),
    'reatract': fields.Boolean(required=False, description='Restriction is reatract'),
    'start': fields.Integer(required=False, description='Restriction start date (timestamp)'),
    'end': fields.Integer(required=False, description='Restriction end date (timestamp)'),
    'organization': fields.String(required=False, description='Restriction organization'),
})