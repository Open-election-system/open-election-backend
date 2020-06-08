from flask import request
from flask_restplus import Resource

from app.api.restrictions import namespace
from app.models.restrictions.models import restriction
from app.controllers.restrictions.restrictions_controller import RestrictionsController

restriction_controller = RestrictionsController()


@namespace.route('')
class RestrictionList(Resource):
    @namespace.doc('list restrictions')
    @namespace.marshal_list_with(restriction)
    def get(self):
        """
        Get all restrictions.
        """
        return restriction_controller.get_all()

    @namespace.doc('add restriction')
    def post(self):
        """
        Create a new restriction.
        """
        data = request.json
        print(request, request.json, data)
        return restriction_controller.create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The restriction identifier')
@namespace.response(404, 'restriction not found')
class Restriction(Resource):
    @namespace.doc('get_restriction')
    def get(self, id):
        """
        Get a restriction by id.
        """
        return restriction_controller.get_one(id)

    @namespace.doc('update_restriction')
    @namespace.expect(restriction)
    def update(self, id):
        """
        Update existing restriction.
        """
        data = request.json
        return restriction_controller.update(id, data)

    def delete(self, id):
        """
        Delete existing restriction.
        """
        return restriction_controller.delete(id)
