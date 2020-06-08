
from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix

def create_app(config_filename):
    # Initialize Flask app
    application = Flask(__name__)
    application.wsgi_app = ProxyFix(application.wsgi_app)
    application.config.from_object(Config)
    return application

def initialize_db():
    # Initialize DB
    from app.connectors.database import db
    return db

def create_api(application):
    # Add API
    blueprint = Blueprint('api', __name__, url_prefix='/api/1')
    api = Api(blueprint,
            title='Open election API',
            version='1.0',
            description='Open election API',
            )
    return api, blueprint

def add_namespaces_to_api(api):
    from app.api import user_namespace, election_namespace, restriction_namespace, option_namespace, vote_namespace
    from app.auth import auth_namespace
    # Add namespaces
    api.add_namespace(user_namespace)
    api.add_namespace(election_namespace)
    api.add_namespace(restriction_namespace)
    api.add_namespace(option_namespace)
    api.add_namespace(vote_namespace)
    api.add_namespace(auth_namespace)
    return api

def register_blueprint(application, blueprint):
    # Register blueprint
    application.register_blueprint(blueprint)
    return application

# Initialization
from config import Config
application = create_app(Config)
db = initialize_db()
api, blueprint = create_api(application)
api = add_namespaces_to_api(api)
application = register_blueprint(application, blueprint)
    