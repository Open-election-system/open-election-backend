from flask import request
from flask_restplus import Resource

from app.api.locations import namespace
from app.api.locations.models import location
from app.api.locations.controllers import LocationController

location_controller = LocationController()


@namespace.route('')
class LocationList(Resource):
    @namespace.doc('list_locations')
    @namespace.marshal_list_with(location)
    def get(self):
        """
        Get all locations.
        """
        return location_controller.get_all()

    @namespace.doc('add_location')
    @namespace.expect(location)
    def post(self):
        """
        Create a new location.
        """
        data = request.json
        return location_controller.create(data)

    @namespace.doc('add_batch_location')
    def post(self):
        """
        Create batch locations.
        """
        data = request.json
        return location_controller.batch_create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The location identifier')
@namespace.response(404, 'Location not found')
class Location(Resource):
    @namespace.doc('get_location')
    def get(self, id):
        """
        Get a location by id.
        """
        # vote_col = db.collection('vote')
        # voting_col = db.collection('votings')
        # votes = location_controller.get_many_to_many(vote_col, voting_col, locationId=id, votingId=None)
        return location_controller.get_one(id)

    @namespace.doc('update_location')
    @namespace.expect(location)
    def update(self, id):
        """
        Update existing location.
        """
        data = request.json
        return location_controller.update(id, data)

    def delete(self, id):
        """
        Delete existing location.
        """
        return location_controller.delete(id)
