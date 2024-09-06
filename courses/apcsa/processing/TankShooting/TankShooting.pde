/* Tank Shooting Lab
  
  A tank can move around on the screen. Crates are placed randomly on the screen.
  Tank shoots bullets when mouse is clicked. If a bullet hits a crate, both are removed
  from their respective arraylists. Bullets are also removed from arraylist if they leave screen. 
    
  Create an arraylist of 10 randomly placed crates. 
  
  If a bullet collide with a crate, add 1 to score and remove the bullet and the 
  their arraylists. Display the score on the screen.
  
  
  1) Initialize score, crates and p_bullets in setup.
  2) Implement mouseClicked() method to get the tank to shoot.
  3) Implement draw() as instructed by the comments.
  
 
*/

Sprite player;
ArrayList<Sprite> crates;
ArrayList<Sprite> p_bullets; // player bullets
int score;

// useful constants
final float CHARACTER_SCALE = 0.8;
final float BULLET_SCALE = 0.7;
final float CRATE_SCALE = 0.5;
final int BULLET_SPEED = 10;
final int NUM_OF_CRATES = 10;

void setup(){
  size(1024, 768);
  imageMode(CENTER);
  
  player = new Sprite("tank.png", CHARACTER_SCALE);
  
  // initialize score. Initialize crates and p_bullets to empty arraylists.



  
/* for loop to create crate Sprite placed randomly on the screen
   use Math.random() and then case to a float(do not use random() from Processing)
   add each crate to the arraylist. Since we have already done this with the
   previous Collect Coins lab, this part is given to you.
*/
  for(int i = 1; i <= NUM_OF_CRATES; i++){
    float x = (float)(Math.random()*width);
    float y = (float)(Math.random()*height);
    Sprite crate = new Sprite("crate.png", CRATE_SCALE, x, y);
    crates.add(crate);
  }
  
  
}

void draw(){
  background(255);
  player.display();
  player.update();
 
  // display crates, USE FOR EACH

  
  
  /* use regular for loop to display and update bullets
     for i from size() - 1 to 0:
       get the current bullet
       display and update it.
       call checkForCollisionWithList with current bullet and arraylist of crates
       which returns an arraylist of crates that collide with this current bullet(store this arraylist
       in variable called collision_list)
       if collision list is not empty:
          remove bullet from p_bullets BY INDEX
          remove the first crate from collision_list from crates arraylist(must remove BY OBJECT
          since we don't know the index of the first crate in collision_list 
          is in the crates arraylist)
          update score by adding 1. 
       if bullet leaves the screen, remove bullet.
  */
  






  
  // display score
  // use fill(r,g,b), textSize(size) and text(str, x, y) 
  


}

/*
  mouseClicked is called automatically whenever the mouse is clicked.
  Create a bullet sprite, initialize its position and set its change_x 
  attribute to BULLET_SPEED. Add to p_bullets arraylist. 
*/
void mouseClicked(){

  
}

void keyPressed(){
  if(keyCode == RIGHT)
    player.change_x = 5;
  else if(keyCode == LEFT)
    player.change_x = -5;
  else if(keyCode == UP)
    player.change_y = -5;
  else if(keyCode == DOWN)
    player.change_y = 5;
}

void keyReleased(){
  if(keyCode == RIGHT)
    player.change_x = 0;
  else if(keyCode == LEFT)
    player.change_x = 0;
  else if(keyCode == UP)
    player.change_y = 0;
  else if(keyCode == DOWN)
    player.change_y = 0;
    
}
