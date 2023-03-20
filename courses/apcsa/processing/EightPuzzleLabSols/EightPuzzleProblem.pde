/* 
  IMPLEMENT THIS CLASS BY FILLING IN CODE ACCORDING TO THE COMMENTS.
  YOU WILL NEED TO IMPLEMENT the constructor, getStartState and isGoalState.


   A SearchProblem is a specification of the problem to be solved.
   It includes an initial state and a goal state as well as any variables necessary
   to describe the problem. 
   
   Every search problem must include the following interface:
   1) getStartState(): Returns the start state of the problem.
   2) isGoalState(State s): Returns whether state s is a goal state(to indicate if we have
   successfully solved the problem.
   3) and finally and most importantly, getSuccessors(Node n) which returns the successors
   of the given node n. This helps us expand a node by returning its neighbors or successors 
   in the breadth first search algorithm.
   
   The three methods above needs to be implemented for any search problem whether
   it's solving shortest paths in a maze, or solving Rubiks cube or the 8-puzzle problem.
   
*/

public class EightPuzzleProblem{
  State puzzle; // initial state of puzzle
  public EightPuzzleProblem(State init){
    puzzle = init;
  }
  
  // Returns the start state of the problem.
  public State getStartState(){
    // BEGIN CODE (about 1 line of code)
    return puzzle;
    // END CODE

  }
  
  // Returns whether state s is a goal state(to indicate if we have
  // successfully solved the problem.)
  public boolean isGoalState(State s){
    // BEGIN CODE (about 1 line of code)
    return s.isGoal();
    // END CODE

  }
  
  // returns the successors of the given node n. This helps us expand a node by 
  // returning its neighbors or successors. YOU DO NOT NEED TO IMPLEMENT THIS METHOD.
  public ArrayList<Node> getSuccessors(Node n){
    // BEGIN CODE (about 6 lines of code)
    // initialize arraylist of Nodes called successors
    ArrayList<Node> successors = new ArrayList<Node>();
    
    // initialize arraylist of Strings called legalMoves
    // by calling the appropriate method from the State class.

    ArrayList<String> legalMoves = n.state.legalMoves();
    
    /* for (each move in legalMoves)
          create new Node s which results from performing the move(action) on the current node
          add s to successors list
    */
    for(String move: legalMoves){
      Node s = new Node(n.state.result(move), n, move);
      successors.add(s);
    }
    // return successors
    return successors;
    // END CODE
  }
}
