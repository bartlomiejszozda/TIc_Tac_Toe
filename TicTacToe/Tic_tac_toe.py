
from draw_board import draw_board
#from user_interface import user_interface
from human_player import human_player
from computer_player import computer_player
from game_state import game_state

class Tic_tac_toe:

    size=3
    def __init__(self):
        #self.__interface=user_interface()
        self.__board=draw_board()
        self.__human=human_player()
        self.__computer=computer_player()
        self.__state=game_state()
        pass
    def start_game(self):
        print("Witamy w grze kolko i krzyzyk. Rozmiar planszy n x n, wybierz n:")
        size = input()
        self.size = int(size)
        self.__board.draw_board(self.size)
        self.game_service()

    def end_game(self):
        print("dzieki za gre, mordo!")
    def game_service(self):
        while (True):
            self.__human.do_turn(self.size)
            if (self.__state.if_game_over()):
                self.__board.draw_board(self.size)
                print("zwyciezyl czlowiek")
                self.end_game()
                break
            self.__computer.do_turn(self.size)
            self.__board.draw_board(self.size)
            if (self.__state.if_game_over()):
                print("zwyciezyl komputer")
                self.end_game()
                break