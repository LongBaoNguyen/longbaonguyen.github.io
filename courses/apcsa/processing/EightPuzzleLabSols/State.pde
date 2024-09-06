/* 

   YOU WILL NEED TO IMPLEMENT ONLY ONE METHOD OF THIS CLASS: isGoal. See below.
   
   
   Read the documentation of this class as you will need to understand how to use it. 
   You do not need to understand all the details of the implementation. 
   
   
A 8-puzzle can be in one of many states or configurations of the board. 

A state is a 2D array denoting the positions of the numbers. The number 0
denote the space. The variables blankRow and blankCol denotes the position of the space
in the 2D array. The interface to this class contains the following methods:

- boolean isGoal(): Returns whether the current state(this state) is the solved position.
PLEASE IMPLEMENT THIS METHOD BELOW.

- String getMove(int row, int col): Given (row, col), move the square in that direction. 
This is used for human-mode; space will be moved according to position of mouse clicks.

- ArrayList<String> legalMoves(): Returns arraylist of strings which denote the legal moves
(up, down, left, right) from the current state. 

- State result(String move): Give a string denoting a move, returns a new State obtained 
after applying the move. 

- boolean equals(Object other): Returns whether this state equals the other state.


*/


public class State{
  int[][] cells;
  int blankRow, blankCol;
  // Precondition: numbers has length 9, numbers 0,1,2,..,8
  public State(int[] numbers){
    cells = new int[3][3];
    int index = 0;
    for(int row = 0; row < 3; row++){
      for(int col = 0; col < 3; col++){
        cells[row][col] = numbers[index];
        index++;
        if(cells[row][col] == 0){
          blankRow = row;
          blankCol = col; 
        }
      }
    }
  }
  
  // Returns whether the current state(this state) is the solved position.
  // IMPLEMENT THIS METHOD
  public boolean isGoal(){
    int[] goal = {1, 2, 3, 4, 5, 6, 7, 8, 0};
    // use nested loop to traverse the 2d array in row major order
    // to check if the numbers occur in the order given by the 1d array called goal.
    int index = 0;
    for(int row = 0; row < 3; row++){
      for(int col = 0; col < 3; col++){
        if(cells[row][col] != goal[index]){
          return false;
        }
        index++;
      }
    }
    return true;
  }
  
  // Given (row, col), move the square in that direction. 
  // This is used for human-mode; space will be moved according to position of mouse clicks.
  public String getMove(int row, int col){
    boolean sameRow = row == blankRow;
    boolean sameCol = col == blankCol;
    if(sameRow != sameCol){
      if(row < blankRow){
        return "up";
      }
      else if(row > blankRow){
        return "down";
      }
      else if(col < blankCol){
        return "left";
      }
      else if(col > blankCol){
        return "right";
      } 
    }
    return "";
  }
  
  // Returns arraylist of strings which denotes the legal moves
  // (up, down, left, right) from the current state. 
  public ArrayList<String> legalMoves(){
    ArrayList<String> moves = new ArrayList<String>();
    if(blankRow != 0){
      moves.add("up");
    }
    if(blankRow != 2){
      moves.add("down");
    }
    if(blankCol != 0){
      moves.add("left");
    }
    if(blankCol != 2){
      moves.add("right");
    }
    return moves;
  }
  
  // Give a string denoting a move, returns a new State obtained 
  // after applying the move. 
  public State result(String move){
    int[] a = {0,0,0,0,0,0,0,0,0};
    State result = new State(a);
    for(int row = 0; row < 3; row++){
      for(int col = 0; col < 3; col++){
        result.cells[row][col] = cells[row][col];
      }
    }
    int newRow = 0, newCol = 0;
    if(move.equals("up")){
      newRow = blankRow - 1;
      newCol = blankCol;
    }
    else if(move.equals("down")){
      newRow = blankRow + 1;
      newCol = blankCol;
    }
    else if(move.equals("left")){
      newRow = blankRow;
      newCol = blankCol - 1;
    }
    else if(move.equals("right")){
      newRow = blankRow;
      newCol = blankCol + 1;
    }
    
    result.cells[blankRow][blankCol] = cells[newRow][newCol];
    result.cells[newRow][newCol] = cells[blankRow][blankCol];
    result.blankRow = newRow;
    result.blankCol = newCol;
    return result;

  }
  
  // Returns whether this state equals the other state.
  public boolean equals(Object other){
    State a = (State)(other);
    for(int row = 0; row < 3; row++){
      for(int col = 0; col < 3; col++){
        if(cells[row][col] != a.cells[row][col]){
          return false;
        }
      }
    }
    return true;
  }

}
