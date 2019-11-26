#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import copy
import math
from heapq import *
import time


PUZZLE_TYPE = 8
ROW_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))

class state():
    def __init__(self, f, g,  parent, init_state):
        self.f = f
        self.parent = parent
        self.data = init_state
        self.g = g

    # Check if the point is in boundary or not
    def in_boundary(self, position):
        x, y = position
        if x >= 0 and y >= 0 and x <= ROW_SIZE-1 and y <= ROW_SIZE-1:
            return(True)
        else:
            return(False)

    # Get the next possible moves for any position
    def get_possible_moves(self, position):
        possible_moves = []
        x, y = position
        neighbor = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
        for each in neighbor:
            i, j = each
            if self.in_boundary((i, j)):
                possible_moves.append(each)
        return(possible_moves)

    # Get the position of any element
    def get_position(self, x):
        for i in range(ROW_SIZE):
            for j in range(ROW_SIZE):
                if self.data[i][j] == x:
                    return i, j

    # Get the next state after swaping the element
    def next_state(self):
        x, y = self.get_position(0)
        child = list()
        for each in self.get_possible_moves((x, y)):
            copy_state = copy.deepcopy(self.data)
            m, n = each
            copy_state[x][y], copy_state[m][n] = copy_state[m][n], copy_state[x][y]
            child.append(state(self.f, self.g+1, self, copy_state))
        return child