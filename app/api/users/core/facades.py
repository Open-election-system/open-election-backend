
from app.api.core.facades import APIBaseFacade


class UserFacade(APIBaseFacade):
    
    @classmethod
    def get_user_info(cls, user_id):
        from app.api import container
        user = []
        user_info = container.services.user_info().get_by_user_id(user_id)
        organizaion = container.services.organizations().get_by_organization_id(user_info['organization_id'])
        location = container.services.locations().get_by_location_id(user_info['location_id'])
        user.append({'user_info': user_info, 'organization': organizaion, 'location': location})
        return user[0]

    @classmethod
    def get_user(cls, user_id):
        from app.api import container
        user = container.services.users().get_user(user_id)
        return user
    
    @classmethod
    def get_all(cls):
        from app.api import container

        users = []
        user_list = container.services.users().get_all()[0]
        for user in user_list:
            user_info = container.services.user_info().get_by_user_id(user['id'])
            organization = container.services.organizations().get_by_organization_id(user_info['organization_id'])
            location = container.services.locations().get_by_location_id(user_info['location_id'])
            users.append({'user': user, 'user_info': user_info, 'organization': organization, 'location': location})
        return users
    
    @classmethod
    def create_user(cls, data):
        from app.api import container
        
        return container.builders.users.build(data)
