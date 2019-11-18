import random
import os
from time import sleep

rows, cols = 30, 30;
board = [[ random.getrandbits(1) for x in range(cols)] for y in range(rows)] 
 
rules = { (1,2): 1 , (1,3): 1, (0,3):1  }
sprites = { 0: '.' ,1:'#' }

def print_board(myboard):
    for r in range(rows):
        for c in range (cols):
            print sprites[myboard[r][c]],
        print
    
print_board(board)
while(True):
    new_board = [[0 for x in range(cols)] for y in range(rows)] 
    #clean our canvas
    sleep(0.1)
    os.system('clear')
    #calculate new_board
    for r in range(rows):
        for c in range (cols):
            my_living_neighbours = 0
            for x_offset in [-1,0,+1]:
                for y_offset in [-1,0,+1]:
                   my_living_neighbours += board[ (r+x_offset) % rows][(c+y_offset) % cols ]
            my_living_neighbours = my_living_neighbours - board[r][c]
            new_board[r][c] = rules.get( (board[r][c], my_living_neighbours), 0 )
    
    board = new_board 
    print_board(board)
