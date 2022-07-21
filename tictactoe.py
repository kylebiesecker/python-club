wincon = False
gameBoard = [[0,0,0],[0,0,0],[0,0,0]]
player = True
while not wincon:
    print('   1  2  3 ')
    count = 0
    for count, row in enumerate(gameBoard):  #enumerate returns (int, value)
        print(count+1,row)

    print(f"Player {'1' if player else '2'}, enter your move by entering row number, followed by enter key, then column number:")
    selectedRow = int(input("Row:"))
    selectedColumn = int(input("Column:"))
    gameBoard[selectedRow-1][selectedColumn-1] = f'{"x" if player else "o"}'
    player = not player
    wincon = checkWincon(gameBoard)

def checkWincon(gameState):
    for count in enumerate(gameState):
        if gameState[count][0] == gameState[count][1] & gameState[count][1] == gameState[count][2]:
            return True
        else:
            return False
