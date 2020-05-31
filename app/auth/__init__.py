# from app import application
from flask_restplus import Api, Resource
from flask import Flask, Blueprint
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('auth', description='Operations related to root')
from .views import namespace as auth_namespace