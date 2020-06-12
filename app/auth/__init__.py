# from app import application
from flask_restplus import Api, Resource
from flask import Flask, Blueprint
from flask_restplus import Namespace, Resource, fields

# namespace = Namespace('auth', description='Operations related to root')
from app.auth.core import init_module

MODULE_NAME = 'auth'

namespace, collection = init_module(MODULE_NAME)

from .views import namespace as auth_namespace