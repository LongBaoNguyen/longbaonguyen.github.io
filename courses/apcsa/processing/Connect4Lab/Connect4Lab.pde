 /*
  Connect 4 Lab.
  Follow the comments below to fill in the code. 
  You will also need to fill in code for the Board class. 
*/
 

// declare currentPlayer variable(1 = red, 2 = yellow)
int currentPlayer;
Board board;
boolean gameOver;

void setup()
{
  size(700,600);
  // initialize currentPLayer, default first player is red = 1

  gameOver = false;
  // initialize board to have 6 rows 7 columns 

}

void draw(){
  background(255);
  // call drawBoard() on board object.
  board.drawBoard();
  
  // call checkWin and store returned value in winner variable.
  
  if(winner != -1){
    gameOver = true;
  }
  if(gameOver){
    String playerWinner = "";
    if(winner == 1)
      playerWinner = "red";
    else if(winner == 2)
      playerWinner = "yellow";
    fill(0);
    textSize(30);
    if(winner != 0){
      text("Winner is ", width/3, height/2);
    }
    else
      text("Draw", width/3, height/2);
    text("Press space to reset.", width/3, height/2 + 30);
  }

}



/* mouseClicked is called when the mouse is clicked
   the variable mouseX and mouseY is the coordinate of where mouse was clicked
*/
void mouseClicked(){
  if(!gameOver){
    // use mouseX to compute column of the selected location
    int col = mouseX / 100;
    // attempt to call selectCell with currentPlayer and col
    // if selectCell is successful, switch player(call switchPlayer below)


  }
}
// switch currentPlayer
void switchPlayer(){
  if(currentPlayer == 1)
    currentPlayer = 2;
  else 
    currentPlayer = 1;
}
void keyPressed(){
  // if gameOver and press space, reset game.
  if(gameOver && key == ' '){
    setup();
  }
  
}
   
