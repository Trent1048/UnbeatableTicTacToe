class Board:
    def __init__(self):
        self.board = [[[" "],[" "],[" "]],
                     [[" "],[" "],[" "]],
                     [[" "],[" "],[" "]]]   

    def display(self):
        for row in range(3):
            for column in range(3):
                print(self.board[row][column][0], end = " ")
                if column < 2:
                    print("|", end = " ")
            if row < 2:
                print("\n---------")
        print("\n")

    def testWin(self):
        win = False
        for rowNum in range(3): #testing rows
            row = self.board[rowNum]
            if row[0] == row[1] == row[2] != " ":
                win = True
        for column in range(3): #testing columns
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != " ":
                win = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":#testing diagonals
            win = True
        return win

    def newBoard(self):
        self.__init__()