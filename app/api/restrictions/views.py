from flask import request
from flask_restplus import Resource

from app.api.restrictions import namespace
from app.api.restrictions.models import restriction


@namespace.route('')
class RestrictionList(Resource):
    @namespace.doc('list restrictions')
    @namespace.marshal_list_with(restriction)
    def get(self):
        """
        Get all restrictions.
        """
        from app.api import container
        return container.services.restrictions().get_all()

    @namespace.doc('add restriction')
    @namespace.expect(restriction)
    def post(self):
        """
        Create a new restriction.
        """
        data = request.json
        from app.api import container
        return container.services.restrictions().create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The restriction identifier')
@namespace.response(404, 'restriction not found')
class Restriction(Resource):
    @namespace.doc('get_restriction')
    def get(self, id):
        """
        Get a restriction by id.
        """
        from app.api import container
        return container.services.restrictions().get_one(id)

    @namespace.doc('update_restriction')
    @namespace.expect(restriction)
    def put(self, id):
        """
        Update existing restriction.
        """
        data = request.json
        from app.api import container
        return container.services.restrictions().update(id, data)

    def delete(self, id):
        """
        Delete existing restriction.
        """
        from app.api import container
        return container.services.restrictions().delete(id)
