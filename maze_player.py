# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:22:41 2026

@author: Zivireus
"""

import parse_grids

maze_file = "maze1.txt"
parse_grids.parse_grid(maze_file)
maze_grid = parse_grids.get_maze_grid()
curr_pos = parse_grids.get_start_position()
end_pos = parse_grids.get_end_position()
direction_dict = {'W' : (-1, 0), 'S' : (1, 0), 'A' : (-1, 0), 'D' : (0, 1)}

def print_grid(maze_grid):
    for i in range(len(maze_grid)):
        for j in range(len(maze_grid[i])):
            print(maze_grid[i][j] + ' ', end='')
        print()
    return
    
def check_bounds(next_pos):
    if(next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(maze_grid) or next_pos[1] >= len(maze_grid[0])):
        return False
    
    if(maze_grid[next_pos[0]][next_pos[1]] == 'x'):
        return False
    
    return True
    

def move(direction):
    direction = direction.upper()
    if(direction_dict.get(direction) == None):
        if( direction == "END" ):
            return "END"
        else: 
            print("Invalid Input: Please use 'W', 'A', 'S', 'D' or 'END'.")
            return "invalid"
        
    next_pos = tuple(map(lambda x, y: x + y, curr_pos, direction_dict[direction]))
    if( not check_bounds(next_pos) ):
        print("Cannot travel to ({}, {})".format(next_pos[0], next_pos[1]))
        return "invalid"
    else:
        #not yet implemented
        return
    
    

while True:
    if(curr_pos == end_pos): break
    
    print_grid(maze_grid)

    direction = input("Move in direction: ")
    update = move(direction)
    #print(update)
    if(update == "END"): break
    


    print()
    
    
    
    
    