from flask_restplus import Namespace, Resource, fields

from app import db

# Initialize namespace
namespace = Namespace('elections', description='Operations related to elections')