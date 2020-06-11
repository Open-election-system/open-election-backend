
from app.api.core.facades import APIBaseFacade


class UserFacade:
    
    @staticmethod
    def get_user_info(user_id):
        from app.api import container
        
        user_info = container.user_info_service.get_by_params(user_id)
        return user_info

    @staticmethod
    def create_user(data):
        from app.api import container
        
        return container.user_builder.build(data)
