/*
  Collect Coins Lab:
  
  Coins are placed randomly on the screen. Player moves around and collect coins.
  The number of coins is updated and displayed on the screen.
  
  For more detail, see the video tutorial: https://youtu.be/RMmo3SktDJo
  OR slides tutorial: https://longbaonguyen.github.io/courses/apcsa/processing/processing3.pdf

   
   
  Complete the code as indicated by the comments.
  Do the following:
  1) In setup, initialize arraylist of coins. Then use a loop to create coin Sprites and placed them
  randomly on the screen. Add each coin to arraylist.
  2) In draw, for loop to display each coin. 
  3) Now, implement checkCollision and checkCollisionList. 
  4) In draw, call checkCollisionList with parameters player and list of coins to get collision list.
  Loop through collision list and remove them and update score. 
  5) In draw, display score using textSize(), fill() and text().
  
  See the comments below for more details. 
 
*/

final static float MOVE_SPEED = 4;
final static float COIN_SCALE = 0.4;
final static float TANK_SCALE = 0.8;


Sprite player;
ArrayList<Sprite> coins; 
int score;

void setup(){
  size(1024, 768);
  imageMode(CENTER);
  // initialize player Sprite by calling constructor; use TANK_SCALE for scaling factor

  // initialize score

  // initialize the arrayList coins
  
  
  // for loop to create coin Sprite and add to coins arraylist
  // randomize their center_x and center_y(use MATH.random() and cast to float)

  
  
  
  
}

void draw(){
  background(255);
  // display player 
  
  // update player
  
  // use for each loop to display coins

  
  
  // call checkCollisionList and 
  // store the returned collision list(arraylist) of coin Sprites that collide with player.
  // if collision list not empty
  //   for loop through collision list
  //     remove each coin, add 1 to score

  
  
  
  
  // call textSize(size), fill(r, g, b) and text(str, x, y) to display score. 
  textSize(32);
  fill(255, 0, 0);
  // fill in score below
  text("Coins:", 50, 50);
}

// returns whether the two Sprites s1 and s2 collide.
public boolean checkCollision(Sprite s1, Sprite s2){
  // fill in code here.
  // or slides: https://longbaonguyen.github.io/courses/apcsa/processing/processing3.pdf
  
  
}

/**
   This method accepts a Sprite s and an ArrayList of Sprites and returns
   the collision list(ArrayList) which consists of the Sprites that collide with the given Sprite. 
   MUST CALL THE METHOD checkCollision ABOVE!
*/ 
public ArrayList<Sprite> checkCollisionList(Sprite s, ArrayList<Sprite> list){
  // fill in code here
  // or slides: https://longbaonguyen.github.io/courses/apcsa/processing/processing3.pdf
  
  // First create an empty arraylist, populate it appropriately, then return it. 
  
}


  
void keyPressed(){
  if(keyCode == RIGHT)
    player.change_x = MOVE_SPEED;
  else if(keyCode == LEFT)
    player.change_x = -MOVE_SPEED;
  else if(keyCode == UP)
    player.change_y = -MOVE_SPEED;
  else if(keyCode == DOWN)
    player.change_y = MOVE_SPEED;
}

void keyReleased(){
  if(keyCode == RIGHT)
    player.change_x = 0;
  else if(keyCode == LEFT)
    player.change_x = 0;
  else if(keyCode == UP)
    player.change_y = 0;
  else if(keyCode == DOWN)
    player.change_y = 0;
    
}
