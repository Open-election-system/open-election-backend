
from app.api.core.builders import APIBaseBuilder


class UserBuilder(APIBaseBuilder):

    @classmethod
    def get_data(cls, data):
        data_user = data.get('user') if 'user' in data else None
        data_user_info = data.get('user_info') if 'user_info' in data else None
        data_organization = data.get('organization') if 'organization' in data else None
        data_location = data.get('location') if 'location' in data else None
        return data_user, data_user_info, data_organization, data_location
        

    @classmethod
    def build(cls, data):
        data_user, data_user_info, data_organization, data_location = cls.get_data(data)
        user = cls.__build_user(data_user)
        organization = cls.__build_organization(data_organization)
        location = cls.__build_location(data_location)
        user_info = cls.__build_user_info({**data_user_info, 'user_id': user, 'organization_id': organization, 'location_id': location})

        return 'Success'

    @classmethod
    def __build_user(cls, user):
        from app.api import container
        from app.core.exceptions import EmailInUseException
        find_user = container.services.users().get_by_params({'email': user['email']})
        if find_user is not None: raise EmailInUseException()
        return container.services.users().create(user)

    @classmethod
    def __build_user_info(cls, user_info):
        from app.api import container
        
        return container.services.user_info().create(user_info)

    @classmethod
    def __build_organization(cls, organization):
        from app.api import container
        find_organization = container.services.organizations().get_by_params(organization)
        return container.services.organizations().create(organization) if find_organization is None else find_organization['id']
    
    @classmethod
    def __build_location(cls, location):
        from app.api import container
        find_location = container.services.locations().get_by_params(location)
        return container.services.locations().create(location) if find_location is None else find_location['id']
