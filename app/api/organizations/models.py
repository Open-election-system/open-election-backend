from flask_restplus import Namespace, Resource, fields

from app.api.organizations import namespace

organization = namespace.model('Organizations', {
    'organization_name': fields.String(required=True, description='The organization name'),
})