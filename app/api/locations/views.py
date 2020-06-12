from flask import request
from flask_restplus import Resource

from app.api.locations import namespace, location_info_namespace

from app.api.locations.models import location, location_response
from app.api import container

@namespace.route('')
class LocationList(Resource):
    @namespace.doc('list_locations')
    @namespace.marshal_list_with(location)
    def get(self):
        """
        Get all locations.
        """
        return container.services.locations().get_all()

    @namespace.doc('add_location')
    @namespace.expect(location)
    @namespace.response(200, 'Success', location_response)
    def post(self):
        """
        Create a new location.
        """
        data = request.json
        return container.services.locations().create(data)


@namespace.route('/<id>')
@namespace.doc(params={'election_id': {'description': 'The election id'}})
@namespace.param('id', 'The location identifier')
@namespace.response(404, 'location not found')
class Location(Resource):
    
    @namespace.doc('get_location')
    def get(self, id):
        """
        Get a location by id.
        """
        return container.services.locations().get_one(id)

    @namespace.doc('update_location')
    @namespace.expect(location)
    def put(self, id):
        """
        Update existing location.
        """
        data = request.json
        return container.services.locations().update(id, data)

    def delete(self, id):
        """
        Delete existing location.
        """
        from app.api import container
        return container.services.locations().delete(id)
