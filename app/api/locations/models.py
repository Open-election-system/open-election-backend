from flask_restplus import Namespace, Resource, fields

from app.api.locations import namespace

location = namespace.model('Locations', {
    'city': fields.String(required=True, description='The user city'),
    'state': fields.String(required=True, description='The user state'),
    'country': fields.String(required=True, description='The user country')
})