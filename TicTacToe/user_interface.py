#from Tic_tac_toe import Tic_tac_toe

class user_interface:
    def __init__(self):
        pass

    def write_start_interface(self,ttt):#ttt czyli objekt Tic_tac_toe
        print("Witamy w grze kolko i krzyzyk. Rozmiar planszy n x n, wybierz n:")
        size= input()
        ttt.size=int(size)


    def write_actual_interface(self):
        pass

