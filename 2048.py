# Game 2048
# 2048 is a board game with nxn dimensions which fills with the number 2
# and 4. The goal of the user is to add identical numbers til 2048.
import random

LEN = 4
RM = [] #Stores random moves (r,c)

# Design: 
    # Initialize the board
    #   - start with a board with two 2s randomly placed.
def printBoard(board):
    for i in range(LEN):
        col = []
        for j in range(LEN):
            col.append("_")
        board.append(col)
        print("\t\t",' '.join(board[i]),end = "\n")
        print()

    # Get the random row and col to populate the board
def randMove():
    randRow = random.randint(0,3)
    randCol = random.randint(0,3)
    # Check for douplicates
    while ([randRow, randCol] in RM):
        print("Redo b/c random douplicate found: ", randRow, randCol)
        randRow = random.randint(0,3)
        randCol = random.randint(0,3)
        return randRow, randCol
    print("The random row and col:", randRow, randCol)
    return randRow, randCol

# After every move and start of the game
#   - fill random cell with a 2 or a 4
def populate(board, start):
   
   #If its the start of the game populate two 2s
    if (start):
        RM.append(randMove())
        board[RM[0][0]][RM[0][1]] = '2'

    #Insert new moves in the begining of the list for easy indexing
    RM.insert(0,randMove())
    board[RM[0][0]][RM[0][1]] = '2'

    printBoard(board)
    print (RM)
 
    # Moves
    #   - up, down, right and left
    #   - all elements in the board will move to the furthest direction

    # After every move 
    #   - fill random cell with a 2 or a 4

    # WIN
    # - all elements must add upto 2048

    # GAME OVER
    # - no empty spaces left to fill with a 2 or a 4
def main():
    board = []
    start = True #Is it the start of the game? 
    print("\t     Welcome to 2048\n",
            "Begin by joining the numbers and get to 2048.")
    printBoard(board)
    populate(board, start)
    start = False 
main()