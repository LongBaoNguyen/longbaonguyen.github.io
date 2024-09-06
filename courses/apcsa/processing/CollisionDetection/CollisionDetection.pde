/* In this lab, we will implement Sprite-Sprite collision detection. 
   This is the simple rectangle-rectangle collision.
   
   First modify Sprite to have an integer alpha instance variable(0-255).
   This variable represents the transparency of the Sprite. 0 means invisible(completely transparent)
   and 255 is completely opaque(no transparency). This is done with tinting. See comments in Sprite
   class in the display method.
   
   Create two Sprites, brick and player. 
   Set the alpha(transparency) level of brick to low(say 100).
   If player collide with brick, set brick to high(255).
   
   You can also create another brick with a low transparency just to show that the player
   drawn BEHIND(draw before) the brick can still be seen. 
*/

// declare Sprites



void setup(){
  size(800, 600);
  imageMode(CENTER);
  // initialize both Sprite objects using one of the constructors
  // set the alpha level of the brick to 100.
  

}

void draw(){
  background(255);
  // call update and display on the player object to update and display the Sprite objects
  // TRY: Draw the player BEFORE the brick so that the player is behind the brick
  // and if the brick's transparency low, you should be able to see the player
  // through the brick. 
  
  
  
  // call the static method check_for_collision from Geometry
  // if collide, set alpha to 255 else reset back to 100
  
  
  
  
  
  
  
  // NO CODE AFTER THIS LINE.

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
