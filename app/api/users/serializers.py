from flask_restplus import Namespace, Resource, fields

from . import namespace

user = namespace.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'name': fields.String(required=True, description='The user name'),
})

