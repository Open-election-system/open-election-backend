from flask_restplus import Api, Resource
from flask import Flask, Blueprint
from flask_restplus import Namespace, Resource, fields

from .users.views import namespace as user_namespace, user_info_namespace
from .elections.views import namespace as election_namespace
from .restrictions.views import namespace as restriction_namespace
from .options.views import namespace as option_namespace
from .votes.views import namespace as vote_namespace


def create_container(container, service_container, buider_container, facade_container):
    """
        Creating an IoC container.
        Different access:
        - to services: container.services.resrictions().get_by_params(user_info)
        - other: container.facades.users.get_user_info(user_id)
    """
    from app.api.elections import ElectionService, ElectionBuilder, ElectionFacade
    from app.api.users import UserService, UserBuilder, UserFacade, UserInfoService
    from app.api.votes import VotingService
    from app.api.restrictions import RestrictionService
    from app.api.options import OptionService, OptionFacade
    from app.api.organizations import OrganizationService
    from app.api.locations import LocationService

    service_container = service_container(ElectionService, UserService, UserInfoService, VotingService, RestrictionService, OptionService, OrganizationService, LocationService)
    service_container.setdefaultattr(UserInfoService.get_table_name(), UserInfoService)
    builder_container = buider_container(ElectionBuilder, UserBuilder)
    facade_container = facade_container(ElectionFacade, UserFacade, OptionFacade)
    container = container(service_container, builder_container, facade_container)
    return container

from app.api.core.containers import IoCServiceContainer, IoCBuiderContainer, IoCContainer, IoCFacadeContainer
container = create_container(IoCContainer, IoCServiceContainer, IoCBuiderContainer, IoCFacadeContainer)