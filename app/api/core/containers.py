
from app.api.core.services.entity import APIEntityServiceMixin
from app.api.core.builders import APIBaseBuilder
from app.api.core.facades import APIBaseFacade
from app.core.utils import setdefaultattr


class EntityContainer:

    def __init__(self, election=None, user=None, voting=None, restriction=None, option=None):
        self.elections = election
        self.users = user
        self.votings = voting
        self.restrictions = restriction
        self.options = option
    
    def setdefaultattr(self, name, value):
        return setdefaultattr(self, name, value)

class IoCServiceContainer(EntityContainer):

    def __init__(self, election: APIEntityServiceMixin, user: APIEntityServiceMixin, voting: APIEntityServiceMixin, restriction: APIEntityServiceMixin, option: APIEntityServiceMixin):
        super(IoCServiceContainer, self).__init__(
            election, user, voting, restriction, option)


class IoCBuiderContainer(EntityContainer):

    def __init__(self, election: APIBaseBuilder, user: APIBaseBuilder):
        super(IoCBuiderContainer, self).__init__(election, user)


class IoCFacadeContainer(EntityContainer):

    def __init__(self, election: APIBaseBuilder, user: APIBaseBuilder, option: APIEntityServiceMixin):
        super(IoCFacadeContainer, self).__init__(election, user, option=option)


class IoCContainer:

    def __init__(self, service_container: IoCServiceContainer, builder_container: IoCBuiderContainer, facade_container: APIBaseFacade):
        self.services = service_container
        self.builders = builder_container
        self.facades = facade_container
