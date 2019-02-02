from player import Player
from board import Board

board = Board()
gameboard = board.board
player1 = Player(gameboard,"X")
bot = Player(gameboard,"O")
notLost = True

print("Welcome to Unbeatable Tic Tac Toe, you will surely loose (or tie) ")
while(notLost):
    board.display()
    while True:
        playerInput = input("Choose a spot on the numPad to put an X :")
        if player1.validLocation(playerInput):
            break
    board.display()
    bot.turn(0)
    notLost = board.testWin()