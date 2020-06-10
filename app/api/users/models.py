from flask_restplus import Namespace, Resource, fields

from app.api.users import namespace

# Input models

user = namespace.model('User', {
    'email': fields.String(required=True, desciption='Email'),
    'password': fields.String(required=True, description='The user password'),
})

user_info = namespace.model('UserInfo', {
    'identification_code': fields.Integer(required=True, description='The user identification_code'),
    'name': fields.String(required=True, description='The user name'),
    'surname': fields.String(required=True, description='The user surname'),
    'middle_name': fields.String(required=True, description='The user middle name'),
    'age': fields.Integer(required=True, description='The user age'),
    'organization': fields.String(required=True, description='The user organization'),
    'city': fields.String(required=True, description='The user city'),
    'state': fields.String(required=True, description='The user state'),
    'country': fields.String(required=True, description='The user country'),
})

# Output models

user_response = namespace.inherit('UserResponse', user, {
    'id': fields.Integer(required=True, description='User id')
})