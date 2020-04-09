/*
  Collect Coins Lab
  
  Coins are placed randomly on the screen. Player moves around and collect coins.
  The number of coins is updated and displayed on the screen.
  
  1) In setup, initialize arraylist of coins. Then use a loop to create coin Sprites and placed them
  randomly on the screen. Add each coin to arraylist.
  2) In draw, for loop to display each coin. 
  3) Now, implement checkForCollisionWithList in the Geometry module. 
  This method accepts a Sprite and a list of Sprites and return an arrayList of Sprites that 
  collide with the given Sprite. 
  4) In draw, call checkForCollisionWithList with parameters player and list of coins to get collision list.
  Loop through collision list and remove them and update score. 
  5) In draw, display score using textSize(), fill() and text().
  
  See the comments below for more details. 
 
*/

Sprite player;
ArrayList<Sprite> coins; 
int score;


float CHARACTER_SCALE = 0.8;
float COIN_SCALE = 0.5;

void setup(){
  size(1024, 768);
  imageMode(CENTER);
  player = new Sprite("tank.png", CHARACTER_SCALE);

  // initialize score
  
  // initialize the arrayList coins

  
  // for loop to create coin Sprite and add to coins arraylist
  // randomize their center_x and center_y(MUST USE MATH.random() and cast to float)

  
}

void draw(){
  background(255);
  player.display();
  player.update();
  
  // use for each loop to display coins

  
  
  // call checkForCollisionWithList from the Geometry module
  // store the returned collision list(arraylist) of coin Sprites that collide with player.
  // if collision list not empty
  //   for loop through collision list
  //     remove each coin, add 1 to score

  
  
  
  
  // call textSize(size), fill(r,g,b) and text(str, x, y) to display score. 
    

    
}

  
void keyPressed(){
  if(keyCode == RIGHT)
    player.change_x = 5;
  else if(keyCode == LEFT)
    player.change_x = -5;
  else if(keyCode == UP)
    player.change_y = -5;
  else if(keyCode == DOWN)
    player.change_y = 5;
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
