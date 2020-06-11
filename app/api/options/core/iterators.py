import jmespath
from copy import deepcopy

from app.core.iterators.agregators import BaseAggregator
from app.core.iterators.iterators import BaseIterator
from app.api.options.serializers import Serializer, OptionAgregationObject, OptionReportAgregationObject


class OptionAgregator(BaseAggregator):

    "An iterable object."
    
    def __init__(self, election_id):
        from app.api import container

        self.election_id = election_id
        self.report = deepcopy(OptionReportAgregationObject(election_id))
        self.data = container.services.options().get_by_election_id(election_id)
        # print(self.data)
        super(OptionAgregator, self).__init__(self.data)
        
    @property
    def iterator(self):
        return OptionIterator
        
    def __iter__(self):
        return self.iterator(self)
    
    
class OptionIterator(BaseIterator):
    """
        An iterator.
    """
    
    def iteration(self):
        self.item = self.container.data[self.order]
        # print(self.item)
        self.count_votes()
        
        
    def count_votes(self):
        from app.api import container
        
        self.option_id = self.item['id']
        self.votes = deepcopy(container.services.votings().get_by_election_and_option_id(self.container.election_id, self.option_id))
        # check if option is alreade in report or not
        search_option = jmespath.search(f'[?option_id==`{self.option_id}`]', self.container.report.options)
        # print(search_option)
        option_votes = search_option['vote_number'] if len(search_option)>0 else 0
        # print(self.option_id, self.votes, option_votes)
        option_votes += len(self.votes)
        option_agregator = OptionAgregationObject(self.option_id, self.item['name'], option_votes)
        option_agregator_serializer = Serializer.serialize(option_agregator)
        # print(option_agregator_serializer)
        self.container.report.options.append(option_agregator_serializer)