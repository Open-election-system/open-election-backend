from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class BaseBuilder(ABC):
    
    @abstractmethod
    def get_data(self) -> None:
        pass
    
    @abstractmethod
    def build(self) -> None:
        pass
