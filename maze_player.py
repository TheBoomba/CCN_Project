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
    - The first grid is the maze grid, the second is the bomb grid.
    - Leave an empty line in between the two grids.
    - Each column is separated by a space and each row is a newline.
    i.e. maze1.txt
    o . x
    . . .
    . x s

    . . .
    b . .
    b b .
"""

from parse_grids import Grid

while True:
    try:
        filename = input("Enter maze filename (or 'end' to quit): ").strip()
        if filename.lower() == "end": break
        if ( filename.find(".txt") == -1 ): filename += ".txt"
        maze = Grid(filename)
        break
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please try again.\n")

while not maze.is_game_over():
    print( "Maze:\n" + maze.return_grid("maze") )
    print( "Bomb:\n" + maze.return_grid("bomb") )
    
    move = input("Move (w/a/s/d/end): ").lower().strip()
    if move == "end": 
        print("Ending game...")
        break
    if not maze.can_move(move):
        print("You can't move there.")
    
if( maze.has_won() ): print("You have escaped the maze!")
if ( maze.has_lost() ): print("You blew up...")
    
    
    