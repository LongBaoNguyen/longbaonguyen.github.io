"""

In this file, you need to:
    
- implement getStartState
- isGoalState
- getSuccessors

See the Problem Specification worksheet. 
"""



class EightPuzzleSearchProblem:
    """
      Implementation of a SearchProblem for the  Eight Puzzle domain

      Each state is represented by an instance of an eightPuzzle.
    """
    def __init__(self, puzzle):
        "Creates a new EightPuzzleSearchProblem which stores search information."
        # TODO: initialize self.puzzle which is initial state of the problem
        self.puzzle = puzzle

    def getStartState(self):
        # TODO: return initial state of the problem
        return self.puzzle

    def isGoalState(self, state):
        # TODO: return whether the given state is the goal state(see State class)
        return state.isGoal()

    def getSuccessors(self, state):
        """
          Returns list of (successor, action) pairs where
          each successor is either left, right, up, or down
          from the given state 
        """
        # TODO implement this function(see pseudocode from Problem Specification worksheet)
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a))
        return succ


    
