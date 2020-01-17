/* In this lab, we will implement Sprite-Sprite collision detection. 
   This is the simple rectangle-rectangle collision.
   
   First modify Sprite to have an integer alpha instance variable(0-255).
   This variable represents the transparency of the Sprite. 0 means invisible(completely transparent)
   and 255 is completely opaque(no transparency). This is done with tinting, see comments
   from the Sprite class. 
   
   Create two Sprites, brick and player. 
   Set the alpha(transparency) level of brick to low(say 100).
   If player collide with brick, set brick to high(255).
   
   You can also create another brick with a low transparency just to show that the player
   drawn BEHIND(draw before) the brick can still be seen. 
*/


Sprite player;
Sprite brick1, brick2;

void setup(){
  size(600, 600);
  imageMode(CENTER);
  // initialize Sprite object using one of the constructors
  // set the alpha level of the brick to 100.
  player = new Sprite("character.png", 1.0, width/4.0, height/4.0);
  brick1 = new Sprite("brick.png", 1.0, 3*width/4.0, height/2.0);
  brick1.alpha = 100;
  brick2 = new Sprite("brick.png", 1.0, width/2.0, height/2.0);

  

}

void draw(){
  background(255);
  // call update and display on the player object to update and display the Sprite objects
  player.update();
  player.display();
  brick1.display();
  brick2.display();

  
  
  // call the static method check_for_collision from Geometry
  // if collide, set alpha to 255 else reset back to 100
  if(Geometry.check_for_collision(player, brick2)){
    brick2.alpha = 255;  
  }
  else{
    brick2.alpha = 100;
  }
  
  
  // add logic here so that the Sprite never leaves the screen.
  // Hint: Use conditional and the setLeft, setRight...etc methods
  // if your character glitches at the screen edge, you didn't do it correctly.
  if(player.getRight() >= width)
    player.setRight(width);
  if(player.getLeft() <= 0)
    player.setLeft(0);
  if(player.getTop() <= 0)
    player.setTop(0);
  if(player.getBottom() >= height)
    player.setBottom(height);
    
    
    
  
  
  
}

// implement keyPressed so that pressing the arrow keys will move the Sprite
// this is the same as the previous lab with some minor changes.
void keyPressed(){
  if(keyCode == RIGHT)
    player.change_x = 6;
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
