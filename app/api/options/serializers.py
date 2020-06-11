
from app.core.serializers import Serializer

# Factory pattern

class OptionReportAgregationObject:
    
    def __init__(self, election_id, options=[]):
        self.election_id = election_id
        self.options = options 
        
class OptionAgregationObject:
    
    def __init__(self, option_id, vote_number):
        self.option_id = option_id
        self.vote_number = vote_number 