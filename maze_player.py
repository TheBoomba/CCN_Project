# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:22:41 2026

@author: Zivireus

All grid information in this file follows the following format:
    - (0, 0) is the most top left corner of the grid.
    - '.' is an open tile the player can travel to.
    - 'x' is a blocked tile the player cannot travel to.
    - 's' is the current player location.
    - 'o' is the final location the player is trying to travel to.
"""

from parse_grids import Grid

    
filename = input("Input Maze Text File: ")
if ( filename.find(".txt") == -1 ): filename += ".txt"
maze = Grid(filename)

while True:
    if( maze.has_won() ):
        print("You have escaped the maze!")
        break
    if ( maze.has_lost() ):
        print("You blew up...")
        break
    
    print( "Maze:\n" + maze.return_grid("maze") )
    print( "Bomb:\n" + maze.return_grid("bomb") )
    
    move = input("Move (w/a/s/d/end): ").lower().strip()
    if not maze.can_move(move):
        print("You can't move there.")
    
    
    
    