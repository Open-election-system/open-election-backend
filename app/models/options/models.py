from flask_restplus import Namespace, Resource, fields

from app.api.options import namespace

option = namespace.model('Options', {
    'id': fields.Integer(required=True, description='Option id'),
    'name': fields.String(required=True, description='Option name'),
    'description': fields.String(required=False, description='Option description'),
    'elections_id': fields.Integer(required=True, description='Elections id'),
})

