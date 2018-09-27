// Ball Bounce Off An Angle
// Adapted from Keith Peters' Algorithm 
// from his book Foundation Actionscript 3.0 Animation: Making Things Move

Ball b;

int segments = 20;
Ground[] ground = new Ground[segments];


void setup(){
  size(800,600);
  b = new Ball(random(50,100), 60, 10);
  // center of segment = midpoint of (0,400) and (width, height)
  float[] peakHeights = new float[segments+1];
  for (int i=0; i<peakHeights.length; i++){
    peakHeights[i] = random(height-60, height-20);
  }

  /* Float value required for segment width (segs)
   calculations so the ground spans the entire 
   display window, regardless of segment number. */
  float segs = segments;
  for (int i=0; i<segments; i++){
    ground[i]  = new Ground(width/segs*i, peakHeights[i], width/segs*(i+1), peakHeights[i+1]);
  }  

}
  
void draw(){
  background(255);
  // fill and draw triangle(inclined ramp): (0,400), (width,height), (0, height)
  b.display();
  b.move();
  b.checkWallsCollision();  
  for (int i=0; i<segments; i++){
    b.checkInclineCollision(ground[i]);
  }
  fill(255,0,0);
  beginShape();
  for (int i=0; i<segments; i++){
    vertex(ground[i].x1, ground[i].y1);
    vertex(ground[i].x2, ground[i].y2);
  }
  vertex(ground[segments-1].x2, height);
  vertex(ground[0].x1, height);
  endShape(CLOSE);
  
  textSize(32);
  textAlign(CENTER);
  text("Press SPACE to reset.", width/2, 100);
  
}

void keyPressed(){
  if(key == ' '){
    setup();
    
  }
  
}
