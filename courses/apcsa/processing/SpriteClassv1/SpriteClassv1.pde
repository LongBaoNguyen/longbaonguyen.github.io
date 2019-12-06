/* In this lab, we will implement the Sprite class which will become
   an essential class to writing arcade games like Zelda or Super Mario.
   
   First implement the Sprite class by following the comments.
   The implement setup() and draw() below to create a Sprite object and moves it around on the
   screen using the keyboard as we have done in the previous lab. 
   Use the "character.png" file in the data folder included in this zip folder.
   Add code so that your Sprite should never be able to leave the screen.
*/



// declare a Sprite object, call it player.


void setup(){
  size(800, 600);
  imageMode(CENTER);
  // initialize Sprite object using one of the constructors
  // set the sprite to be in the middle of the screen.
  // TRY DIFFERENT SCALING AND MAKE SURE THIS WORKS!
  


}

void draw(){
  background(255);
  // call update and display on the player object to update and display the Sprite

  
  
  // add logic here so that the Sprite never leaves the screen.
  // Hint: Use conditional and the setLeft, setRight...etc methods
  // if your character glitches at the screen edge, you didn't do it correctly.
  
  
  
  
}

// implement keyPressed so that pressing the arrow keys will move the Sprite
// this is the same as the previous lab with some minor changes.
void keyPressed(){
    
}

void keyReleased(){
    
}
