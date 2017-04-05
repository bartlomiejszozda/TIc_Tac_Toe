from Tic_tac_toe import Tic_tac_toe
from human_player import human_player
import unittest
from Exceptions import Not_A_Possible_Input_Or_Not_In_Array_Size, Not_An_Integer , Place_Is_Cover
human = human_player()

class TestTic_tac_toe(unittest.TestCase):

    def test_x_not_in_size_intput_return_exception(self):
        N=Tic_tac_toe.size
        print(N)
        x=N+1
        y=0
        self.assertRaises(Not_A_Possible_Input_Or_Not_In_Array_Size , human.value_in_size, x,y,N)
