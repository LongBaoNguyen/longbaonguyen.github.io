/* This lab introduces you to the basics of Processing including drawing
simple shapes, text and animation.  

See the following slides for an intro to Processing. 
https://longbaonguyen.github.io/courses/apcsa/processing/processing1.pdf

To do: 
    1) Draw a rectangle with top left corner at (100, 400) and width = 100, height = 300
    2) Draw a line connecting the top left corner and bottom right corner. 
    3) Display some text on the screen. Use the text() method.
    4) Print out some text on the console. Use the print() method. 
    4) Draw a small red circle with radius 20 and make it move to the right. 
    
    Drawing API:
    ellipse(x, y, width, height): (x, y) center of ellipse.
    rect(x, y, width, height): (x, y) top left corner of rectangle.
    line(x1, y1, x2, y2): line connecting (x1, y1) and (x2, y2)
    text(str, x, y): display str at location (x, y).
*/

// declare int variables x, y(do not initialize)


void setup(){
  // set size of window and initialize x and y

  
}

void draw(){
  background(255);
  // draw a blue rectangle with top left corner at (100, 400) and width = 100, height = 300
  strokeWeight(2);

  
  // draw a line connecting the top left corner and bottom right corner. 
  strokeWeight(3);

  
  // display some text on the screen. Use the text(str, x, y) method.
  textSize(32);
  fill(0); // black
  
  
  // print out some text on the console. Use the println() method. 

  
  // set the fill to red. Call fill(red, green, blue).
  // Then call ellipse(x, y, width, height)
  // to draw circle centered at (x, y) with diameter 20
  fill(255, 0, 0);
  strokeWeight(1);
        
          
  // update the center by adding 5 pixels to x every frame

}
