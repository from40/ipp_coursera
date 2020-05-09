#!/usr/bin/env python3
# https://py3.codeskulptor.org/#user305_nv0JPAdEjIR2tyk.py
"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random
import sys
sys.path.append('2048')
import game_2048_testsuite as testsuite


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    merged_list = [0 for dummy_ind in range(len(line))]
    update_index = 0
    for index in range(len(line)):
        if line[index] != 0:
            if merged_list[update_index] == 0:
                merged_list[update_index] += line[index]
            else:
                if merged_list[update_index] == line[index]:
                    merged_list[update_index] += line[index]
                    update_index += 1
                else:
                    update_index += 1
                    merged_list[update_index] += line[index]
    return merged_list


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._grid = []
        self.reset()

        up_list = []
        down_list = []
        for ind in range(self._width):
            up_list.append([0, ind])
            down_list.append([self._height - 1, ind])
        left_list = []
        right_list = []
        for ind in range(self._height):
            left_list.append([ind, 0])
            right_list.append([ind, self._width - 1])
        self._initial_indices = {UP: up_list,
                                 DOWN: down_list,
                                 LEFT: left_list,
                                 RIGHT: right_list,
                                 }
        print(self._initial_indices)

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_column in range(self._width)] for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        msg = "["
        for row in range(self._height):
            msg += str(self._grid[row])
        msg += "]"
        return msg

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        grid_change = False
        if direction in (UP, DOWN):
            steps = self._height
        if direction in (LEFT, RIGHT):
            steps = self._width
        for pos in self._initial_indices[direction]:
            temp_list = []
            for step in range(steps):
                row = pos[0] + step * OFFSETS[direction][0]
                col = pos[1] + step * OFFSETS[direction][1]
                temp_list.append(self._grid[row][col])
            temp = merge(temp_list)
            for step in range(steps):
                row = pos[0] + step * OFFSETS[direction][0]
                col = pos[1] + step * OFFSETS[direction][1]
                if temp[step] != self._grid[row][col]:
                    grid_change = True
                self._grid[row][col] = temp[step]
        if grid_change:
            self.new_tile()
        #msg = ""
        #for row in range(self._height):
        #    msg += str(self._grid[row])
        #return msg

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if random.randint(0, 100) < 90:
            new_tile = 2
        else:
            new_tile = 4
        row = random.randrange(self._height)
        col = random.randrange(self._width)
        while self._grid[row][col] != 0:
            row = random.randrange(self._height)
            col = random.randrange(self._width)
        self.set_tile(row, col, new_tile)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


# test for TwentyFortyEight class
if __name__ == '__main__':
    testsuite.run_test(TwentyFortyEight)


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))