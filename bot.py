class Bot:
    def __init__(self, symbol, board):
        self.board = board
        self.symbol = symbol
        self.symbols = ["X","O"]

    def turn(self):
        self.testCols()

    def testRows(self):
        for xo in self.symbols:
            for row in self.board.board:
                if row.count(xo) == 2:
                    return [True, row[" "]]
        return [False]

    def testCols(self):
        return True

    def testDiag(self):
        return True