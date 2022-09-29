/* This lab introduces you to the basics of animation in Processing. We will animate
a bouncing ball. 

See the following slides for an intro to Processing. 
https://longbaonguyen.github.io/courses/apcsa/processing/processing1.pdf

*/

// declare int variables x, y(do not initialize) for center of ball
// and velocities in each component: change_x, change_y(integers)
int x, y;

// declare a variable for the radius of the ball


void setup(){
  // set size of window and initialize x, y, change_x, change_y, radius
  size(800, 600);
  x = width / 2;
  y = height / 2; // width and height are reserved variables representing
                  // width and height of screen(in this case, 800, 600)
  
}

void draw(){
  background(255);
  // set the fill to red. Call fill(red, green, blue).
  // Then call ellipse(x, y, width, height)
  // to draw circle centered at (x, y) with diameter = 2 * radius
  
  
          
  // update the center by adding change_x and change_y to x and y respectively.

  
  
  // if right edge of ball passes right side of screen or 
  // left edge of ball passes left side of screen, negate change_x
  // Note: use radius in the conditional so that the ball bounces exactly at edge.
  // Hint: Use width variable



  // if top edge of ball passes top side of screen or 
  // bottom edge of ball passes bottom side of screen, negate change_y
  // Note: use radius in the conditional so that the ball bounces exactly at edge.
  // Hint: Use height variable


  
}
