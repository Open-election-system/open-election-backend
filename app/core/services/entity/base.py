import abc

class BaseEntityService:

    __metaclass__ = abc.ABCMeta

    @property
    def __collection(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_one(self, id):
        pass

    @abc.abstractmethod
    def create(self, data):
        pass

    @abc.abstractmethod
    def update(self, id, data):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass