from flask_restplus import Namespace, Resource, fields

from app.api.organizations import namespace

# Input models

organization = namespace.model('Organizations', {
    'organization': fields.String(required=True, description='The organization name')
})

# Output models

organization_response = namespace.inherit('OrganizationResponse', organization, {
    'id': fields.Integer(required=True, description='Organization id')
})
