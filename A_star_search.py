#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import timeit
from helper import *
import time


def Astar_search(board):
    """Function to implement the A-star search algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    board : [type]
        [description]
    opt : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    counter = 0
    start = board.initial_state
    visited = set()

    if opt == 1:
        start.f = board.manhattan(start.data)
    elif opt == 2:
        start.f = board.misplaced_tiles(start.data)

    # Push f value, counter and class
    heappush(board.priority_queue, (start.f, counter, start))

    start_time = timeit.default_timer()
    while len(board.priority_queue):

        # Initializing current node
        current = heappop(board.priority_queue)[-1]
        visited.add(board.array2D_to_tuple(current.data))

        # Incrementing count to check No of explored node.
        board.count += 1

        # Check if goal reached or not.
        if opt == 1:
            if(board.manhattan(current.data) == 0):  
                print("Goal Node Reached!")
                break  
        if opt == 2:            
            if(board.misplaced_tiles(current.data) == 0):  
                print("Goal Node Reached!")
                break        

        children = current.next_state()
        for each in children:
            # Check if node is visited or not.
            if board.array2D_to_tuple(each.data) not in visited:
                counter += 1
                if opt == 1:
                    # Update the value of heuristic and apeend to heap
                    each.f = board.f_val(each.g, board.manhattan(each.data))
                    heappush(board.priority_queue, (each.f, counter, each))       
                elif opt == 2: 
                    each.f = board.f_val(each.g, board.misplaced_tiles(each.data))
                    heappush(board.priority_queue, (each.f, counter, each))       
  
    board.path_cost = current.g                 
    end_time = timeit.default_timer()
    board.execution = end_time - start_time 

    # Backpropagating 
    while current.parent != None:
        board.path.append(current)
        current = current.parent
    board.path.append(current)
    board.path.reverse()


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


        puzzle_8 = [8, 7, 6, 5, 1, 4, 2, 0, 3] # Second Configuration for testing
        print("Second Configuration")
        board = Puzzle(puzzle_8, goal_state_list)
        Astar_search(board)
        board.write_to_file(file_name+"2")


        puzzle_8 = [1, 5, 7, 3, 6, 2, 0, 4, 8] # Final Configuration for testing
        print("Final Configuration")
        board = Puzzle(puzzle_8, goal_state_list)
        Astar_search(board)
        board.write_to_file(file_name+"3")

    else:
        print("Invalid Choice")
