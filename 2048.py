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
    # Check for douplicates in random moves and present moves
    while ([randRow, randCol] in RM or [randRow, randCol] in PM):
        print("Redo b/c random douplicate found: ", randRow, randCol)
        randRow = random.randint(0,3)
        randCol = random.randint(0,3)
        return randRow, randCol
    print("The random row and col:", randRow, randCol)
    PM.clear()
    return [randRow, randCol]

# After every move and start of the game
#   - fill random cell with a 2 or a 4
def populate(board, start):
    isEmpty(board)
    print ("PM: " , PM)
    #If its the start of the game populate two 2s
    if (start):
        RM.append(randMove())
        board[RM[0][0]][RM[0][1]] = '2'

    #Insert new moves in the begining of the list for easy indexing
    RM.insert(0,randMove())
    board[RM[0][0]][RM[0][1]] = '2'

    printBoard(board)
    print (RM)
    RM.clear()

# Append non-empty cells to present elements
def isEmpty(board):
    for i in range(LEN):
        for j in range(LEN):
            if board[i][j] != '_':
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
    # Moves
    #   - up, down, right and left
    #   - all elements in the board will move to the furthest direction
def moveUp(board):
    print("Move up was called")
    for i in range(LEN-1,0,-1):
        #Goal : Move element all the way up in it's column
        for j in range(LEN):
            #get board[i] and scan for anything that isnt _
            #if curr isn't empty and prev isn't empty
            if board[i][j] != '_' and board[i-1][j] != '_':
                #if curr and prev are equal the far left contains the sum
                if board[i][j] == board[i-1][j]:
                    board[3][j] = str(int(board[i][j])+ int(board[i-1][j]))
                    ##print("Board[i][0]", 3, j," is updated to: ", board[3][j])
                    board[i][j] = '_'
                    ##print(i,j ,"is empty now")
                    #make sure prev isn't 3rd row;
                    if(i-1 != 3):
                        board[i+1][j] = '_'
                        ##print(i+1,j, "Next is empty ")
    
            #if the current isn't empty and not equal to next and next is empty
            elif board[i][j] != '_' and board[i][j] != board[i-1][j] and board[i-1][j] == '_':
                board[i-1][j] = board[i][j]
                board[i][j] = '_'
                ##print("Board[i+1][j]", i-1,j, " is updated to: ", board[i-1][j])
                #printBoard(board)
    populate(board,False)

def moveDown(board):
    print("Move down was called")
    #Start from 0,0 and move down each row
    for i in range(LEN-1):
        #Goal : Move element all the way down in it's column
        for j in range(LEN):
            #get board[i] and scan for anything that isnt _
            #if curr isn't empty and next isn't empty
            if board[i][j] != '_' and board[i+1][j] != '_':
                #if curr and next are equal the far down contains the sum
                if board[i][j] == board[i+1][j]:
                    board[i+1][j] = str(int(board[i][j])+ int(board[i+1][j]))
                    board[i][j] = board[i-1][j]
                    break

            #if the current isn't empty and not equal to next and next is empty
            if board[i][j] != '_' and board[i][j] != board[i+1][j] and board[i+1][j] == '_':
                board[i+1][j] = board[i][j]
                board[i][j] = '_'
                
    populate(board,False)

def moveLeft(board):
    print("Move Left was called")
    #Start from 0,3 and keep moving to the left col
    #Goal : [_ _ 2 _] to move 2 to the left
    for i in range(LEN):
        for j in range(LEN-1,0,-1):

            #get board[i] and scan for anything that isnt _
            #if curr isn't empty and prev isn't empty
            if board[i][j] != '_' and board[i][j-1] != '_':
                #if curr and prev are equal the far left contains the sum
                if board[i][j] == board[i][j-1]:
                    board[i][0] = str(int(board[i][j])+ int(board[i][j-1]))
                    ##print("Board[i][0]", i, 0," is updated to: ", board[i][0])
                    board[i][j] = '_'
                    ##print(i,j ,"is empty now")
                    #make sure prev isn't far left; o/w far left would be _ instead of sum
                    if(j-1 != 0):
                        board[i][j-1] = '_'
    
            #if the current isn't empty and not equal to prev and prev is empty
            elif board[i][j] != '_' and board[i][j] != board[i][j-1] and board[i][j-1] == '_':
                board[i][j-1] = board[i][j]
                board[i][j] = '_'
                ##print("Board[i][j-1]", i,j-1, " is updated to: ", board[i][j-1])
            
    populate(board,False)


def moveRight(board):
    print("Move right was called")
    for i in range(LEN):
        #Goal : [_ 2 _ _] to move 2 to the right
        for j in range(LEN-1):
            # No need to care ab moves; get board[i] and scan for anything that isnt _
            if board[i][j] != '_' and board[i][j+1] != '_':
                if board[i][j] == board[i][j+1]:
                    board[i][j+1] = str(int(board[i][j])+ int(board[i][j+1]))
                    board[i][j] = board[i][j-1]
                    break
                       
            #if the current isn't empty and not equal to next and next is empty
            if board[i][j] != '_' and board[i][j] != board[i][j+1] and board[i][j+1] == '_':
                board[i][j+1] = board[i][j]
                board[i][j] = '_'
            
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
            if '_' in board[i][j]:
                return False

    return True



def main():
    board = []
    start = True #Is it the start of the game? 
    print("\t     Welcome to 2048\n",
            "Begin by joining the numbers and get to 2048.")
    printBoard(board)
    populate(board, start)
    start = False 
    userInput = userMove(board)
    while(userInput != 'q' and userInput != 'Q' and gameOver(board) != True):
        userInput = userMove(board)
        #check gameover or win
        gameOver(board)
    


main()