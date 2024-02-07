# IMPLEMENT the check_for_collision function below

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
        
        
    
