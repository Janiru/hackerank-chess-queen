import numpy as np
import re

first_input = input()
board_lenght, num_obstacles = first_input.split()

second_input = input()
queen_y, queen_x = second_input.split()

num_obstacles = int(num_obstacles)
board_lenght = int(board_lenght)
queen_y = int(queen_y)
queen_x = int(queen_x)
obstacle_array = []

Up = False
Down = False
Left = False
Right = False

## make 2D array

def make_2D_array(rows,cols):
    twoDArray = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        twoDArray.append(row)
    return twoDArray

chess_board = make_2D_array(board_lenght,board_lenght)

##
# getting inputs for obstacles

for obstacles in range(0, num_obstacles):
    obstacle = input()
    obstacle_x, obstacle_y = obstacle.split()
    obstacle_x = int(obstacle_x)
    obstacle_y = int(obstacle_y)
    obstacle_array.insert(obstacles, [obstacle_x, obstacle_y])

obstacle_array_rows = (len(obstacle_array))
obstacle_array_cols = (len(obstacle_array[0]))
    
# placing the obstacles on the chess board

for row in range(obstacle_array_rows):
    pawn = obstacle_array[row]
    pawn = ' '.join([str(elem) for elem in pawn])
    pawn=pawn.replace(",","")
    print(pawn)
    obs_r,obs_c = pawn.split()
    chess_board[int(obs_r)][int(obs_c)] = 2

# calculate the number of possible moves

# going up
for y in range(1,queen_y + 1 ):
    if chess_board[queen_y - y][queen_x] != 2 and Up== False:
        chess_board[queen_y - y][queen_x] = 3
    else:
        Up=True
#going down 

for y in range(1,(board_lenght - queen_y)):
    if chess_board[queen_y + y][queen_x] != 2 and Down== False:
        chess_board[queen_y + y][queen_x] = 3
    else:
        Down=True

#going left

for y in range(1,queen_y + 1 ):
    if chess_board[queen_y - y][queen_x] != 2 and Left== False:
        chess_board[queen_y - y][queen_x] = 3
    else:
        Left=True

# place queen
chess_board[queen_y][queen_x] = 1

# printing the array

for row in chess_board:
   for column in row:
      print(int(column),end = " ")
   print()

