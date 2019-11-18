// This lab will requires you to 
// load an image and move it using the keyboard

// declare a PImage object
// and variables to position/move object

PImage img;
float center_x, center_y;
float change_x, change_y;


void setup(){
  size(800, 600);
  imageMode(CENTER);
  img = loadImage("character.png");
  center_x = width/2;
  center_y = height/2;
  
  change_x = 0;
  change_y = 0;
  // initialize image by calling loadImage(filename)
  
  


}

void draw(){
  background(255);
  
  // draw image by using image(image, x, y)
  image(img, center_x, center_y);
  // update position
  
  center_x += change_x;
  center_y += change_y;
  
  
}

// implement keyPressed and keyReleased
