# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:44:41 2026

@author: Zivireus
"""

maze_grid = []
bomb_grid = []
start_pos = (-1, -1)
end_pos = (-1, -1)


def parse_grid(gridFileName):
    global start_pos, end_pos
    
    gridFile = open(gridFileName, "r")
    
    line = gridFile.readline()
    while len(line) != 1:
        as_list = line.strip().split()
        maze_grid.append(as_list)
        line = gridFile.readline()
    
    line = gridFile.readline()
    while len(line) != 1 and line:
        as_list = line.strip().split()
        bomb_grid.append(as_list)
        line = gridFile.readline()
            
    gridFile.close()
    
    for i in range(len(maze_grid)):
        for j in range(len(maze_grid[0])):
            if(maze_grid[i][j] == 's'): start_pos = (i, j)
            if(maze_grid[i][j] == 'o'): end_pos = (i, j)
    

def get_start_position():
    return start_pos

def get_end_position():
    return end_pos

def get_maze_grid():
    return maze_grid

def get_bomb_grid():
    return bomb_grid
