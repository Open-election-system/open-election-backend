from flask_restplus import Namespace, Resource, fields

from app import db

# Initialize namespace
namespace = Namespace('users', description='Operations related to users')

# Initialize db collection
collection = db.collection('users')