// Ball Bounces Off Angles
// Adapted from Keith Peters' Algorithm 
// from his book Foundation HTML5 Animation with JavaScript.


// position, radius of the ball
float posx, posy;
float radius;

// velocity of the ball
float velx, vely;

// center, rotation and length of inclined segment.
float gx, gy, rot, len;

void setup(){
  size(600,600);
  //initialize variables.
  posx = 
  posy = 
  radius = 
  
  velx = 
  vely =
  
  // center of segment = midpoint of (0,400) and (width, height)
  gx = 
  gy = 
  
  // length and rotation of segment
  // use dist(x1,y1,x2,y2) to compute distance.
  // use atan2(dy, dx) for the rotation angle.
  len = 
  rot = 
}
  
void draw(){
  background(255);
  // fill and draw triangle(inclined ramp): (0,400), (width,height), (0, height)
  // use fill(r,g,b) and triangle(x1,y1,x2,y2,x3,y3)
  
  
  
  displayBall();
  moveBall();
  checkWallsCollision();  
  checkInclineCollision();

}

void displayBall(){
  // fill and draw circle(ball) at (posx,posy) with radius
  // use ellipse(x,y,2*radius,height)
  
  
}

void moveBall(){
  // move ball (optionally add GRAVITY)
  // add velocity to position
  
  
}

void checkWallsCollision(){
  // check if posx passes right wall
  // realign posx to right wall and change direction
  if(posx > width - radius){
    posx = width - radius;
    velx = -1*velx;
  }
   
  // check if posx passes left wall
  // realign posx to left wall and change direction
  if(posx < radius){
    posx = radius;
    velx = -1*velx;
  }
    

  
  // check if posy passes top wall
  // realign posy to top wall and change direction
  // fill in your code below
  if(       ){

  }
  
}

void checkInclineCollision(){
  // check incline collision and reverse direction
  // use coordinate rotation trick, see lecture video for more details. 
  
  // (dx, dy) is relative position of ball with respect to (gx,gy)
  float dx = 
  float dy = 
  
  
  // compute cosine, sine of rot angle, use Processing's cos() and sin().
  float cosine = 
  float sine = 
  
  
  // rotate (dx,dy) to new coordinate (dx_,dy_)
  // rotate (velx, vely) to (velx_,vely_)
  // see lecture video for the formulas
  // use rotation matrix 
  float dx_ = 
  float dy_ = 
  float velx_ = 
  float vely_ = 
  
  
  // once rotated, it is easy to see when to bounce
  // and how to bounce(negate vertical velocity in rotated coordinate)
  // remember to realign dy_ before bouncing
  if (           ) {
    
    
  }

  // rotate everything back to restore the original 
  // coordinate axis.
  dx = 
  dy = 
  velx = 
  vely = 
  
  // update posx and posy
  posx = 
  posy = 

}
