
from app.api.core.facades import APIBaseFacade


class UserFacade:
    
    @classmethod
    def get_user_info(cls, user_id):
        from app.api import container
        
        user_info = container.user_info_service.get_by_params(user_id)
        return user_info

    @classmethod
    def create_user(cls, data):
        from app.api import container
        
        return container.user_builder.build(data)
