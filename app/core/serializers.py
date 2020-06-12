

class Serializer:
    
    @classmethod
    def serialize(cls, object_to_serialize):
        return object_to_serialize.__dict__