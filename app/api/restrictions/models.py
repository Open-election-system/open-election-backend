from flask_restplus import Namespace, Resource, fields

from app.api.restrictions import namespace

restriction = namespace.model('Restriction', {
    'id': fields.Integer(required=True, description='Restriction id'),
    'age_from': fields.Integer(required=False, description='Restriction age from'),
    'age_to': fields.Integer(required=False, description='Restriction age to'),
    'votes_number': fields.Integer(required=False, description='Restriction of votes to use'),
    'reatract': fields.Boolean(required=False, description='Restriction is reatract'),
    'start': fields.DateTime(required=False, description='Restriction start date'),
    'end': fields.DateTime(required=False, description='Restriction end date'),
    'organization': fields.String(required=False, description='Restriction organization'),
})

