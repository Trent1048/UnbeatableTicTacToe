class Player:
    def __init__(self, symbol, board):
        self.board = board
        self.symbol = symbol
        
    def validLocation(self, location):
        if location <= 9 and location > 0 and self.board[2 - int((location - 1) / 3)][(location - 1) % 3][0] == " ":
            return True
        else: 
            return False

    def turn(self, location):
        self.board[2 - int((location - 1) / 3)][(location - 1) % 3][0] = self.symbol