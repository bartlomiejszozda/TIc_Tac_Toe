import abc
from abc import ABC

class AbstractGameState(ABC):
    """klasa abstrakcyjna wykonujaca ruch komputera i obslugujaca ruch czlowieka"""

    @abc.abstractmethod
    def do_turn(self,N):
        pass
        """sprawdza, czy dane miejsce nie jest zajete i wykonuje nowy ruch"""