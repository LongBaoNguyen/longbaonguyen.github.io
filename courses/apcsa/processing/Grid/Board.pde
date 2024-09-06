public class Board{
  // declare 2D array of Cell objects.
  Cell[][] grid;
  
  public Board(int rows, int cols){
    // initialize 2D array of Cell objects(null)

    
    
    // use nested loop to initialize each Cell(use new Cell())


  }
  public void selectCell(int player, int row, int col){
    // if Cell at row, col is empty
    //     set player and update isEmpty variable to false



  }
  
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
    // for each nonempty cell, draw red circle if 0
    // and green circle if 1
    for(int i = 0; i < grid.length; i++){
      for(int j = 0; j < grid[i].length; j++){
        if(!grid[i][j].isEmpty && grid[i][j].getPlayer() == 0){
          // draw red circle
          fill(255, 0, 0);
          ellipse(j*100 + 50, i*100 + 50, 100, 100);
        }
        else if(!grid[i][j].isEmpty && grid[i][j].getPlayer() == 1){
          // draw red circle
          fill(0, 255, 0);
          ellipse(j*100 + 50, i*100 + 50, 100, 100);
        }
        
      }
    }
  }
}
