from flask import request
from flask_restplus import Resource

from app.api.elections import namespace
from app.api.elections.models import election
from app.api.elections.services import ElectionService

election_service = ElectionService()
container = {}


@namespace.route('')
class ElectionList(Resource):
    @namespace.doc('list elections')
    @namespace.marshal_list_with(election)
    def get(self):
        """
        Get all elections.
        """
        # user_id = request.headers['user-id']
        # return container.elections_facade.get_elections(user_id)
        return election_controller.get_all()

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
    def get(self, election_id):
        """
        Get a election by id.
        """

        # user_id = request.headers['user-id']
        # return container.elections_facade.get_election(election_id, user_id)
        return election_controller.get_one(election_id)

    @namespace.doc('update_election')
    @namespace.expect(election)
    def update(self, election_id):
        """
        Update existing election.
        """
        data = request.json
        # return container.elections_facade.create_election(data)
        return election_controller.update(election_id, data)


    def delete(self, election_id):
        """
        Delete existing election.
        """

        return election_controller.delete(election_id)


@namespace.route('/stats/<id>')
@namespace.param('id', 'The election identifier')
class ElectionStats(Resource):
    @namespace.doc('get_election')
    def get(self, election_id):
        """
        Get a election by id.
        """
        # user_id = request.headers['user-id']
        # return container.elections_facade.get_election(election_id)
