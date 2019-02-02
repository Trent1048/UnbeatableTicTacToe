class Bot:
    def __init__(self, symbol, board):
        self.board = board
        self.gameboard = self.board.board
        self.symbol = symbol
        self.symbols = ["X","O"]

    def turn(self):
        testRows = self.testRows()
        testCols = self.testCols()
        testDiag = self.testDiag()
        if testRows[0]:
            self.gameboard[testRows[1]][testRows[2]] = self.symbol
        elif testCols[0]:
            self.gameboard[testCols[2]][testCols[1]] = self.symbol
        elif testDiag[0]:
            self.gameboard[testDiag[1]][testDiag[2]] = self.symbol

    def testRows(self):
        for xo in self.symbols:
            for row in range(3):
                if self.gameboard[row].count(xo) == 2 and " " in self.gameboard[row]:
                    return [True, row, self.gameboard[row].index(" ")]
        return [False]

    def testCols(self):
        for xo in self.symbols:
            for row in range(3):
                column = []
                for col in range(3):
                    column.append(self.gameboard[col][row])
                if column.count(xo) == 2 and " " in column:
                    return [True, row, column.index(" ")]
        return [False]

    def testDiag(self):
        if self.gameboard[1][1] == " ":
            return [True, 1, 1]
        return [False]