"""
Tic Tac Toe Player
"""

#from asyncio.windows_events import NULL
#from email.policy import default
from asyncio.windows_events import NULL
import math

from numpy import Infinity
#from operator import truediv
#from queue import Empty
#from turtle import pos
#from typing import final

X = "X"
O = "O"
EMPTY = None
depth = 0



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY,EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    '''return [['X', EMPTY, EMPTY],
            ['X', EMPTY, EMPTY],
           [EMPTY, EMPTY,'O']]'''


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    x = o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x += 1
            elif board[i][j] == 'O':
                o += 1
    if x == o :
        return 'X'
    elif x > o :
        return 'O'

"""
def actions(board):
    '''
    Returns set of all possible actions (i, j) available on the board.
    '''
    # raise NotImplementedError
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return tuple(possible_actions)
"""

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    modified_board = board
    try:
        if modified_board[action[0]][action[1]] == EMPTY:
            modified_board[action[0]][action[1]] = player(board)
        else:
            raise IndexError
    except IndexError:
        print("Invalid move")
    finally:
        return modified_board


def winner(board):
    '''
    Returns the winner of the game, if there is one
    '''
    # raise NotImplementedError

    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
           return board[i][0]

    # check column
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
           return board[0][j]

    # check digonal
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[j][i]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return EMPTY

def terminal(board):
    '''
    Returns True if game is over, False otherwise.
    '''
    winningPlayer = winner(board)
    if winningPlayer != EMPTY:
        return winningPlayer
    elif isMovesLeft(board) == False:
        return True
    
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError

    if terminal(board):
        winning_player = winner(board)
        if winning_player == 'X':
            return 10
        elif winning_player == 'O':
            return -10
        return 0


'''
def findBest(board, turn) :
    score = utility(board)
    if score is None : score = 0
    actions_list = actions(board)
    # If Maximizer has won the game return his/her
    # evaluated score
    if score == 1 or score == -1 :
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if (len(actions_list) == 0) :
        return 0


    # If this maximizer's move
    if turn :    
        best = -100

        # Traverse all cells
        for i in actions_list :        
            new_board = result(board, i)

            # Call minimax recursively and choose
            # the maximum value
            best = max(best, findBest(new_board, False))

            # Undo the move
            board[i[0]][i[1]] = EMPTY
        return best

    # If this minimizer's move
    else :
        best = 100

        # Traverse all cells
        for i in actions_list :
            new_board = result(board, i)

            # Call minimax recursively and choose
            # the minimum value
            best = min(best, findBest(new_board, True))

            # Undo the move
            board[i[0]][i[1]] = EMPTY
        return best
'''       

'''
def minimax(board):

    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    
    bestVal = -100
    actions_list = actions(board)
 
    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in actions_list :
        new_board = result(board, i)
        
        moveVal = findBest(new_board, False)

        # Undo the move
        board[i[0]][i[1]] = EMPTY

        # If the value of the current move is
        # more than the best value, then update
        # best/
        if (moveVal > bestVal) :               
            bestMove = (i[0], i[1])
            bestVal = moveVal
    return bestMove
'''




def isMovesLeft(board) :
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == EMPTY) :
                return True
    return False
 
'''
def evaluate(b) :
   
    # Checking for Rows for X or O victory.
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
            if (b[row][0] == player(b)) :
                return 10
            elif (b[row][0] == opponent) :
                return -10
 
    # Checking for Columns for X or O victory.
    for col in range(3) :
      
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
         
            if (b[0][col] == player(b)) :
                return 10
            elif (b[0][col] == opponent) :
                return -10
 
    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
     
        if (b[0][0] == player(b)) :
            return 10
        elif (b[0][0] == opponent) :
            return -10
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
        if (b[0][2] == player(b)) :
            return 10
        elif (b[0][2] == opponent) :
            return -10
 
    # Else if none of them have won then return 0
    return 0
 '''

def minimax(board, depth, isMax) :
    score = utility(board)
    if (score == 10) :
        return score
 
    if (score == -10) :
        return score
 
    if (isMovesLeft(board) == False) :
        return 0
 
    if (isMax) :    
        best = -1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (board[i][j]==EMPTY) :
                 
                    # Make the move
                    board[i][j] = player(board)
 
                    # Call minimax recursively and choose
                    # the maximum value
                    best = max( best, minimax(board, depth + 1, not isMax))
 
                    # Undo the move
                    board[i][j] = EMPTY
        return best
 
    else :
        best = 1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (board[i][j] == EMPTY) :
                 
                    # Make the move
                    board[i][j] = player(board)
 
                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, not isMax))
 
                    # Undo the move
                    board[i][j] = EMPTY
        return best
 
def findBestMove(board) :
    bestVal = 0
    bestMove = (-Infinity,-Infinity)
 
    for i in range(3) :    
        for j in range(3) :
         
            # Check if cell is empty
            if (board[i][j] == EMPTY):
                curr_player = player(board)
                
                # Make the move
                board[i][j] = curr_player

                if curr_player == 'X' :
                    bestVal = -1
                    moveVal = minimax(board, 0, False)

                    # Undo the move
                    board[i][j] = EMPTY

                    if (moveVal > bestVal) :               
                        bestMove = (i, j)
                        bestVal = moveVal
 
                else :
                    bestVal = 1
                    moveVal = minimax(board, 0, True) 

                    # Undo the move
                    board[i][j] = EMPTY

                    if (moveVal < bestVal) :               
                        bestMove = (i, j)
                        bestVal = moveVal
 

    print("The value of the best Move is :", bestVal)
    print()
    return bestMove