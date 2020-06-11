from app.api.core.facades import APIBaseFacade
from app.api.options.core.iterators import OptionAgregator, OptionIterator
from app.core.serializers import Serializer

class OptionFacade(APIBaseFacade):
    
    @classmethod
    def get_option_stats_by_election_id(cls, election_id):
        option_agregator = OptionAgregator(election_id)
        for n in option_agregator: pass # don't remove this line
        serialized_report = Serializer.serialize(option_agregator.report)
        return serialized_report
    
    # @classmethod
    # def get_option_stats_by_election_id(cls, election_id):
    #     option_agregator = OptionAgregator(election_id)
    #     for n in option_agregator: pass # don't remove this line
    #     serialized_report = Serializer.serialize(option_agregator.report)
    #     return serialized_report