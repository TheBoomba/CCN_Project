# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:44:41 2026

@author: Zivireus

All grid information in this file follows the following format:
    - (0, 0) is the most top left corner of the grid.
    - '.' is an open tile the player can travel to.
    - 'x' is a blocked tile the player cannot travel to.
    - 's' is the current player location.
    - 'o' is the final location the player is trying to travel to.
    - "b" is a bomb tile where the player loses if traversed.
"""
class Grid:
    MOVES = {
        "w": (-1, 0),  # Up
        "s": (1, 0),   # Down
        "a": (0, -1),  # Left
        "d": (0, 1),   # Right
        }
    
    def __init__(self, filename):
        self.maze_grid = []
        self.bomb_grid = []
        self.player_pos = None
        self.exit_pos = None
        self.parse_grid(filename)
        
    def return_grid(self, gridType):
        """ Returns a string detailing every tile in the grid.
        
        Args: 
            gridType (str) -- "maze" or "bomb" depending on which is desired.
        """
        string = ""
        if(gridType == "maze"):
            for i in range(len(self.maze_grid)):
                for j in range(len(self.maze_grid[i])):
                    string += self.maze_grid[i][j] + ' '
                string += '\n'
                
        if(gridType == "bomb"):
            for i in range(len(self.bomb_grid)):
                for j in range(len(self.bomb_grid[i])):
                    string += self.bomb_grid[i][j] + ' '
                string += '\n'
        return string
        
    #probably unneeded
    def __str__(self):
        string = ""
        for i in range(len(self.maze_grid)):
            for j in range(len(self.maze_grid[i])):
                string += self.maze_grid[i][j] + ' '
            string += '\n'
        return string
            
    def has_won(self):
        """ Returns true if the player reaches the exit. """
        return self.player_pos == self.exit_pos
    
    def has_lost(self):
        """ Returns true if the player has stepped on a bomb. """
        return self.get_bomb_value(self.player_pos) == "b"
    
    def get_maze_value(self, pos):
        """ Returns the tile at pos in maze_grid. """
        return self.maze_grid[pos[0]][pos[1]]
    
    def set_maze_value(self, pos, newValue):
        """ Sets the value at pos to newValue. """
        row, col = pos
        self.maze_grid[row][col] = newValue;
    
    def get_bomb_value(self, pos):
        """ Returns the tile at pos in bomb_grid. """
        return self.bomb_grid[pos[0]][pos[1]]
    
    def is_valid_pos(self, pos):
        """ Checks the next position the player wants to travel to.

        Arguments:
            next_pos (int, int) -- coordinates of the position the player 
                                   wants to travel to.
        Returns
            True -- The player can travel to next_pos.
            False -- The player cannot travel to next_pos.
        """
        # Checks grid boundaries
        if(pos[0] < 0 or 
           pos[1] < 0 or 
           pos[0] >= len(self.maze_grid) or 
           pos[1] >= len(self.maze_grid[0])): 
            return False
        # Checks if next_pos is a wall
        if(self.maze_grid[pos[0]][pos[1]] == 'x'): 
            return False
        return True
    
    def parse_grid(self, gridFileName):
        """ Reads a txt file and populates the grids and key positions.
        
        Parses the input file into 2D lists for 'self.maze_grid' and 
        'self.bomb_grid'. 
        Then locates the start position ('player_pos') and the grid's
        exit position ('exit_pos').
        
        Args:
            gridFileName (str) -- Name of the text file containing grid info.
        """
        with open(gridFileName, "r") as gridFile:
            # Maze Grid
            line = gridFile.readline()
            while len(line) != 1:
                as_list = line.strip().split()
                self.maze_grid.append(as_list)
                line = gridFile.readline()
            
            # Bomb Grid
            line = gridFile.readline()
            while len(line) != 1 and line:
                as_list = line.strip().split()
                self.bomb_grid.append(as_list)
                line = gridFile.readline()
        
        # Find player_pos and exit_pos
        for i in range(len(self.maze_grid)):
            for j in range(len(self.maze_grid[0])):
                if(self.maze_grid[i][j] == 's'): self.player_pos = (i, j)
                if(self.maze_grid[i][j] == 'o'): self.exit_pos = (i, j)

    def can_move(self, direction):
        """ Sees if the player can travel to the next tile.
        
        Adds the direction to the player's current position. 
        It checks if that new tile is a valid position for the player to be. 
        
        Args:
            direction (str) -- w, a, s, or d
        """
        if direction not in self.MOVES: return False
        
        next_pos = tuple( 
            map(lambda x, y: x + y, self.player_pos, self.MOVES[direction])
            )
        
        if self.is_valid_pos(next_pos):
            self.set_maze_value(self.player_pos, ".")
            self.set_maze_value(next_pos, "s")
            self.player_pos = next_pos
            return True
        return False
        
    
    
