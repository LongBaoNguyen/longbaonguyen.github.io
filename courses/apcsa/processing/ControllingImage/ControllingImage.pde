// This lab will requires you to 
// load an image and move it using the keyboard

// declare a PImage object
// and variables to position/move object
PImage img;
int centerX, centerY;
int changeX, changeY;

void setup(){
  size(800, 600);
  imageMode(CENTER);
  // initialize image by calling loadImage(filename)
  img = loadImage("character.png");
  centerX = width/2;
  centerY = height/2;
  changeX = 0;
  changeY = 0;
}

void draw(){
  background(255);
  // draw image by using image(image, x, y)
  image(img, centerX, centerY);
  // update position
  centerX += changeX;
  centerY += changeY;
  
}

// implement keyPressed and keyReleased

void keyPressed(){
  if(keyCode == RIGHT){
  
  }
  if(key == 'a'){
    
  }
  
}

void keyReleased(){
}
