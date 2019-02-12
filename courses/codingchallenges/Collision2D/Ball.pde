class Ball{
  float x,y,radius;
  float vx, vy, mass;
  Ball(float x_, float y_, float radius_){
    // initialize x, y and radius
    
    
    // randomize vx, xy
    
    
    // set mass to be proportional to radius
    // for example mass = radius/2.
    
    
  }  
  void display(){
    fill(255,0,0);
    ellipse(x,y,2*radius,2*radius);
  }
  void move(){
    x += vx;
    y += vy;
    if(x > width - radius){
      x = width - radius;
      vx = -vx; 
    }
    if(x < radius){
      x = radius;
      vx = -vx;
    }
    if(y > height - radius){
      y = height - radius;
      vy = -vy; 
    }
    if(y < radius){
      y = radius;
      vy = -vy; 
    } 
  }
}
