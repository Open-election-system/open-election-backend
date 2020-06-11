
from app.api.core.builders import APIBaseBuilder


class UserBuilder(APIBaseBuilder):

    @classmethod
    def get_data(cls):
        data_user = data.get('user')
        data_user_info = data.get('user_info')
        

    @classmethod
    def build(cls, data):
        data_user, data_user_info = cls.get_data()

        user_info = cls.__build_user_info(data_user_info)
        user = cls.__build_user({**data_user, 'user_info_id': user_info.id})

    @classmethod
    def __build_user(cls, user):
        from app.api import container
        
        return container.user_service.create(user)

    @classmethod
    def __build_user_info(cls, user_info):
        from app.api import container
        
        return container.user_info_service.create(user_info)
