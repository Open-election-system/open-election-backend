
from app.core.iterators.agregators import BaseAggregator
from app.core.iterators.iterators import BaseIterator

class OptionAgregator(BaseAggregator):

    "An iterable object."
    
    def __init__(self):
        from app.api import container
        self.data = container.services.options().get_all()
        super(OptionAgregator, self).__init__(self.data)
    
    @property
    def iterator(self):
        return OptionIterator
        
    def __iter__(self):
        from app.api import container
        self.option = self.iterator(self)
        if self.option is dict:
            self.votes = container.services.votings().get_by_option_id(self.option['id'])
            print(self.option, self.votes)
        return self.iterator(self)
    
class OptionIterator(BaseIterator):
    """
        An iterator.
    """
    
    def iteration(self):
        self.item = self.container.data[self.order]
        # print(self.item)
        # self.votes = container.services.votes().get_votes_by_items(self.item['id'])