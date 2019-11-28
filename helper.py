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


class Puzzle():

    def __init__(self, start_data, goal_data):
        self.open = list()
        self.priority_queue = []
        self.start = start_data
        self.goal = goal_data
        self.initial_state = self.convert_2D(start_data)
        self.goal_data_list = [i for i in range(0, PUZZLE_TYPE + 1)]
        self.goal_state = self.convert_2D(self.goal_data_list)
        self.path = [] 
        self.execution = 0
        self.count = 0

    # Convert list of initial state to 2D
    def convert_2D(self, puzzle):
        puzzle_2D = []
        row = []
        for idx, val in enumerate(puzzle):
            row.append(val)
            if (idx + 1) % ROW_SIZE == 0:     
                puzzle_2D.append(row)
                row = []
        return state(0, 0, None, puzzle_2D)

    # Calculate manhattan as heuristic
    def manhattan(self, input_data):
        distance = 0
        for i in range(ROW_SIZE):
            for j in range(ROW_SIZE):
                if input_data[i][j] != self.goal_state.data[i][j] and input_data[i][j] != 0:
                    A = self.goal_data_list.index(input_data[i][j])
                    x, y = divmod(A, ROW_SIZE)
                    distance += abs(x - i) + abs(y - j)
        return distance

    # Calculate no of misplaced tiles as heuristic
    def misplaced_tiles(self, input_data):
        counter = 0
        for i in range(ROW_SIZE):
            for j in range(ROW_SIZE):
                if input_data[i][j] != self.goal_state.data[i][j] and input_data[i][j] != 0:
                    counter += 1
        return counter

    # Calculate the cost 
    def f_val(self, g, h):
        f_n = g + h
        return(f_n)

    # Convert 2D array to a list
    def array2D_to_tuple(self, data):
        new_list = []
        for i in data:
            for j in i:
                new_list.append(j)
        return tuple(new_list)