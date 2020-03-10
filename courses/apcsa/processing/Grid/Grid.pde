/*
  Grid Lab.
*/


// declare currentPlayer variable(0 = red, 1 = green)
int currentPlayer;
Board board;

void setup()
{
  size(700,600);
  // initialize currentPLayer, default first player is red = 0
  
  // initialize board to have 6 rows 7 columns 

  
}

void draw(){
  background(255);
  // call drawBoard() on board object.

}

/* mouseClicked is called when the mouse is clicked
   the variable mouseX and mouseY is the coordinate of where mouse was clicked
*/
void mouseClicked(){
  // use mouseX, mouseY to compute row and column of Cell.

  
  
  // if Cell at row and col is empty, call selectCell
  // with currentPlayer and row and col to set Cell
  // call updatePlayer() to update currentPlayer.

  
  
}
    
void updatePlayer(){
  // update currentPlayer variable.
  // if 0 then 1, conversely if 1 then 0.



}
