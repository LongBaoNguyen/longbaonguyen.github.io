/*
  For this Board class, implement:
  1) constructor
  2) nonEmptyCell method
  3) selectCell method
  4) part of checkWin method
  You do not need to implement the drawBoard method. 

*/

public class Board{
  int[][] grid;
  int moves; // total number of moves
  
  public Board(int rows, int cols){
    // initialize 2D array of ints, initially all 0(empty cell)

    // initialize moves = 0

  }
  /* Returns the largest row(top row of board is row 0) in the given 
     column that is nonempty. Return -1 if column is full. 
  */
  public int nonEmptyCell(int col){
    // start at the last row, MUST use while loop to traverse up
    // until it reaches an empty cell.


  
  }
  /* The given player attempts to play in the given column.
     Returns true if play was successful(at least one empty cell in the column)
     and false otherwise(column is full). 
  */
  public boolean selectCell(int player, int col){   
    // call nonEmptyCell above and save returned value in row variable.
    
    // if row != -1, set location to player, increase moves and return true

    
    
    // otherwise return false
    
  }
  /* Returns: 
    a) 0 if draw, 
    b) -1 if game still in progress(no winner yet)
    c) player(1 or 2) if that player has won
  */
  public int checkWin(){
    for(int row = 0; row < grid.length; row++){
      for(int col = 0; col < grid[0].length; col++){
        int value = grid[row][col];
        // if current cell is nonempty
        if(value != 0){
          // check from current plus 3 cells to the right
          // make sure going right 3 cells doesn't go out of bounds
          if(col < grid[0].length - 3 && grid[row][col + 1] == value
            && grid[row][col + 2] == value && grid[row][col + 3] == value)
            return value;
          
          // check from current plus 3 cells down
          // make sure going down by 3 cells doesn't go out of bounds
          // fill in this code here(see the previous conditional)
          
          
          
          
          
          // check from current plus 3 cells diagonal to the right
          // make sure going diagonal to the right doesn't go out of bounds
          if(col < grid[0].length - 3 && row < grid.length - 3
            && grid[row + 1][col + 1] == value && grid[row + 2][col + 2] == value 
            && grid[row + 3][col + 3] == value)
            return value;
            
            
            
          // check from current plus 3 cells diagonal to the left
          // make sure going diagonal to the left doesn't go out of bounds
          // fill in code here(see previous conditional)

        } 
      }
    }
    if(moves == 42){
      return 0; // full, no winner = draw
    }
    return -1;  // no winner yet, game still not over
  }

  // draw board, you do not need to implement this method
  public void drawBoard(){
    strokeWeight(2);
    stroke(0);
    
    // use for loop to draw horizontal lines
    // use line(begin_x, begin_y, end_x, end_y)
    for(int i=1;i<=5;i++)
      line(0,100*i,700,100*i);
     
    // use for loop to draw vertical lines
    // use line(begin_x, begin_y, end_x, end_y)
    for(int i=1;i<=6;i++)
      line(100*i,0,100*i,600);
    
    
    // use nested loop to traverse grid 2D array
    // for each nonempty cell, draw red circle if 1
    // and yellow circle if 2
    for(int i = 0; i < grid.length; i++){
      for(int j = 0; j < grid[i].length; j++){
        if(grid[i][j] == 1){
          // draw red circle
          fill(255, 0, 0);
          ellipse(j*100 + 50, i*100 + 50, 100, 100);
        }
        else if(grid[i][j] == 2){
          // draw yellow circle
          fill(255, 255, 0);
          ellipse(j*100 + 50, i*100 + 50, 100, 100);
        }
        
      }
    }
  }
  
}
