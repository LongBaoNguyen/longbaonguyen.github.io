class EightPuzzleSearchProblem:
    """
      Implementation of a SearchProblem for the  Eight Puzzle domain

      Each state is represented by an instance of an eightPuzzle.
    """
    def __init__(self, puzzle):
        "Creates a new EightPuzzleSearchProblem which stores search information."
        self.puzzle = puzzle

    def getStartState(self):
        return self.puzzle

    def isGoalState(self, state):
        return state.isGoal()

    def getSuccessors(self, state):
        """
          Returns list of (successor, action) pairs where
          each successor is either left, right, up, or down
          from the given state 
        """
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a))
        return succ


    
