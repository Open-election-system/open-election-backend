from flask import request
from flask_restplus import Resource

from app.api.organizations import namespace, organization_info_namespace

from app.api.organizations.models import organization, organization_response
from app.api import container

@namespace.route('')
class OrganizationList(Resource):
    @namespace.doc('list_organizations')
    @namespace.marshal_list_with(organization)
    def get(self):
        """
        Get all organizations.
        """
        return container.services.organizations().get_all()

    @namespace.doc('add_organization')
    @namespace.expect(organization)
    @namespace.response(200, 'Success', organization_response)
    def post(self):
        """
        Create a new organization.
        """
        data = request.json
        return container.services.organizations().create(data)


@namespace.route('/<id>')
@namespace.doc(params={'election_id': {'description': 'The election id'}})
@namespace.param('id', 'The organization identifier')
@namespace.response(404, 'organization not found')
class Organization(Resource):
    
    @namespace.doc('get_organization')
    def get(self, id):
        """
        Get a organization by id.
        """
        return container.services.organizations().get_one(id)

    @namespace.doc('update_organization')
    @namespace.expect(organization)
    def put(self, id):
        """
        Update existing organization.
        """
        data = request.json
        return container.services.organizations().update(id, data)

    def delete(self, id):
        """
        Delete existing organization.
        """
        from app.api import container
        return container.services.organizations().delete(id)
