// This lab will requires you to 
// detects basic collisions with a circle and a rectangle.

// declare a PImage object
// and variables to position/move object

PImage img;
float center_x, center_y;
float change_x, change_y;

// declare radius, position of circle

// declare width, height, position of rectangle

void setup(){
  size(800, 600);
  imageMode(CENTER);
  rectMode(CENTER);
  // initialize image by calling loadImage(filename)
  img = loadImage("character.png");
  center_x = width/2;
  center_y = height/2;
  change_x = 0;
  change_y = 0;
  
  
  // initialize width, height, position of rectangle


  // initialize radius, position of circle

}

void draw(){
  background(255);
  
  // draw image by using image(image, x, y)
  image(img, center_x, center_y);
  // update position
  center_x += change_x;
  center_y += change_y;
  
  
  // calculate distance from character to center of circle
  
  
  // if distance is less than or equal to radius
  // fill a certain color, else fill a different color
  // then draw the circle.
  
    
  
  // check if character is within rectangle
  // 2 checks: between left and right bounds and top and bottom bounds

  // if within rectangle, fill a certain color
  // else fill a different color
  // draw rect
  
    
  
}
void keyPressed(){
  if(keyCode == RIGHT)
    change_x = 5;
  else if(keyCode == LEFT)
    change_x = -5;
  else if(keyCode == UP)
    change_y = -5;
  else if(keyCode == DOWN)
    change_y = 5;
    
}

void keyReleased(){
  if(keyCode == RIGHT)
    change_x = 0;
  else if(keyCode == LEFT)
    change_x = 0;
  else if(keyCode == UP)
    change_y = 0;
  else if(keyCode == DOWN)
    change_y = 0;
    
}
// implement keyPressed and keyReleased
