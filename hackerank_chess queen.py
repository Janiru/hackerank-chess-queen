from typing import Sized


def make_2D_array(size):
    twoDArray = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        twoDArray.append(row)
    return twoDArray

first_input = input()
board_length,num_obs = first_input.split()
board_length = int(board_length)
num_obs = int(num_obs)
second_input = input()
queen_row,queen_column = second_input.split()
queen_row = int(queen_row)
queen_column = int(queen_column)
chess_board = make_2D_array(board_length)
movments_count = 0

#bools for movments
Up = False
Down = False
Left = False
Right = False

diagonal_top_left = False
diagonal_top_right = False
diagonal_bottom_left = False
diagonal_bottom_right = False

#placing the obstacles 
for i in range(num_obs):
    obs_input = input()
    obs_r,obs_c = obs_input.split()
    obs_r = int(obs_r)
    obs_c = int(obs_c)
    chess_board[obs_r-1][obs_c-1] = 2
#placing the queen
chess_board[queen_row-1][queen_column-1] = 1

#calculating the movments

# up
for y in range(1, queen_row):
    if(chess_board[(queen_row-y)-1][queen_column-1] != 2 and Up == False):
        chess_board[(queen_row-y)-1][queen_column-1] = 9
        movments_count += 1
    else: 
        Up = True
#Down
for y in range(1, (board_length-queen_row) + 1):
    if(chess_board[(queen_row+y)-1][queen_column-1] != 2 and Down == False):
        chess_board[(queen_row+y)-1][queen_column-1] = 9
        movments_count += 1
    else: 
        Down = True
# right
for y in range(1, (board_length - queen_column) + 1):
    if(chess_board[(queen_row)-1][(queen_column+y)-1] != 2 and Right == False):
        chess_board[(queen_row)-1][(queen_column+y)-1] = 9
        movments_count += 1
    else: 
        Right = True 
# left
for y in range(1,queen_column):
    if(chess_board[(queen_row)-1][(queen_column-y)-1] != 2 and Left == False):
        chess_board[(queen_row)-1][(queen_column-y)-1] = 9
        movments_count += 1
    else: 
        Left = True 
#top left
for y in range(1,queen_column):
    if(chess_board[(queen_row-y)-1][(queen_column-y)-1] != 2 and diagonal_top_left == False):
        chess_board[(queen_row-y)-1][(queen_column-y)-1] = 9
        movments_count += 1
    else: 
        diagonal_top_left = True 
#top right
for y in range(1,queen_column):
    if(chess_board[(queen_row-y)-1][(queen_column+y)-1] != 2 and diagonal_top_right == False):
        chess_board[(queen_row-y)-1][(queen_column+y)-1] = 9
        movments_count += 1
    else: 
        diagonal_top_right = True 
    
#bottom left
for y in range(1,queen_column):
    if(chess_board[(queen_row+y)-1][(queen_column-y)-1] != 2 and diagonal_bottom_left == False):
        chess_board[(queen_row+y)-1][(queen_column-y)-1] = 9
        movments_count += 1
    else: 
        diagonal_bottom_left = True 
#bottom right
for y in range(1,queen_column):
    if(chess_board[(queen_row+y)-1][(queen_column+y)-1] != 2 and diagonal_bottom_right == False):
        chess_board[(queen_row+y)-1][(queen_column+y)-1] = 9
        movments_count += 1
    else: 
        diagonal_bottom_right = True
   

#printing the array
print()
for i in chess_board:
    for j in i:
        print(j,end=" ")
    print("")
print(f"movs {movments_count}")
