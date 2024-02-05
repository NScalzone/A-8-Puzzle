import math
from heuristics import heuristic_one, manhattan_distance, my_heuristic

PUZZLE = 8
#PUZZLE = 15
SQUARES = PUZZLE + 1
#Puzzle 1
#START = [5,2,8,4,1,7,'b',3,6]

#Puzzle 2
START = [4,5,'b',1,6,8,7,3,2] 

#other puzzle tried
#START = [8,7,4,'b',5,1,6,3,2]

GOAL = [1,2,3,4,5,6,7,8,'b']

#15 Puzzle config
#START = [2,3,5,6,8,9,1,4,7,10, 'b',15,14,13,12,11]
#START = [13,9,5,1,14,6,7,2,15,10,11,3,'b',12,8,4]
#GOAL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'b']


GOAL_BOARD = []
OutFile = open('Best_First_h3_P2.txt', 'w')


def create_board(squares: int, start: list, board):
    """ 
    Function to create a square board from a given list of inputs
    """
    board_size = int(math.sqrt(squares))
    list_ind = 0
    for j in range(0, board_size, 1):
        board.append([])
        for k in range(0, board_size, 1):
            board[j].append(start[list_ind])
            list_ind += 1 

def count_inversions(board):
    total_inversions = 0
    for i in range(0, len(board), 1):
        if board[i] != 'b':
            
            for j in range((i), len(board), 1 ):
                if board[j] != 'b':
                
                    if board[j] < board[i]:
                        total_inversions += 1
    return total_inversions

def goal_reachable(start, goal):
    start_count = count_inversions(start)
    goal_count = count_inversions(goal)
    if (start_count % 2) == 0 and (goal_count % 2) == 0:
        return True
    else:
        return False

def board_to_list(board):
    """
    Function to convert the board back to list to evaluate
    """
    current_list = []
    for i in range(0, len(board), 1):
        for j in range(0, len(board[i]), 1):
            current_list.append(board[i][j])
    return current_list

def find_blank(board):
    blank_index = []
    for i in range(0, len(board), 1):
        for j in range(0, len(board), 1):
            if board[i][j] == 'b':
                blank_index.append(i)
                blank_index.append(j)
                return blank_index

def go_up(blank, board):
    mininum = 0
    maximum = len(board) - 1
    blank_row = blank[0]
    blank_col = blank[1]
    if blank_row > mininum:
        temp = board[blank_row - 1][blank_col]
        board[blank_row - 1][blank_col] = 'b'
        board[blank_row][blank_col] = temp
        uplist = (board_to_list(board))
        temp = board[blank_row][blank_col]
        board[blank_row][blank_col] = 'b'
        board[blank_row - 1][blank_col] = temp
        return uplist
    else:
        return 0
    
def go_down(blank, board):
    mininum = 0
    maximum = len(board) - 1
    blank_row = blank[0]
    blank_col = blank[1]
    if blank_row < maximum:
        temp = board[blank_row + 1][blank_col]
        board[blank_row + 1][blank_col] = 'b'
        board[blank_row][blank_col] = temp
        downlist = (board_to_list(board))
        temp = board[blank_row][blank_col]
        board[blank_row][blank_col] = 'b'
        board[blank_row + 1][blank_col] = temp
        return downlist
    else:
        return 0

def go_left(blank, board):
    mininum = 0
    maximum = len(board) - 1
    blank_row = blank[0]
    blank_col = blank[1]
    if blank_col > mininum:
        temp = board[blank_row][blank_col - 1]
        board[blank_row][blank_col - 1] = 'b'
        board[blank_row][blank_col] = temp
        leftlist = (board_to_list(board))
        temp = board[blank_row][blank_col]
        board[blank_row][blank_col] = 'b'
        board[blank_row][blank_col - 1] = temp
        return leftlist
    else:
        return 0

def go_right(blank, board):
    mininum = 0
    maximum = len(board) - 1
    blank_row = blank[0]
    blank_col = blank[1]
    if blank_col < maximum:
        temp = board[blank_row][blank_col + 1]
        board[blank_row][blank_col + 1] = 'b'
        board[blank_row][blank_col] = temp
        rightlist = (board_to_list(board))
        temp = board[blank_row][blank_col]
        board[blank_row][blank_col] = 'b'
        board[blank_row][blank_col+ 1] = temp
        return rightlist
    else:
        return 0
    
if goal_reachable(START, GOAL):    
    
    # Create boards    
    BOARD = []
    create_board(SQUARES,START,BOARD)
    create_board(SQUARES,GOAL,GOAL_BOARD)
    print(BOARD)
    print(GOAL_BOARD)

    PreviousStates = []
    PreviousStates.append(START)

    runs = 0
    Solved = False
    decision_que = {}
    while runs < 8000 and not Solved:

         # Determine move options
        blank_index = find_blank(BOARD)
        up = go_up(blank_index, BOARD)
        down = go_down(blank_index, BOARD)
        left = go_left(blank_index, BOARD)
        right = go_right(blank_index, BOARD)
        move_options = [up, down, left, right]
        
        # find moves that have not already been played
        for i in move_options:
            if i != 0:
                if i not in PreviousStates:
                    # Heuristic one uses lists as it's input. Comment the lines creating the 
                    # test board to run heuristic one.
                    # To run with manhattan distance or my heuristic, we need boards at inputs. 
                    # Please uncomment the following two lines, and the line for the heuristic you want
                    # to use. 

                    test_board = []
                    create_board(SQUARES, i, test_board)
                    #score = manhattan_distance(GOAL_BOARD, test_board)
                    score = my_heuristic(GOAL_BOARD, test_board)
                    #score = heuristic_one(GOAL, i)
                    decision_que[score] = i
                    
        # Identify best current move              
        best_key = min(decision_que.keys()) 
        best_option = decision_que[best_key]

        # If puzzle is solved, end loop
        if best_option == GOAL:
            Solved = True
            
        #Add the next state of the puzzle to the list of visited positions     
        PreviousStates.append(best_option)
        
        # Reset board to new current state
        BOARD = []
        create_board(SQUARES, best_option, BOARD)
        
         # Printouts for solution path
        #print(' Total runs: ', runs,'\n', BOARD ,'\n')
        OutFile.write(' Total runs: ')
        OutFile.write(str(runs))
        OutFile.write('\n')
        OutFile.write(str(BOARD))
        OutFile.write('\n')
        
        # remove the current state from the queue so that it isn't revisited
        del decision_que[best_key]
        runs += 1

    if Solved:
        print('Puzzle Sovled! ', runs, ' runs required.')
    else:
        print('Puzzle could not be solved in 8000 moves or less')

else:
    print("Goal state is unreachable, please provide new start state")

