from flask import request
from flask_restplus import Resource

from app.api.elections import namespace
from app.api.elections.models import election
from app.api.elections.services import ElectionService

election_service = ElectionService()


@namespace.route('')
class ElectionList(Resource):
    @namespace.doc('list elections')
    @namespace.marshal_list_with(election)
    def get(self):
        """
        Get all elections.
        """
        return election_service.get_all()

    @namespace.doc('add election')
    @namespace.expect(election)
    def post(self):
        """
        Create a new election.
        """
        data = request.json
        return election_service.create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The election identifier')
@namespace.response(404, 'election not found')
class Election(Resource):
    @namespace.doc('get_election')
    def get(self, id):
        """
        Get a election by id.
        """
        return election_service.get_one(id)

    @namespace.doc('update_election')
    @namespace.expect(election)
    def update(self, id):
        """
        Update existing election.
        """
        data = request.json
        return election_service.update(id, data)

    def delete(self, id):
        """
        Delete existing election.
        """
        return election_service.delete(id)
