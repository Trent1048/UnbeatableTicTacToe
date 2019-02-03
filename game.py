from player import Player
from board import Board
from bot import Bot

notLost = True
notQuit = True
noList = ["no", "No", "n", "N"]

print("Welcome to Unbeatable Tic Tac Toe, you will not win \n")
while notQuit:
    board = Board()
    gameboard = board.board
    player1 = Player("X", gameboard)
    bot = Bot("O", board)
    while notLost: #main game loop
        board.display()
        while True:
            playerInput = int(input("Choose a spot on the numPad to put an X: "))
            if player1.validLocation(playerInput):
                break
        print()
        board.turns += 1
        player1.turn(playerInput)
        bot.turn()
        notLost = not board.testWin()
    board.display()
    if input("Want to try again? ") in noList:
        notQuit = False
    else:
        notLost = True
print("Bye now ")