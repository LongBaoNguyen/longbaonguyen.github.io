class Ball{
  float posx, posy;
  float radius;
  float velx, vely;
  float gravity = 0.05;
  
  Ball(float x, float y, float r){
    posx = x;
    posy = y;
    radius = r;
    velx = .5;
    vely = 0; 
  }
  void display(){
  // fill and draw ellipse(ball) at (posx,posy)
  fill(0,0,255);
  ellipse(posx, posy, 2*radius, 2*radius);
}
  void move(){
  // move ball
  // gravity
  vely = vely + gravity;
 
   
  posx = posx + velx;
  posy = posy + vely;
  
  
}
  void checkWallsCollision(){
  // check top and the two side walls only
  // reverse direction if collide
  if(posx > width - radius){
    posx = width - radius;
    velx = -0.8*velx;
  }
  if(posx < radius){
    posx = radius;
    // changes direction + damping: velocity reduces by 20%.
    velx = -0.8*velx; 
  }
    
  
}
void checkInclineCollision(Ground g){
  // check incline collision and reverse direction
  // use coordinate rotation trick, see lecture video for more details. 
  
  // (dx, dy) is relative position of ball with respect to (gx,gy)
  float dx = posx - g.x;
  float dy = posy - g.y;
  
  
  // compute cosine, sine of rot angle.
  float cosine = cos(g.rot);
  float sine = sin(g.rot);
  
  
  // rotate (dx,dy) to new coordinate (dx_,dy_)
  // rotate (velx, vely) to (velx_,vely_)
  // see lecture video for the formulas
  float dx_ = cosine * dx + sine * dy;
  float dy_ = cosine * dy - sine * dx;
  float velx_ = cosine * velx + sine * vely;
  float vely_ = -sine * velx + cosine * vely ;
  
  
  // once rotated, it is easy to see when to bounce
  // and how to bounce(negate vertical velocity in rotated coordinate)
  if (dy_ > -radius && posx > g.x1 && posx < g.x2){
    dy_ = -radius;
    vely_ = -0.6*vely_;  
  }

    // rotate everything back to restore the original 
    // coordinate axis.
    dx = cosine * dx_ - sine * dy_;
    dy = cosine * dy_ + sine * dx_;
    velx = cosine * velx_ - sine * vely_;
    vely = cosine * vely_ + sine * velx_;
    posx = g.x + dx;
    posy = g.y + dy;

}
  
  
  
}
