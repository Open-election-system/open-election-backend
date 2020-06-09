from flask_restplus import Namespace, Resource, fields

from app.api.users import namespace

# Input models

user = namespace.model('User', {
    'email': fields.String(required=True, desciption='Email'),
    'password': fields.String(required=True, description='The user password'),
    'identification_code': fields.Integer(required=True, description='The user identification_code'),
    'name': fields.String(required=True, description='The user name'),
    'surname': fields.String(required=True, description='The user surname'),
    'age': fields.Integer(required=True, description='The user age'),
    'organization': fields.String(required=True, description='The user organization'),
})

# Output models

user_response = namespace.inherit('UserResponse', user, {
    'id': fields.Integer(required=True, description='User id')
})