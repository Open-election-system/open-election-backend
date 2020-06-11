import collections.abc

class BaseIterator(collections.abc.Iterator):
    """
        An iterator.
    """
    def __init__(self, container):
        self.container = container
        self.order = 0

    def __next__(self):
        self.order += 1
        if self.order >= self.container.max:  
            raise StopIteration
        self.iteration()
        return self.item  

    def iteration(self):
        self.item = None
        
    def __iter__(self):
        return self
