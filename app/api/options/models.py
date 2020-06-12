from flask_restplus import Namespace, Resource, fields

from app.api.options import namespace

option = namespace.model('Options', {
    'name': fields.String(required=True, description='Option name'),
    'description': fields.String(required=False, description='Option description'),
    'election_id': fields.Integer(required=True, description='Elections id'),
})

option_response = namespace.inherit('OptionsResponse', option, {
    'id': fields.Integer(required=True, description='Options id')
})

nested_option = namespace.model('Options', {
    'name': fields.String(required=True, description='Option name'),
    'description': fields.String(required=False, description='Option description'),
})
