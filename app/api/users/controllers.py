from app.api.users import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.controllers.entity import APIEntityController


class UserController(APIEntityController):
    __users_collection = APIDatabaseController(collection)

    def get_all(self):
        return self.__users_collection.get_all()

    def get_one(self, id):
        return self.__users_collection.get_one(id)

    def create(self, data):
        return self.__users_collection.post(data)

    def update(self, id, data):
        return self.__users_collection.put(id, data)

    def delete(self, id):
        return self.__users_collection.delete(id)
