 /* 

YOU WILL NEED TO IMPLEMENT ONLY ONE METHOD OF THIS CLASS: expand. See below.

 
 A search algorithm explores a search tree over the state-space graph, 
 forming various paths from the initial state, trying to find a path that reaches a 
 goal state. Each node in the search tree corresponds to a state in the state space 
 and the edges in the search tree correspond to actions. An action when applied to a 
 node(parent) leads to a child or successor node. The root of the tree corresponds to the 
 initial state of the problem.
 
 A Node object consists of:
 1) a state 
 2) an action which when applied to the parent node leads to this node(child or successor node)
 3) a parent Node(node which generates this current node by the action)
 
 The interface to this class includes:
 
public ArrayList<String> path(): Returns arraylist of strings denoting the actions 
from initial state to the current(this) node. You will need to implement this methd below.

public ArrayList<Node> expand(EightPuzzleProblem problem): Given a Search problem, return
an arraylist of successors(children) of the current node. You will need to implement this method below.
 */

public class Node{
  State state;
  Node parent;
  String action;
  public Node(State s, Node p, String a){
    state = s;
    parent = p;
    action = a;
  }
  public Node(State s){
    this(s, null, "");
  }
  
  // Returns arraylist of strings denoting the actions 
  // from initial state to the current(this) node. YOU DO NOT NEED TO IMPLEMENT THIS METHOD.
  public ArrayList<String> path(){
    // BEGIN CODE (about 6 lines of code)
    
    // initialize arraylist of strings called actions
    ArrayList<String> actions = new ArrayList<String>();
    // initialize currentNode to be this node. Use "this" keyword.
    Node currentNode = this;
    
    /* while (currentNode's parent is not null)
           add currentNode's action to beginning(index 0) of actions list
           set currentNode to currentNode's parent
    */
    while(currentNode.parent != null){
      actions.add(0, currentNode.action);
      currentNode = currentNode.parent;
    }
    
    // return actions list
    return actions;
    // END CODE
  }
  
  // Given a Search problem, return an arraylist of successors(children) of 
  // the current node. 
  public ArrayList<Node> expand(EightPuzzleProblem problem){
    // BEGIN CODE (about 2 lines of code)
    
    // initialize arraylist of Nodes and set it equal to the result of calling getSuccessors
    // method from the EightPuzzleProblem class. 
    ArrayList<Node> nodes = problem.getSuccessors(this);
    
    // return nodes
    return nodes;
    // END CODE
  }
  
}
