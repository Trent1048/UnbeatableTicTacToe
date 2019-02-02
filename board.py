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

    def testWin(self):
        for rowNum in range(3):
            row = self.board[rowNum]
            if row[0] == row[1] == row[2]:
                return True
        