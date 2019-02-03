class Bot:
    def __init__(self, symbol, board):
        self.board = board
        self.gameboard = self.board.board
        self.symbol = symbol
        self.symbols = ["O","X"]

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
        elif self.gameboard[1][1] == " ":
            self.gameboard[1][1] = self.symbol
        else:
            self.prioritize()

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
        for corner in range(4):
            if self.gameboard[self.board.corners[corner][0]][self.board.corners[corner][1]] == self.gameboard[1][1] != " ":
                opCorner = self.board.oppositeCorner(corner)
                if self.gameboard[opCorner[0]][opCorner[1]] == " ":
                    return [True, opCorner[0], opCorner[1]]
        return[False]

    def prioritize(self):
        corners = []
        for corner in range(4):
            corners.append(self.gameboard[self.board.corners[corner][0]][self.board.corners[corner][1]])
        if self.board.turns != 2 or not "X" in corners:
            for corner in range(4):
                if self.gameboard[self.board.corners[corner][0]][self.board.corners[corner][1]] == " ":
                    self.gameboard[self.board.corners[corner][0]][self.board.corners[corner][1]] = self.symbol
                    break
        elif self.board.turns == 2:
            for edge in range(4):
                opEdge = self.board.oppositeSide(edge)
                if self.gameboard[self.board.edges[edge][0]][self.board.edges[edge][1]] == " " == self.gameboard[opEdge[0]][opEdge[1]]:
                    self.gameboard[self.board.edges[edge][0]][self.board.edges[edge][1]] = self.symbol
                    break