from flask_restplus import Api, Resource
from flask import Flask, Blueprint
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('root', description='Operations related to root')
from .views import namespace as root_namespace
from .users.views import namespace as user_namespace
from .elections.views import namespace as election_namespace