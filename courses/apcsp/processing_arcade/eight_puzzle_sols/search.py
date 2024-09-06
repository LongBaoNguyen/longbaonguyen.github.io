# YOU DO NOT NEED TO IMPLEMENT the graphSearch algorithm below. 
# Read the code. This is the breadth-first search implementation discussed in class.

# DO NOT MODIFY THIS FILE.


from __future__ import division, print_function
import random
from node import *


def graphSearch(problem):
    init = problem.getStartState()
    frontier = []
    frontier.append(Node(init))
    visited = []
    
    while len(frontier) != 0:
        s = frontier.pop(0)
        if problem.isGoalState(s.state):
            return s.path()
        inVisited = s.state in visited
        if not inVisited:
            visited.append(s.state)
            neighbors = s.expand(problem)
            for neighbor in neighbors:
                frontier.append(neighbor)
    return null
        
        
    
