from flask_restplus import Api, Resource
from flask import Flask, Blueprint
from flask_restplus import Namespace, Resource, fields

from .users.views import namespace as user_namespace
from .elections.views import namespace as election_namespace
from .restrictions.views import namespace as restriction_namespace
from .options.views import namespace as option_namespace
from .votes.views import namespace as vote_namespace


def create_container(container, service_container, buider_container, facade_container=None):
    """
        Creating an IoC container.
    """
    from app.api.elections import ElectionService, ElectionBuilder, ElectionFacade
    from app.api.users import UserService, UserBuilder, UserFacade
    from app.api.votes import VotingService
    from app.api.restrictions import RestrictionService
    from app.api.options import OptionService

    service_container = service_container(ElectionService, UserService, VotingService, RestrictionService, OptionService)
    builder_container = buider_container(ElectionBuilder, UserBuilder)
    container = container(service_container, builder_container)
    return container

from app.api.core.containers import IoCServiceContainer, IoCBuiderContainer, IoCContainer
container = create_container(IoCContainer, IoCServiceContainer, IoCBuiderContainer)