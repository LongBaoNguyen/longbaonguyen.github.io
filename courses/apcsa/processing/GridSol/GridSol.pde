/*
  Grid Lab.
*/


// declare currentPlayer variable(0 = red, 1 = green)
int currentPlayer;
Board board;

void setup()
{
  size(700,600);
  // initialize currentPLayer, default first player is red
  currentPlayer = 0;
  // initialize board to have 6 rows 7 columns 
  board = new Board(6, 7);
  
}

void draw(){
  background(255);
  // call drawBoard() on board object.
  board.drawBoard();

}

void mouseClicked(){
// mouseClicked is called when the mouse is clicked
// the variable mouseX and mouseY is the coordinate of where mouse was clicked

  // use mouseX, mouseY to compute row and column of Cell.
  int row = mouseY / 100;
  int col = mouseX / 100;
  
  // if Cell at row and col is empty, call selectCell
  // with currentPlayer and row and col to set Cell
  // call updatePlayer() to update currentPlayer.
  if(board.grid[row][col].isEmpty){
    board.selectCell(currentPlayer, row, col);
    updatePlayer();
  }
  
}
    
void updatePlayer(){
  // update currentPlayer variable.
  // if 0 then 1, conversely if 1 then 0.
  currentPlayer++;
  currentPlayer %= 2;
}
