from player import Player
from board import Board

board = Board()
gameboard = board.board
player1 = Player("X", gameboard)
bot = Player("O", gameboard)

notLost = True
notQuit = True
noList = ["no", "No", "n", "N"]

print("Welcome to Unbeatable Tic Tac Toe, you will surely loose (or tie) ")
while notQuit:
    while notLost:
        board.display()
        while True:
            playerInput = int(input("Choose a spot on the numPad to put an X: "))
            if player1.validLocation(playerInput):
                break
        player1.turn(playerInput)
        board.display()
        #bot.turn(0)
        notLost = board.testWin()
    if input("Want to try again? ") in noList:
        notQuit = False
    else:
        notLost = True
        board.newBoard()
print("Bye now ")