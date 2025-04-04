"""

In this file, you need to implement:

- path function

Look for "TODO". 


"""
class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state.  
    
    """

    def __init__(self, state, parent=None, action=None):
        "Create a search tree Node, derived from a parent by an action."
        self.state = state
        self.parent = parent
        self.action = action


    def path(self):
        """
        Create a path of actions from the start to the current state
        """
        # TODO: Implement this function, see pseudocode from worksheet.
        # remove pass below before implementing code
        pass

    

    def get_neighbors(self, problem):
        """
        Return a list of nodes reachable from this node.
        """
        return [Node(next, self, act)
                for (next, act) in problem.getSuccessors(self.state)]
