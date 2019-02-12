Ball b1, b2;

void setup(){
  size(800,600);
  // initialize ball objects
  
  
}

void draw(){
  background(255);
  
}

void collision(Ball b1, Ball b2){
  // calculate distance between balls
  float dx = 
  float dy = 
  float dist = 
  // if distance is within sum of radii(collide)
  if(      ){
    
    // find angle between balls
    // compute sine and cosine of angle
    float angle = 
    float sin = 
    float cos = 
    
    // rotate velocity
    float vx1 = 
    float vy1 =
    float vx2 = 
    float vy2 =
    
    //resolve 1D velocity, use temp variables
    float vx1final =
    float vx2final = 
    
    // update velocity
    vx1 = 
    vx2 =
    
    //rotate vel back
    b1.vx = 
    b1.vy = 
    b2.vx = 
    b2.vy = 

    }
 
}
