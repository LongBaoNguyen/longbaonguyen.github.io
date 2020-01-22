Ball[] b;

void setup(){
  size(600,600);
  // initialize and populate b array.
  // all ball objects have the same color
  
  color c = color(255, 0, 255);
  b = new Ball[20];
  
  for(int i = 0; i < b.length; i++)
    b[i] = new Ball(c);
  
}

void draw(){
  background(255);
  // draw, update and bounce balls
  for(int i = 0; i < b.length; i++){
    b[i].display();
    b[i].update();
  }
   
  // call largest and set its color to a different color
  // than the other ball objects
}

// returns Ball that has the largest radius
// return the first one if there are multiples. 
public Ball largest(Ball[] balls)
{
  return null;
  
}
