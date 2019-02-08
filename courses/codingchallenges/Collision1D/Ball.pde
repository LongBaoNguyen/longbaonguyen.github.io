class Ball{
  float x,y,radius;
  float vx, mass;
  // write a constructor with input paramters
  // do not randomize!
  // mass should be a function of radius
   
   
  void display(){
    fill(255,0,0);
    ellipse(x,y,2*radius,2*radius);
  }
  void move(){
    x += vx;
    if(x > width - radius){
      x = width - radius;
      vx = -vx; 
    }
    if(x < radius){
      x = radius;
      vx = -vx;
    }
    
  }
}
