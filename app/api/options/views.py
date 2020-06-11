from flask import request
from flask_restplus import Resource

from app.api.options import namespace
from app.api.options.models import option


@namespace.route('')
class OptionList(Resource):
    @namespace.doc('list_options')
    @namespace.marshal_list_with(option)
    def get(self):
        """
        Get all options.
        """
        from app.api import container
        return container.services.options().get_all()

    @namespace.doc('add_option')
    @namespace.expect(option)
    def post(self):
        """
        Create a new option.
        """
        data = request.json
        from app.api import container
        return container.services.options().create(data)

    @namespace.doc('add_batch_option')
    def post(self):
        """
        Create batch options.
        """
        from app.api import container
        return container.services.options().batch_create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The option identifier')
@namespace.response(404, 'Option not found')
class Option(Resource):
    @namespace.doc('get_option')
    def get(self, id):
        """
        Get a option by id.
        """
        from app.api import container
        return container.services.options().get_one(id)

    @namespace.doc('update_option')
    @namespace.expect(option)
    def put(self, id):
        """
        Update existing option.
        """
        data = request.json
        from app.api import container
        return container.services.options().update(id, data)

    def delete(self, id):
        """
        Delete existing option.
        """
        from app.api import container
        return container.services.options().delete(id)
