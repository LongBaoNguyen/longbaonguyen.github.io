// Modify Sprite to have an integer alpha instance variable(0-255)
// Use tint(white_amount, alpha_amount) to simulate transparency.
// See the comments in the display method below.

public class Sprite{
  float center_x, center_y;
  float change_x, change_y;
  float w, h;
  PImage image; 
              // create integer variable alpha(transparency)
              // 255 is completely opaque, 0 is completely transparent(invisible).
              // initialize it to the default 255.
  Sprite(String filename){
    image = loadImage(filename);
    w = image.width;
    h = image.height;
    center_x = 0;
    center_y = 0;
    change_x = 0;
    change_y = 0;
  }
  Sprite(String filename, float scale){
    image = loadImage(filename);
    w = image.width * scale;
    h = image.height * scale;
    center_x = 0;
    center_y = 0;
    change_x = 0;
    change_y = 0;
  }
  Sprite(String filename, float scale, float x, float y){
    image = loadImage(filename);
    w = image.width * scale;
    h = image.height * scale;
    center_x = x;
    center_y = y;
    change_x = 0;
    change_y = 0;
  }
  void display(){
    // call tint() with two arguments 
    // Mix alpha against a white color(255) to simulate transparency
    // tint(255, 64) for example is about 75% transparency.
    
    // draw the image 
    
    
    // then untint it so that this does not apply to other objects.
    
  }
  void update(){
    center_x += change_x;
    center_y += change_y;
  }
  void setLeft(float left){
    center_x = left + w/2;
  }
  float getLeft(){
    return center_x - w/2;
  }
  void setRight(float right){
    center_x = right - w/2;
  }
  float getRight(){
    return center_x + w/2;
  }
  void setTop(float top){
    center_y = top + h/2;
  }
  float getTop(){
    return center_y - h/2;
  }
  void setBottom(float bottom){
    center_y = bottom - h/2;
  }
  float getBottom(){
    return center_y + h/2;
  }
}
