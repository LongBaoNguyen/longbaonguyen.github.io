// Stopwatch program
// Fill in the code below to implement the Stopwatch program
// that keep track of the time elapsed since the start of program.


int hrs, mins;
float secs; // including fractional part

String timestr = "";
void setup(){
  // set size of window
 
}

// default frame rate for draw() 
// is 60 times a second.
void draw(){
  background(255);
  // frameCount is the current number of frames
  // 60*60*60 is the number of frames in an hour.
  hrs =     // fill in code here. 
  
  // framesLeft is number of frames after
  // taking into account the number of hrs. 
  int framesLeft =    // fill in code here.
  
  // 60*60 is the number of frames in a minute.
  mins =    // fill in code here.
  
  
  // framesLeft is now the number of frames after
  // already taking account hrs and mins.
  framesLeft = // fill in code here.
  
  // now compute secs(float) including fractional part.
  secs = // fill in code here.
  
  // seconds is a String that represent secs
  // accurate to two decimal places.
  String seconds = String.format("%.2f", secs);
  
  // timestr concatenate in the total time elapsed
  // in the form hrs:mins:seconds
  timestr = // fill in code here.
  
  
  // use fill(r,g,b) to set color
  // use textSize(int) for font size
  // use text(String, int, int) to display
  // the time string, timestr, on the screen.
  // you may optionally use textAlign(CENTER) to align your text.
  // fill in code below.
  
  
}
