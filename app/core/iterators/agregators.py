import collections.abc

from app.core.iterators.iterators import BaseIterator

class BaseAggregator(collections.abc.Iterable):

    "An iterable object."
    
    def __init__(self, data, max=None):
        self.data = data
        self.max = max if max is not None else len(data)
        
    @property
    def iterator(self):
        return OptionIterator
    
    def __iter__(self):
        return self.iterator(self)