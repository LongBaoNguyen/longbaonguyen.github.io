public class Board{
  // declare 2D array of Cell objects.
  private Cell[][] grid;
  
  public Board(int row, int col){
    // initialize 2D array of Cell objects(null)
    grid = new Cell[row][col];
    
    // use nested loop to initialize each Cell
    for(int i = 0;i < grid.length;i++)
      for(int j = 0;j < grid[0].length;j++)
        grid[i][j] = new Cell();
  }
  public void selectCell(int player, int row, int col){
    // if Cell at row, col is empty
    // set player and isEmpty variable
    if(grid[row][col].isEmpty){
      grid[row][col].setPlayer(player);
      grid[row][col].isEmpty = false;
    }   
  }
  
  public void drawBoard(){
    // this is the trickiest part of the lab.
    // draw horizontal lines and vertical lines
    strokeWeight(2);
    stroke(0);
    
    // use for loop to draw horizontal lines
    for(int i = 1;i < 6;i++)
      line(0,100 * i,700,100 * i);
    
    // use for loop to draw vertical lines
  
    for(int i= 1;i < 7;i++)
      line(100 * i,0,100 * i,600);
      
    // use nested loop to traverse grid 2D array
    // for each nonempty cell, draw red circle if 0
    // and green circle if 1
    for(int i = 0;i < grid.length;i++){
      for(int j = 0;j < grid[0].length;j++){
        if(!grid[i][j].isEmpty && grid[i][j].getPlayer() == 0){
          fill(255,0,0);
          ellipse(100 * j + 50,100 * i + 50,100,100);
        }
        else if(!grid[i][j].isEmpty && grid[i][j].getPlayer() == 1){
          fill(0,255,0);
          ellipse(100 * j + 50,100 * i + 50,100,100);
        }
          
      }
     }
  
  }
}
