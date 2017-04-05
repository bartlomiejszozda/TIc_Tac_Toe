from draw_board import draw_board
from Validator import Validator
from Exceptions import Not_A_Possible_Input_Or_Not_In_Array_Size, Not_An_Integer , Place_Is_Cover

board=draw_board()
class human_player:
    def __init__(self):
        pass
    def do_turn(self,N):
        while(True):
            print("Aby wybrac miejsce postawienia znaku, wpisz (x y) bez nawiasow\n, gdzie x-numer wiersza, y-numer kolumny numerowane od 0.")
            point = input()
            x=int (point[0])
            y=int (point[2])
            if (self.value_in_size(x,y, N)):
                board.list_of_cross_points.append((x, y))
                break

    def value_in_size(self,x,y , N):
        if not Validator.a_possibe_input_or_in_array_size(self, x, N):
            print("wybrales zbyt duze liczby(x,y musza byc mniejsze od rozmiaru)")
            raise Not_A_Possible_Input_Or_Not_In_Array_Size(x)
        if not Validator.a_possibe_input_or_in_array_size(self, y, N):
            raise Not_A_Possible_Input_Or_Not_In_Array_Size(y)

        elif (not Validator.place_is_free(self, x, y, board.list_of_circle_points, board.list_of_cross_points)):
            raise Place_Is_Cover((x, y))
        return True
