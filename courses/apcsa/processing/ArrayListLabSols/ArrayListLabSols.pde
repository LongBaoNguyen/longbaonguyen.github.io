//declare an arrayList of Ball objects
ArrayList<Ball> list;
void setup(){
  size(800,600);
  //initialize arraylist.
  list = new ArrayList<Ball>();
  
  // populate list with 30 Ball objects
  for(int i = 0; i < 30; i++){
      list.add(new Ball(color(255,0,0)));   
    } 
}

void draw(){
  background(255);
  
  // display and move all the objects
  // if the mouse is inside a Ball object 
  // remove it from list
  for(int i=list.size()-1; i>=0; i--){
    Ball current = list.get(i);
    current.display();
    current.update();
    if(distanceToMouse(current)<=current.radius)
      list.remove(i);
    
  }
}

// returns distance of a Ball to the mouse
public float distanceToMouse(Ball a){
  float dx = a.x - mouseX;
  float dy = a.y - mouseY;
  float distance = sqrt(dx*dx+dy*dy);
  return distance; 
}
