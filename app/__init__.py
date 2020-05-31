
from flask import Flask, Blueprint
from flask_restplus import Api, Resource
from werkzeug.middleware.proxy_fix import ProxyFix

from config import Config

application = Flask(__name__)
application.wsgi_app = ProxyFix(application.wsgi_app)
application.config.from_object(Config)

from app.api import root_namespace, user_namespace, election_namespace
from app.auth import auth_namespace

blueprint = Blueprint('api', __name__, url_prefix='/api/1')
api = Api(blueprint,
          title='Open election API',
          version='1.0',
          description='Open election API',
          ) 
api.add_namespace(root_namespace)
api.add_namespace(user_namespace)
api.add_namespace(election_namespace)
api.add_namespace(auth_namespace)
application.register_blueprint(blueprint)
