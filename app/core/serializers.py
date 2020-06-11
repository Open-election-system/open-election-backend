

class Serializer:
    
    @classmethod
    def serialize(cls, object_to_serialize):
        print(object_to_serialize.__dict__)
        return object_to_serialize.__dict__