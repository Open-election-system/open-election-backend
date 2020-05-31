from flask_restplus import Namespace, Resource, fields

from . import namespace

election = namespace.model('Election', {
    'id': fields.String(required=True, description='The election identifier'),
    'name': fields.String(required=True, description='The election name'),
    'description': fields.String(required=True, description='The election description'),
    'description': fields.String(required=True, description='The election description'),


})

