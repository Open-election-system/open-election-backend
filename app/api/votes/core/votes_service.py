from app.api.votes import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.controllers.entity import APIEntityController


class VotesService(APIEntityController):
    __TABLE_NAME = 'votes'
    __votes_collection = APIDatabaseController(collection)

    def get_all(self):
        return self.__votes_collection.get_all()

    def get_one(self, id):
        return self.__votes_collection.get_one(id)

    def create(self, data):
        return self.__votes_collection.post(data)

    def update(self, id, data):
        return self.__votes_collection.put(id, data)

    def delete(self, id):
        return self.__votes_collection.delete(id)

    def count_by_option(self, option_id):
        pass
        # return self.__votes_collection.delete(id)

    def count_user_election_votes(self, election_id, user_id):
        pass
        # return self.__votes_collection.delete(id)
