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
    def get_many_to_many(self, id):
        return self.__collection.get_many_to_many(id)

    @abc.abstractmethod
    def create(self, data):
        pass
    
    @abc.abstractmethod
    def batch_create(self, data_list):
        return self.__collection.batch_create(data_list)
    
    @abc.abstractmethod
    def update(self, id, data):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def get_by_equal_params(self, id, filter_dict):
        return self.__collection.get_by_equal_params(filter_dict)

    @abc.abstractmethod
    def get_by_any_params(self, filter_list):
        return self.__collection.get_by_any_params(filter_list)