class Board:
    def __init__(self):
        self.board = [[" "," "," "],
                     [" "," "," "],
                     [" "," "," "]]   
        self.edges = [[0,1],[1,0],[1,2],[2,1]]#self.board[this stuff]
        self.corners = [[0,0],[0,2],[2,0],[2,2]]
        
    def display(self):
        for row in range(3):
            for column in range(3):
                print(self.board[row][column], end = " ")
                if column < 2:
                    print("|", end = " ")
            if row < 2:
                print("\n---------")
        print("\n")

    def testWin(self):
        for rowNum in range(3): #testing rows
            row = self.board[rowNum]
            if row[0] == row[1] == row[2] != " ":
                return True
        for column in range(3): #testing columns
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":#testing diagonals
            return True
        for row in self.board:
            for column in row:
                if column == " ":
                    return False
        return True           