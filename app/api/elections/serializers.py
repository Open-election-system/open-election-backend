from flask_restplus import Namespace, Resource, fields

from . import namespace

restrictions = namespace.model('Restrictions', {
    'ageFrom': fields.Integer(required=False),
    'ageTo': fields.Integer(required=False),
    'reatract': fields.Boolean(required=False),
    'votesAmount': fields.Integer(required=False),
    'startDate': fields.DateTime(required=False),
    'endDate': fields.DateTime(required=False),
})

options = namespace.model('Options', {
    'id': fields.Integer(required=False),
    'name': fields.String(required=True),
})

votes = namespace.model('Votes', {
    'userId': fields.Integer(required=False),
    'optionId': fields.String(required=True),
    'lastModified': fields.DateTime(required=False),
})

election = namespace.model('Election', {
    'id': fields.Integer(required=True, description='The election identifier'),
    'name': fields.String(required=True, description='The election name'),
    'description': fields.String(required=True, description='The election description'),
    'restrictions':  fields.List(fields.Nested(restrictions), description='pets', required=True),
    'options': fields.List(fields.Nested(options), required=True, description='The election options'),
    'votes': fields.List(fields.Nested(votes), required=False, description='The election votes'),
})

