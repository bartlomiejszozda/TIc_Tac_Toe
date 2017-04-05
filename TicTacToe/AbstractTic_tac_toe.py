import abc
from abc import ABC

class AbstractTic_tac_toe(ABC):
    """ klasa abstrakcyjna, rozpoczynajaca gre, prowadzaca rozgrywke, wypisujaca wskazowki, przekazujaca ruch i konczaca gre"""

    @abc.abstractmethod
    def start_game(self):
        pass
        """rozpoczyna gre, ustawia wielkosc planszy i uruchamia game_service"""

    @abc.abstractmethod
    def game_service(self):
        pass
        """obsluguje gre,
        przekazuje ruch graczowi i komputerowi.
        Uruchamia rysowanie planszy
        oraz sprawdzanie czy ktos wygral"""

    @abc.abstractmethod
    def game_end(self):
        pass
        """krotki komunikat na zakonczenie rozgrywki"""