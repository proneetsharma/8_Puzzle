#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import timeit
from helper import *




if __name__ == '__main__':       

    goal_state_list = [i for i in range(0, PUZZLE_TYPE + 1)]

    opt = int(sys.argv[1])
    if opt == 1 or opt == 2:

        if opt ==1:
            print("\nRunning A star search with Manhattan Dist heuristic\n")
            file_name = "A_star_manhattan"

        else:
            print("\nRunning A star search with Misplaced Tiles heuristic\n")
            file_name = "A_star_misplaced_tiles"


        puzzle_8 = [0, 1, 2, 3, 4, 5, 8, 6, 7] # Initial Configuration for testing
        print("Initial Configuration")
        board = Puzzle(puzzle_8, goal_state_list)
        Astar_search(board)
        board.write_to_file(file_name+"1")