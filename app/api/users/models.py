from flask_restplus import Namespace, Resource, fields

from app.api.users import namespace

# Input models

user = namespace.model('User', {
    'email': fields.String(required=True, desciption='Email'),
    'password': fields.String(required=True, description='The user password'),
    'identification_code': fields.Integer(required=True, description='The user identification_code'),
    'name': fields.String(required=True, description='The user name'),
    'surname': fields.String(required=True, description='The user surname'),
})

user_info = namespace.model('UserInfo', {
    'user_id': fields.Integer(required=True, description='The user age'),
    'age': fields.Integer(required=True, description='The user age'),
    'organization': fields.String(required=True, description='The user organization'),
    'state': fields.String(required=True, desciption='Email'),
    'city': fields.String(required=True, description='The user password'),
    'country': fields.String(required=True, description='The user name'),
})

# Output models

user_response = namespace.inherit('UserResponse', user, {
    'id': fields.Integer(required=True, description='User id')
})


user_info_response = namespace.inherit('UserInfoResponse', user, {
    'id': fields.Integer(required=True, description='user info id')
})