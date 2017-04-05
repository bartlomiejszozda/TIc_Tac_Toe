from draw_board import draw_board
board=draw_board()

from random import randint

class computer_player:
    def do_turn(self,N):
        while(True):
            x=randint(0,N-1)
            y=randint(0,N-1)
            if (x < N and y < N and (x, y) not in board.list_of_circle_points and (x, y) not in board.list_of_cross_points):
                board.list_of_circle_points.append((x, y))
                break

