import math

def heuristic_one(goal:list, current:list):
    total_misplaced = 0
    for i in range(len(goal)):
        if goal[i] != current[i]:
            total_misplaced += 1
    return total_misplaced

def find_index(target, board):
    index = []
    for i in range(len(board)):
        for j in range(len(board[i])): 
            if board[i][j] == target:
                index.append(i)
                index.append(j)
    return index

def manhattan_distance(goal, current):
    total_manhattan_distance = 0
    for i in range(len(current)):
        for j in range(len(current[i])):
            goal_index = find_index(current[i][j], goal)
            row_diff = abs(i - goal_index[0])
            col_diff = abs(j - goal_index[1])
            total_diff = row_diff + col_diff
            total_manhattan_distance += total_diff
    return total_manhattan_distance

# for my heuristic, I chose total euclidian distance, as that is admissable and will genrally be slightly
# less (or equal to) than the mahattan distance at any given configuration.
def my_heuristic(goal, current):
    total_score = 0
    for i in range(len(current)):
        for j in range(len(current[i])):
            goal_index = find_index(current[i][j], goal)
            row_diff = abs(i - goal_index[0])
            col_diff = abs(j - goal_index[1])
            
            euclidian_distance = math.sqrt(row_diff^2 + col_diff^2)
            total_score += round(euclidian_distance, 1)
    
    # convert to int to simplify comparison, with full decimal representation it takes forever because
    # there are so many distinct data points
    return int(total_score)
