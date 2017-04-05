
class draw_board:
    list_of_circle_points=[]
    list_of_cross_points=[]

    def __init__(self):
        pass
    def draw_board(self,N):
        for i in range (N):
            print("(", end='')
            for j in range(N):
                print("|",end='')
                if((i,j) in self.list_of_circle_points):
                    print("O",end='')
                elif ((i,j) in self.list_of_cross_points):
                    print("X",end='')
                else:
                    print("_",end='')
                print("|",end='')
            print(")")

