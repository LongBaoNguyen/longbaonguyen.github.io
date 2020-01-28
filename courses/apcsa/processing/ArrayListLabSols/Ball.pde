/* 
You do not need to write code for this class. 
**/

public class Ball{
  float x, y;
  float radius;
  float change_x, change_y;
  color c; // c = color(255,0,0,) is red
            // c = color(255) is white
            
  // write the constructor that accepts one parameter(color) 
  // randomizing the ball's position, radius, change_x
  // change_y, you must use Math.random and Java casting
  // do not use Processing's random() and Processing casting
  public Ball(color c){
    x = (float)(Math.random() * width);  
    y = (float)(Math.random() * height);
    radius = (float)(Math.random() * 20) + 10;
    change_x = (float)(Math.random() * 20) - 10;
    change_y = (float)(Math.random() * 20) - 10;
    this.c = c;
  }
    
  // write the display() method to draw the ball
  public void display(){
    fill(c);
    ellipse(x, y, 2 * radius, 2 * radius);
  }

  
  // write the update() method to move the ball
  // and bounce if it hits the right/left edge

  public void update(){
    x += change_x;
    y += change_y;
    if(x >= width - radius){
      x = width - radius;
      change_x *= -1;
    }
    else if(x <= radius){
      x = radius;
      change_x *= -1;
    }
    
    if(y >= height - radius){
      y = height - radius;
      change_y *= -1;
    }
    else if(y <= radius){
      y = radius;
      change_y *= -1;
    }
  } 
}
