from app.api.core.facades import APIBaseFacade
from app.api.options.core.iterators import OptionAgregator, OptionIterator

class OptionFacade(APIBaseFacade):
    
    @classmethod
    def iterate_through_options(cls):
        numbers = OptionAgregator()
        for n in numbers:
            print(n)
        