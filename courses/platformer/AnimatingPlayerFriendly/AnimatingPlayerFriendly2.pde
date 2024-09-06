/*
  Animating the Player Lab:
  
  In this lab, we will animate a player as he walks left and right.
  To keep things simple, we won't have jumping or any platform collisions.
    
  There are two versions of this lab:
  1) Friendly Version. More helper code is provided in lab template.
  2) More Challenging Version. Less helper code is provided.
  For more detail, see the tutorial: https://youtu.be/l7kKqx6puAo
   
  This is the more friendly version.
  
  Complete the code as indicated by the comments.
  Do the following:
  1) Implement the AnimatedSprite and Player class. 
  2) In draw, call display, update and updateAnimation on player. 
 
*/
final static float MOVE_SPEED = 4;

final static int NEUTRAL_FACING = 0; 
final static int RIGHT_FACING = 1; 
final static int LEFT_FACING = 2; 

PImage playerImage;
Player player;

void setup(){
  size(800, 600);
  imageMode(CENTER);
  playerImage = loadImage("player_stand_right.png");
  player = new Player(playerImage, 0.8);
  player.center_x = width/2;
  player.center_y = height/2;
}

void draw(){
  background(255);
  // TODO:
  // call display, update and updateAnimation on player.
  
  

}

// called whenever a key is pressed.
void keyPressed(){
  if(keyCode == RIGHT){
    player.change_x = MOVE_SPEED;
  }
  else if(keyCode == LEFT){
    player.change_x = -MOVE_SPEED;
  }
}

// called whenever a key is released.
void keyReleased(){
  if(keyCode == RIGHT){
    player.change_x = 0;
  }
  else if(keyCode == LEFT){
    player.change_x = 0;
  }
}
