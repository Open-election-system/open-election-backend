container = {}


class UsersBuilder:
    @staticmethod
    def build(data):
        data_user = data.get('user')
        data_user_info = data.get('user_info')

        user_info = UsersBuilder.__build_user_info(data_user_info)
        user = UsersBuilder.__build_user({**data_user, 'user_info_id': user_info.id})

    @staticmethod
    def __build_user(user):
        return container.user_service.create(user)

    @staticmethod
    def __build_user_info(user_info):
        return container.user_info_service.create(user_info)
