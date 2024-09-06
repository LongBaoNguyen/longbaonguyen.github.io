/* This lab introduces you to the basics of animation in Processing. We will animate
a bouncing ball. 

See the following slides for an intro to Processing. 
https://longbaonguyen.github.io/courses/apcsa/processing/processing1.pdf

To do: 
    
    Drawing API:
    ellipse(x, y, width, height): (x, y) center of ellipse.
    rect(x, y, width, height): (x, y) top left corner of rectangle.
    line(x1, y1, x2, y2): line connecting (x1, y1) and (x2, y2)
    text(str, x, y): display str at location (x, y).
*/

// declare int variables x, y(do not initialize) for center of ball
// and velocities in each component: change_x, change_y(integers)

int x, y, change_x, change_y;

// declare a variable for the radius of the ball
int radius;


void setup(){
  // set size of window and initialize x, y, change_x, change_y, radius
  size(800, 600);
  x = 100;
  y = 200;
  change_x = 5;
  change_y = 3;
  radius = 50;
  
}

void draw(){
  background(255);
  // set the fill to red. Call fill(red, green, blue).
  // Then call ellipse(x, y, width, height)
  // to draw circle centered at (x, y) with diameter = 2 * radius
  fill(255, 0, 0);
  ellipse(x, y, 2 * radius, 2 * radius);
          
  // update the center by adding change_x and change_y to x and y respectively.
  x += change_x;
  y += change_y;
  
  
  // if right edge of ball passes right side of screen or 
  // left edge of ball passes left side of screen, negate change_x
  // Note: use radius in the conditional so that the ball bounces exactly at edge.
  if(x + radius > width || x - radius < 0)
    change_x *= -1;


  // if top edge of ball passes top side of screen or 
  // bottom edge of ball passes bottom side of screen, negate change_y
  // Note: use radius in the conditional so that the ball bounces exactly at edge.

  if(y + radius > height || y - radius < 0)
    change_y *= -1;

  
}
