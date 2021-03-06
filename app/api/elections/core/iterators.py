import jmespath
from copy import deepcopy

from app.core.iterators.agregators import BaseAggregator
from app.core.iterators.iterators import BaseIterator
from app.core.serializers import Serializer
from app.api.elections.serializers import ElectionReportAgregationObject

class ElectionAgregator(BaseAggregator):

    "An iterable object."
    
    def __init__(self):
        from app.api import container

        self.report = deepcopy(ElectionReportAgregationObject())
        self.data = container.services.elections().get_all()
        super(ElectionAgregator, self).__init__(self.data)
        
    @property
    def iterator(self):
        return ElectionIterator
        
    def __iter__(self):
        return self.iterator(self)
    
    
class ElectionIterator(BaseIterator):
    """
        An iterator.
    """
    
    def iteration(self):
        self.item = self.container.data[self.order]
        self.count_votes()
        
        
    def count_votes(self):
        from app.api import container
        
        self.election_id = self.item['id']
        election = container.facades.options.get_option_stats_by_election_id(self.election_id)
        self.container.report.elections.append(election)