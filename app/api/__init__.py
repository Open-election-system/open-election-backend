from flask_restplus import Api, Resource
from flask import Flask, Blueprint
from flask_restplus import Namespace, Resource, fields

from .users.views import namespace as user_namespace
from .elections.views import namespace as election_namespace
from .restrictions.views import namespace as restriction_namespace