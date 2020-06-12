
from app.api.core.services.entity import APIEntityServiceMixin
from app.api.core.builders import APIBaseBuilder
from app.api.core.facades import APIBaseFacade
from app.core.utils import setdefaultattr


class EntityContainer:

    def __init__(self, election=None, user=None, user_info=None, voting=None, restriction=None, option=None, organization=None, location=None):
        self.elections = election
        self.users = user
        self.votings = voting
        self.restrictions = restriction
        self.options = option
        self.organizations = organization
        self.locations = location
        self.user_info = user_info
    
    def setdefaultattr(self, name, value):
        return setdefaultattr(self, name, value)

class IoCServiceContainer(EntityContainer):

    def __init__(self, election: APIEntityServiceMixin, user: APIEntityServiceMixin,
                 user_info: APIEntityServiceMixin ,
                voting: APIEntityServiceMixin, restriction: APIEntityServiceMixin, option: APIEntityServiceMixin, 
                organization: APIEntityServiceMixin, location: APIEntityServiceMixin):
        super(IoCServiceContainer, self).__init__(
            election, user, 
            user_info,
             voting, restriction, option, organization, location)


class IoCBuiderContainer(EntityContainer):

    def __init__(self, election: APIBaseBuilder, user: APIBaseBuilder):
        super(IoCBuiderContainer, self).__init__(election, user)


class IoCFacadeContainer(EntityContainer):

    def __init__(self, election: APIBaseFacade, user: APIBaseFacade, option: APIEntityServiceMixin, votings:APIBaseFacade):
        super(IoCFacadeContainer, self).__init__(election, user, option=option, voting=votings)


class IoCContainer:

    def __init__(self, service_container: IoCServiceContainer, builder_container: IoCBuiderContainer, facade_container: APIBaseFacade):
        self.services = service_container
        self.builders = builder_container
        self.facades = facade_container
