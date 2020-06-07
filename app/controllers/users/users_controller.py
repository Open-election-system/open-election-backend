from app.api.users import namespace, collection
from app.models.db_controller.db_controller import DatabaseController
from app.controllers.entity_controller.entity_controller import EntityController


class UsersController(EntityController):
    __users_collection = DatabaseController(collection)

    def get_all(self):
        return self.__users_collection.get_all()

    def get_one(self, id):
        return self.__users_collection.get_one(id)

    def create(self, data):
        return self.__users_collection.post(id, data)

    def update(self, id, data):
        return self.__users_collection.put(id, data)

    def delete(self, id):
        return self.__users_collection.delete(id)
