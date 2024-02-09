"""

In this file, you need to implement:
    
- graphSearch

Look for "TODO". 

"""


from __future__ import division, print_function
import random
from node import *


def graphSearch(problem):
    frontier = [] # list of nodes
    visited = []  # list of states
    
    init = problem.getStartState()
    frontier.append(Node(init, None, None))
    
    while len(frontier) != 0:
        # TODO:
        # remove first node(index 0) from frontier list, call it s
        s = frontier.pop(0)
        
        # TODO:
        # if state of s is goal state:
        #      return path from initial to this goal state s
        if problem.isGoalState(s.state):
            return s.path()
        
        
        inVisited = s.state in visited
        if not inVisited:
            visited.append(s.state)
            neighbors = s.get_neighbors(problem)
            
            # TODO:
            # for each neighbor in list of neighbors:
            #      append neighbor to frontier list
            for neighbor in neighbors:
                frontier.append(neighbor)
    # if this point is reached, frontier list is empty and no path was found
    return None
        
        
    
