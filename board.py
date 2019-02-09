class Board:
    def __init__(self, display = False):
        if not display:
            self.board = [[" "," "," "],
                         [" "," "," "],
                         [" "," "," "]]   
            self.edges = [[0,1],[1,0],[1,2],[2,1]]#self.board[this stuff]
            self.corners = [[0,0],[0,2],[2,0],[2,2]]
            self.turns = 0
        else:
            self.board = [["7","8","9"],
                         ["4","5","6"],
                         ["1","2","3"]] 

    def display(self):#prints out the board in a nice looking way
        for row in range(3):
            for column in range(3):
                print(self.board[row][column], end = " ")
                if column < 2:
                    print("|", end = " ")
            if row < 2:
                print("\n---------")
        print("\n")

    def testWin(self):
        for rowNum in range(3):#testing rows
            row = self.board[rowNum]
            if row[0] == row[1] == row[2] != " ":
                return True
        for column in range(3):#testing columns
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":#testing diagonals
            return True
        for row in self.board:
            for column in row:
                if column == " ":
                    return False
        return True           

    def oppositeCorner(self, corner):#returns a len 2 list refering to location of corner/edge in relationship to the board
        return self.corners[3 - corner]

    def oppositeSide(self, side):
        return self.edges[3 - side]

    def cornerBetweenEdges(self, edge1, edge2):#if there are 2 edges that are next to each other with the same symbol, it will return the corner that is between them. this is used to stop the corner strat
        edgePairs = [[0,1],[0,2],[1,3],[2,3]]
        for edgePair in range(4):
            if (edge1 == edgePairs[edgePair][0] and edge2 == edgePairs[edgePair][1]) or (edge1 == edgePairs[edgePair][1] and edge2 == edgePairs[edgePair][0]):
                return edgePair

    def toSingleArray(self):#returns the whole board as a single array to be used for counting the number of X's and O's in it (to ensure a correct number of turns)
        singleBoard = []
        for row in range(3):
            for column in range(3):
                singleBoard.append(self.board[row][column])
        return singleBoard

    def correctNumOfTurns(self):# returns true if you can add another O without it being unfair
        numOfOs = 0
        singleBoard = self.toSingleArray()
        for o in range(9):
            if singleBoard[o] == "O":
                numOfOs += 1
        if numOfOs == self.turns - 1:
            return True
        return False
