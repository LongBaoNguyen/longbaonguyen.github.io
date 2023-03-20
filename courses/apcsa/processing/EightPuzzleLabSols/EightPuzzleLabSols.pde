

/* Implement the classes in the following order:
   1) State class
   2) Queue class.
   3) Node class.
   4) EightPuzzleProblem class.
   
   Then implement the breadth first search algorithm below(graphSearch). 
   
   Note: set AIMode below to false in setup() to play manually.
   
*/


import java.util.*;

State i, f;
EightPuzzleProblem problem;
boolean gameOver;
State puzzle;
int sizeSquare;
ArrayList<String> moves;

boolean AIMode;

//initialize them in setup().
void setup(){
  size(600, 600);
  sizeSquare = width/3;
  puzzle = createRandomPuzzle(50);
  gameOver = false;
  AIMode = false;
  problem = new EightPuzzleProblem(puzzle);
  moves = graphSearch(problem);
}

// modify and update them in draw().
void draw(){
  background(255);
  drawPuzzle(puzzle);
  if(puzzle.isGoal()){
    gameOver = true;
  }

  
  if(AIMode && frameCount % 60 == 0 && moves.size() != 0){
    puzzle = puzzle.result(moves.remove(0));
  }
  if(gameOver){
    fill(0, 0, 255);
    textSize(80);
    text("You win!", 10, height/2);
    text("Press 'r' to reset!", 10, height/2+100);

  }
  
} 

// returns a random puzzle(State object)
public State createRandomPuzzle(int numMoves){
  int[] goal = {1, 2, 3, 4, 5, 6, 7, 8, 0};
  State p = new State(goal);
  for(int i = 0; i < numMoves; i++){
    ArrayList<String> legalMoves = p.legalMoves();
    int rand = (int)(Math.random()*(legalMoves.size()));
    String randomMove = legalMoves.get(rand);
    p = p.result(randomMove);
  }
  return p;
}

public void drawPuzzle(State p){
  strokeWeight(8);
  fill(255, 0, 0);
  for(int i = 1; i < 3; i++){
    line(i*sizeSquare, 0, i*sizeSquare, height);
  }
  for(int i = 1; i < 3; i++){
    line(0, i*sizeSquare, width, i*sizeSquare);
  }
  for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
        if(p.cells[i][j] != 0){
          fill(255, 0, 0);
          textSize(80);
          text(p.cells[i][j], 100+j*200 - 20, 100+ i * 200 + 20);
        }
    }
  }
}


public ArrayList<String> graphSearch(EightPuzzleProblem p){
  // initialize init variable which is the start state of the puzzle problem p(1 line)
  State init = p.getStartState();
  
  Queue frontier = new Queue();
  frontier.push(new Node(init));
  ArrayList<State> visited = new ArrayList<State>();
  
  while(!frontier.isEmpty()){
    // create a Node s which is the first Node from the queue frontier(call pop).(1 line)
    Node s = frontier.pop();
    
    // if the state of node s is the puzzle's p goal state 
    // then return the path from the start to current node s (if block, one statement)
    if(p.isGoalState(s.state)){
      return s.path();
    }
    
    // has state of node s been visited?
    boolean inVisited = visited.contains(s.state);
    
    if(!inVisited){
      // add state of s to visited
      visited.add(s.state);
      
      // initialize neighbors arraylist which is the result of expanding node s. (1 line)
      ArrayList<Node> neighbors = s.expand(p);
      
      // for each loop through neighbors and push each neighbor node to frontier
      for(Node x : neighbors){
        frontier.push(x);
      }
    }
  }
  
  // if there is no solution, return null.
  return null;
  
}
void keyPressed(){
  if(key == 'r'){
    setup();
  }
}

void mouseClicked(){
  if(!AIMode){
  int row = mouseY/sizeSquare;
  int col = mouseX/sizeSquare;
  String m = puzzle.getMove(row, col);
  if(puzzle.legalMoves().contains(m)){
    puzzle = puzzle.result(m);
  }
  }
}
