from flask_restplus import Namespace, Resource, fields

from app.api.elections import namespace

election = namespace.model('Elections', {
    'id': fields.Integer(required=True, description='Election id'),
    'name': fields.String(required=True, description='Election name'),
    'description': fields.String(required=False, description='Election description'),
    'restrictions_id': fields.Integer(required=True, description='Election restrictions'),
})

