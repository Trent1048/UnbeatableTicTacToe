class Bot:
    def __init__(self, symbol, board):
        self.board = board
        self.gameboard = self.board.board
        self.symbol = symbol
        self.symbols = ["O","X"]

    def turn(self):#first tests if there is 2 of the same symbol in a line so it can either block or win
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
            self.prioritize()#if nothing above was triggered, it will go through this function that is set up to block forks and place O's strategically 

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
        xCornerCount = 0
        xEdgeCount = 0
        for cornEdge in range(4):
            if self.gameboard[self.board.corners[cornEdge][0]][self.board.corners[cornEdge][1]] == "X":
                xCornerCount += 1
            if self.gameboard[self.board.edges[cornEdge][0]][self.board.edges[cornEdge][1]] == "X":
                xEdgeCount += 1   
        if self.board.turns == 2 and (xCornerCount == 2 or (xCornerCount == 1 and xEdgeCount == 1)):#blocks the opposite diagonals strat and the edge and corner on opposite side strat
            for edge in range(4):
                opEdge = self.board.oppositeSide(edge)
                if self.gameboard[self.board.edges[edge][0]][self.board.edges[edge][1]] == " " == self.gameboard[opEdge[0]][opEdge[1]]:
                    self.gameboard[self.board.edges[edge][0]][self.board.edges[edge][1]] = self.symbol
                    break
        else:
            for edge in range(4):#blocks the empty corner between 2 edges strat
                for otherEdge in range(4):
                    cornerBetweenEdges = self.board.cornerBetweenEdges(edge,otherEdge)
                    if cornerBetweenEdges != None and edge != otherEdge and self.gameboard[self.board.corners[cornerBetweenEdges][0]][self.board.corners[cornerBetweenEdges][1]] == " " and self.gameboard[self.board.edges[otherEdge][0]][self.board.edges[otherEdge][1]] == self.gameboard[self.board.edges[edge][0]][self.board.edges[edge][1]] == "X":
                        self.gameboard[self.board.corners[cornerBetweenEdges][0]][self.board.corners[cornerBetweenEdges][1]] = self.symbol
                        break 
                if not self.board.correctNumOfTurns():
                    break
            if self.board.correctNumOfTurns():#if nothing else in prioritize worked, these 2 lower if statements will ensure that O gets a turn 
                for corner in range(4):
                    if self.gameboard[self.board.corners[corner][0]][self.board.corners[corner][1]] == " ":
                        self.gameboard[self.board.corners[corner][0]][self.board.corners[corner][1]] = self.symbol
                        break
            if self.board.correctNumOfTurns():
                for edge in range(4):
                    if self.gameboard[self.board.edges[edge][0]][self.board.edges[edge][1]] == " ":
                        self.gameboard[self.board.edges[edge][0]][self.board.edges[edge][1]] = self.symbol
                        break