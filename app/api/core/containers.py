
from app.api.core.services.entity import APIEntityServiceMixin
from app.api.core.builders import APIBaseBuilder


class EntityContainer:

    def __init__(self, election=None, user=None, voting=None, restriction=None, option=None):
        self.elections = election
        self.users = user
        self.votings = voting
        self.restrictions = restriction
        self.options = option


class IoCServiceContainer(EntityContainer):

    def __init__(self, election: APIEntityServiceMixin, user: APIEntityServiceMixin, voting: APIEntityServiceMixin, restriction: APIEntityServiceMixin, option: APIEntityServiceMixin):
        super(IoCServiceContainer, self).__init__(
            election, user, voting, restriction, option)


class IoCBuiderContainer(EntityContainer):

    def __init__(self, election: APIBaseBuilder, user: APIBaseBuilder):
        super(IoCBuiderContainer, self).__init__(election, user)


class IoCContainer:

    def __init__(self, service_container: IoCServiceContainer, builder_container: IoCBuiderContainer, facade_container=None):
        self.services = service_container
        self.builders = builder_container
