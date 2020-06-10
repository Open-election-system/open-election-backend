container = {}


class UsersFacade:
    @staticmethod
    def get_user_info(user_id):
        user_info = container.users_service.get_by_params(user_id)
        return user_info

    @staticmethod
    def create_user(data):
        return container.user_builder.build(data)
