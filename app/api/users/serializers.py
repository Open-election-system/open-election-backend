from flask_restplus import Namespace, Resource, fields

from . import namespace

user = namespace.model('User', {
    'id': fields.Integer(required=True, description='The user id'),
    'password_id': fields.Integer(required=True, description='The user password_id'),
    'identification_code': fields.Integer(required=True, description='The user identification_code'),
    'name': fields.String(required=True, description='The user name'),
    'surname': fields.String(required=True, description='The user surname'),
    'age': fields.Integer(required=True, description='The user age'),
    'organization': fields.String(required=True, description='The user organization'),
})

