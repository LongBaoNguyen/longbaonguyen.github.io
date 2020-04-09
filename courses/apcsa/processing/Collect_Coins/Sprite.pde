// YOU DO NOT NEED TO MODIFY THIS CLASS.

public class Sprite{
  float center_x, center_y;
  float change_x, change_y;
  float w, h;
  PImage image; 
  
  public Sprite(String filename, float scale, float x, float y){
    image = loadImage(filename);
    w = image.width * scale;
    h = image.height * scale;
    center_x = x;
    center_y = y;
    change_x = 0;
    change_y = 0;
  }  
  public Sprite(String filename){
    this(filename, 1.0, 0.0, 0.0);
  }
  public Sprite(String filename, float scale){
    this(filename, scale, 0.0, 0.0);
  }
  public Sprite(PImage img, float scale){
    image = img;
    w = image.width * scale;
    h = image.height * scale;
    center_x = 0;
    center_y = 0;
    change_x = 0;
    change_y = 0;  
  }

  void display(){
    image(image, center_x, center_y, w, h);  
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
