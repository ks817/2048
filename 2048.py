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
    return [randRow, randCol]

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
    
def userMove(board):
    validMoves = ['i','I','K','k','J','j','L','l']
    print("Make your move: \n\ti = up \n\tk = down \n\tj = left \n\tl = right \n\tq = quit")
    userInput = input("")
    while userInput not in validMoves and userInput != 'q' and userInput != 'Q':
        userInput = input("Please enter a valid move (i,k,j,l,q)\n")

    if(userInput == 'i' or userInput == 'I'):
        moveUp(board)

    elif(userInput == 'k' or userInput == 'K'):
       moveDown(board)

    elif(userInput == 'j' or userInput == 'J'):
        moveLeft(board)

    elif(userInput == 'l' or userInput == 'L'):
        moveRight(board)
    # Moves
    #   - up, down, right and left
    #   - all elements in the board will move to the furthest direction
def moveUp(board):
    print("Move up was called")

def moveDown(board):
    print("Move down was called")

def moveLeft(board):
    print("Move Left was called")

def moveRight(board):
    print("Move right was called")
    for i in range(LEN):
        #Goal : [_ 2 _ _] to move 2 to the right
        for j in range(LEN-1):
            # No need to care ab moves; get board[i] and scan for anything that isnt _
            if board[i][j] != '_' and board[i][j+1] != '_':
                if board[i][j] == board[i][j+1]:
                    board[i][3] = str(int(board[i][j])+ int(board[i][j+1]))
                    board[i][j] = '_'
                    board[i][j+1] = '_'
            #if the current isn't empty and not equal to next and next is empty
            if board[i][j] != '_' and board[i][j] != board[i][j+1] and board[i][j+1] == '_':
                board[i][j+1] = board[i][j]
                board[i][j] = '_'
            
    printBoard(board)
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
    userMove(board)
main()