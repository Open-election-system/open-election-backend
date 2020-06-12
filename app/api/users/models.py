from flask_restplus import Namespace, Resource, fields

from app.api.users import namespace

from app.api.organizations.models import organization
from app.api.locations.models import location

# Input models

user = namespace.model('User', {
    'email': fields.String(required=True, desciption='Email'),
    'password': fields.String(required=True, description='The user password'),
})

user_info = namespace.model('UserInfo', {
    'age': fields.Integer(required=True, description='The user age'),
    'identification_code': fields.Integer(required=True, description='The user identification_code'),
    'name': fields.String(required=True, description='The user name'),
    'surname': fields.String(required=True, description='The user surname'),
})

# user_full_info = namespace.model('UserFullInfo', {
#     'user': fields.Nested(user),
#     'user_info': fields.Nested(user_info),
#     # 'organization': fields.Nested(organization),
#     # 'location': fields.Nested(location)
# })

# Output models

user_response = namespace.inherit('UserResponse', user, {
    'id': fields.Integer(required=True, description='User id')
})


user_info_response = namespace.inherit('UserInfoResponse', user, {
    'id': fields.Integer(required=True, description='user info id')
})