from flask_restplus import Namespace, Resource, fields

from app.api.locations import namespace

# Input models

location = namespace.model('Locations', {
    'district': fields.String(required=True, description='The user district'),
    'city': fields.String(required=True, description='The user city'),
    'region': fields.String(required=True, description='The user region')
})

# Output models

location_response = namespace.inherit('LocationResponse', location, {
    'id': fields.Integer(required=True, description='Location id')
})
