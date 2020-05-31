
from flask import Flask, Blueprint
from flask_restplus import Api, Resource
from werkzeug.middleware.proxy_fix import ProxyFix
from firebase_admin import credentials, firestore, initialize_app

from config import Config

# Initialize Flask app
application = Flask(__name__)
application.wsgi_app = ProxyFix(application.wsgi_app)
application.config.from_object(Config)

# Initialize DB
from app.database import db
 
# Add API
from app.api import user_namespace, election_namespace
from app.auth import auth_namespace

blueprint = Blueprint('api', __name__, url_prefix='/api/1')
api = Api(blueprint,
          title='Open election API',
          version='1.0',
          description='Open election API',
          )

# Add namespaces
api.add_namespace(user_namespace)
api.add_namespace(election_namespace)
api.add_namespace(auth_namespace)
application.register_blueprint(blueprint)
