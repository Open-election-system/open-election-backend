from flask_restplus import Namespace, Resource, fields

from app import application
from app.auth import namespace

# Input models

auth = namespace.model('AuthModel', {
    'email': fields.String(required=True, desciption='Email'),
    'password': fields.String(required=True, description='The user password'),
})

# Output models

login_response = namespace.model('AuthResponse', {
    'id': fields.String(required=True, desciption='User id'),
})

error = namespace.model('Error', {
    'message': fields.String(required=True, desciption='error message'),
    'code': fields.String(required=True, desciption='error code'),
})
