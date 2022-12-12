# Game 2048
# 2048 is a board game with nxn dimensions which fills with the number 2
# and 4. The goal of the user is to add identical numbers til 2048.
import random

LEN = 4
RM = [] #Stores random moves (r,c)
PM = [] #Stores row and col of present element

# Design: 
    # Initialize the board
    #   - start with a board with two 2s randomly placed.
def createBoard(board):
    for i in range(LEN):
        col = []
        for j in range(LEN):
            col.append(0)
        board.append(col)

def printBoard(board):
    for i in range(LEN):
        for j in range(len(board[i])):
            #print("\t\t",' '.join(board[i]),end = "\n")
            print("\t", board[i][j], end=" ")
        print("\n")

    # Get the random row and col to populate the board
def randMove(board):
    currIndex(board)
    randRow = random.randint(0,3)
    randCol = random.randint(0,3)
    # Check for douplicates in random moves and present moves
    while ([randRow, randCol] in PM or [randRow, randCol] in RM):
        print("Redo b/c random douplicate found: ", randRow, randCol)
        randRow = random.randint(0,3)
        randCol = random.randint(0,3)
    print("The random row and col:", randRow, randCol)
    print ("PM: " , PM)
    PM.clear()
    return [randRow, randCol]

# After every move and start of the game
#   - fill random cell with a 2 or a 4
def populate(board, start):
    #If its the start of the game populate two 2s
    if (start):
        RM.append(randMove(board))
        board[RM[0][0]][RM[0][1]] = 2

    #Insert new moves in the begining of the list for easy indexing
    RM.insert(0,randMove(board))
    board[RM[0][0]][RM[0][1]] = 2

    print (RM)
    RM.clear()
    printBoard(board)

# Append non-empty cells to present elements
def currIndex(board):
    for i in range(LEN):
        for j in range(LEN):
            if board[i][j] != 0:
                PM.append([i,j])

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

    return userInput

""" def merge(board):
    for i in range(LEN): 
        for j in range(LEN-1): 
            if board[i][j] == board[i][j+1] and board[i][j] != 0: 
                board[i][j] *= 2 
                board[i][j+1] = 0
     """
    
    
    # Moves
    #   - up, down, right and left
    #   - all elements in the board will move to the furthest direction
# Moves elements all the upwards while adding similar ones
def moveUp(board):
    added = [] #To keep track of whether the elements were already added to avoid adding twice
    
    for i in range(LEN-1,0,-1):        
        for j in range(LEN):

            #Move all the elements to the Up until next remains empty
            if board[i][j] != 0 and board[i-1][j] == 0:
                board[i-1][j] = board[i][j] #moves element Up
                board[i][j] = 0

            #Current isn't empty; current == next and both are not in recently added
            elif board[i][j] != 0 and board[i][j] == board[i-1][j] and (i, j) not in added and (i-1,j) not in added:
                #Double the value of the element and empty current
                board[i-1][j] *= 2
                board[i][j] = 0
    
                added.append((i, j))
                added.append((i-1, j))

    populate(board,False)

# Moves elements to the furthest down while adding similar elements once
def moveDown(board):
    
    added = [] 
    
    for i in range(LEN-1):
        for j in range(LEN):

            #Move all the elements downward
            if board[i][j] != 0 and board[i+1][j] == 0:
                board[i+1][j] = board[i][j] #moves element right
                board[i][j] = 0 #empties prev

            #Current isn't empty; current == next and both are not in recently added
            elif board[i][j] != 0 and board[i][j] == board[i+1][j] and (i, j) not in added and (i+1,j) not in added:
                # Double the value of the element
                board[i][j] *= 2
                board[i+1][j] = board[i][j]
                board[i][j] = 0

                #WORKEDDD to skip a 0 in the middle
                if i != 0 and board[i-1][j]!=0:
                    board[i][j] = board[i-1][j]
                    board[i-1][j] = 0

                added.append((i, j))
                added.append((i+1, j))
            


    populate(board,False)



# Moves elements to the furthest left while adding similar elements once
def moveLeft(board):
    for i in range(LEN):
        
        added = [] #To keep track of whether the elements were already added to avoid adding twice
        
        for j in range(LEN-1,0,-1):
            
            #Move all the elements to the left
            if board[i][j] != 0 and board[i][j-1] == 0:
                board[i][j-1] = board[i][j] #moves element left
                board[i][j] = 0
            
            #Current isn't empty; current == prev and both are not in recently added
            elif board[i][j] != 0 and board[i][j] == board[i][j-1] and (i, j) not in added and (i,j-1) not in added:
                #Double the value of the element and empty current
                board[i][j] *= 2
                board[i][j-1] = board[i][j]
                board[i][j] = 0
                #WORKEDDD to skip a 0 in the middle
                if j != 3 and board[i][j+1]!=0:
                    board[i][j] = board[i][j+1]
                    board[i][j+1] = 0

                added.append((i, j))
                added.append((i, j-1))
    
    populate(board,False)


# Moves elements to the furthest right while adding similar elements once
def moveRight(board):
    for i in range(LEN):
        
        added = [] #To keep track of whether the elements were already added to avoid adding twice
        
        for j in range(LEN-1):

            #Move all the elements to the right
            while board[i][j] != 0 and board[i][j + 1] == 0:
                board[i][j + 1] = board[i][j] #moves element right
                board[i][j] = 0 #empties prev

            #Current isn't empty; current == next and both are not in recently added
            if board[i][j] != 0 and board[i][j] == board[i][j + 1] and (i, j) not in added and (i,j+1) not in added:
                # Double the value of the element
                board[i][j] *= 2
                board[i][j+1] = board[i][j]
                board[i][j] = 0 #empty current
                #WORKEDDD to skip a 0 in the middle
                if j != 0 and board[i][j-1]!=0:
                    board[i][j] = board[i][j-1]
                    board[i][j-1] = 0


                added.append((i, j))
                added.append((i, j+1))

    populate(board,False)


    # After every move 
    #   - fill random cell with a 2 or a 4

    # WIN
    # - all elements must add upto 2048

# GAME OVER
# - no empty spaces left to fill with a 2 or a 4
def gameOver(board):
    for i in range(LEN):
        for j in range(LEN):
            if board[i][j] == 0:
                return False

    return True


def main():
    board = []
    start = True #Is it the start of the game? 
    print("\t     Welcome to 2048\n",
            "Begin by joining the numbers and get to 2048.")
    createBoard(board)
    populate(board, start)
    start = False
    userInput = userMove(board)
    while(userInput != 'q' and userInput != 'Q' and gameOver(board) != True):
        userInput = userMove(board)
        #check gameover or win
        gameOver(board)
    
main()