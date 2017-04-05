from draw_board import draw_board

board=draw_board()
class human_player:
    def do_turn(self,N):
        while(True):
            print("Aby wybrac miejsce postawienia znaku, wpisz (x y) bez nawiasow\n, gdzie x-numer wiersza, y-numer kolumny numerowane od 0.")
            point = input()
            #print(point[0],point[2])
            x=int (point[0])
            y=int (point[2])
            if (x>=N or y>=N):
                print("wybrales zbyt duze liczby(x,y musza byc mniejsze od rozmiaru)")
            elif((x,y) in board.list_of_circle_points or (x,y) in board.list_of_cross_points):
                print("to miejsce jest juz zajete!")
            else:
                board.list_of_cross_points.append((x, y))
                break
            #print(boar# d.list_of_cross_points)