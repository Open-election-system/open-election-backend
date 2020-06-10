from flask import request
from flask_restplus import Resource

from app.api.organizations import namespace
from app.api.organizations.models import organization
from app.api.organizations.controllers import OrganizationController

organization_controller = OrganizationController()


@namespace.route('')
class OrganizationList(Resource):
    @namespace.doc('list_organizations')
    @namespace.marshal_list_with(organization)
    def get(self):
        """
        Get all organizations.
        """
        return organization_controller.get_all()

    @namespace.doc('add_organization')
    @namespace.expect(organization)
    def post(self):
        """
        Create a new organization.
        """
        data = request.json
        return organization_controller.create(data)

    @namespace.doc('add_batch_organization')
    def post(self):
        """
        Create batch organizations.
        """
        data = request.json
        return organization_controller.batch_create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The organization identifier')
@namespace.response(404, 'organization not found')
class Organization(Resource):
    @namespace.doc('get_organization')
    def get(self, id):
        """
        Get a organization by id.
        """
        # vote_col = db.collection('vote')
        # voting_col = db.collection('votings')
        # votes = organization_controller.get_many_to_many(vote_col, voting_col, organizationId=id, votingId=None)
        return organization_controller.get_one(id)

    @namespace.doc('update_organization')
    @namespace.expect(organization)
    def update(self, id):
        """
        Update existing organization.
        """
        data = request.json
        return organization_controller.update(id, data)

    def delete(self, id):
        """
        Delete existing organization.
        """
        return organization_controller.delete(id)
