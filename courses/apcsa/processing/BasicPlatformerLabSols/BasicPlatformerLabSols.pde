/*
  Basic Platformer Lab:
  
  Add gravity and resolve platform collisions. Add jumping ability to the player. 
  
  Complete the code as indicated by the comments.
  Do the following:
  1) Implement resolvePlatformCollisions.
  2) Implement the isOnPlatforms method.
  3) Implement the keyPressed method so that if user presses 'a', player jumps.
  See the comments below for more details. 
  4) Add a few lines of code in draw() to make everything works. 
  
  For more detail, see the tutorials: 
  Slides:
  
  
  Videos:
  Resolving Platform Collisions Part 1: https://youtu.be/nFOlo6F60FA
  Resolving Platform Collisions Part 2: https://youtu.be/kZYIuI7BLZY
  Add Jumping to Player: https://youtu.be/LaftkH8bs9c


 
*/

final static float MOVE_SPEED = 4;
final static float SPRITE_SCALE = 50.0/128;
final static float SPRITE_SIZE = 50;
final static float GRAVITY = .6;
final static float JUMP_SPEED = 14; 

final static float RIGHT_MARGIN = 400;
final static float LEFT_MARGIN = 60;
final static float VERTICAL_MARGIN = 40;


//declare global variables
Sprite player;
PImage snow, crate, red_brick, brown_brick;
ArrayList<Sprite> platforms;

//initialize them in setup().
void setup(){
  size(800, 600);
  imageMode(CENTER);
  player = new Sprite("player.png", 0.8);
  player.center_x = 500;
  player.center_y = 100;
  
  // arraylist of bricks
  platforms = new ArrayList<Sprite>();
 
 
  red_brick = loadImage("red_brick.png");
  brown_brick = loadImage("brown_brick.png");
  crate = loadImage("crate.png");
  snow = loadImage("snow.png");
  
  // create 2d map of bricks from csv file(you can edit this to change the map)
  createPlatforms("map.csv");
}

// modify and update them in draw().
void draw(){
  background(255);
  
  player.display();
  
  // call resolvePlatformCollisions
  resolvePlatformCollisions(player, platforms);
  
  // display platforms arraylist(for each loop)
  for(Sprite s: platforms)
    s.display();

} 


/* Implement this method. Resolve collision between sprite and arraylist of bricks
*/
public void resolvePlatformCollisions(Sprite s, ArrayList<Sprite> walls){
  // add gravity to change_y of sprite
  s.change_y += GRAVITY;
  
  // move in y-direction by adding change_y to center_y to update y position.
  s.center_y += s.change_y;
  
  // Now resolve any collision in the y-direction:
  // compute collision_list between sprite and walls(platforms) by calling
  // checkCollisionList and storing the returned arraylist in collision_list
  ArrayList<Sprite> col_list = checkCollisionList(s, walls);
  
  /* if collision_list is nonempty:
       get the first platform from collision list
       if sprite is moving down(change_y > 0)
         set bottom of sprite to equal top of platform
       else if sprite is moving up
         set top of sprite to equal bottom of platform
       set sprite's change_y to 0
  */
  if(col_list.size() > 0){
    Sprite collided = col_list.get(0);
    if(s.change_y > 0){
      s.setBottom(collided.getTop());
    }
    else if(s.change_y < 0){
      s.setTop(collided.getBottom());
    }
    s.change_y = 0;
  }

  // move in x-direction by adding change_x to center_x to update x position.
  s.center_x += s.change_x;
  
  // Now resolve any collision in the x-direction:
  // compute collision_list between sprite and walls(platforms) by calling
  // checkCollisionList and storing the returned arraylist in collision_list
  col_list = checkCollisionList(s, walls);

  /* if collision list is nonempty:
       get the first platform from collision list
       if sprite is moving right
         set right side of sprite to equal left side of platform
       else if sprite is moving left
         set left side of sprite to equal right side of platform
  */

  if(col_list.size() > 0){
    Sprite collided = col_list.get(0);
    if(s.change_x > 0){
        s.setRight(collided.getLeft());
    }
    else if(s.change_x < 0){
        s.setLeft(collided.getRight());
    }
  }  
}

// Implement this method
// returns true if sprite is one a platform.
public boolean isOnPlatforms(Sprite s, ArrayList<Sprite> walls){
  // move down say 5 pixels
  s.center_y += 5;

  // check to see if sprite collide with any walls by calling
  // checkCollisionList and storing the returned arraylist in collision_list
  ArrayList<Sprite> col_list = checkCollisionList(s, walls);
  
  // move back up 5 pixels to restore sprite to original position.
  s.center_y -= 5;

  // if sprite did collide with walls(length of collision list > 0)
  // it must have been on a platform: return true
  // otherwise return false.
  return col_list.size() > 0;
}


// called whenever a key is pressed.
// add in else if block:
// if key pressed is 'a' and player is on platform, jump.
void keyPressed(){
  if(keyCode == RIGHT){
    player.change_x = MOVE_SPEED;
  }
  else if(keyCode == LEFT){
    player.change_x = -MOVE_SPEED;
  }
  else if(key == 'a' && isOnPlatforms(player, platforms)){
      player.change_y = -JUMP_SPEED;
  }
}

// called whenever a key is released.
void keyReleased(){
  if(keyCode == RIGHT){
    player.change_x = 0;
  }
  else if(keyCode == LEFT){
    player.change_x = 0;
  }
}

/*
DO NOT MODIFY CODE BELOW THIS POINT
*/

boolean checkCollision(Sprite s1, Sprite s2){
  boolean noXOverlap = s1.getRight() <= s2.getLeft() || s1.getLeft() >= s2.getRight();
  boolean noYOverlap = s1.getBottom() <= s2.getTop() || s1.getTop() >= s2.getBottom();
  if(noXOverlap || noYOverlap){
    return false;
  }
  else{
    return true;
  }
}

public ArrayList<Sprite> checkCollisionList(Sprite s, ArrayList<Sprite> list){
  ArrayList<Sprite> collision_list = new ArrayList<Sprite>();
  for(Sprite p: list){
    if(checkCollision(s, p))
      collision_list.add(p);
  }
  return collision_list;
}


void createPlatforms(String filename){
  String[] lines = loadStrings(filename);
  for(int row = 0; row < lines.length; row++){
    String[] values = split(lines[row], ",");
    for(int col = 0; col < values.length; col++){
      if(values[col].equals("1")){
        Sprite s = new Sprite(red_brick, SPRITE_SCALE);
        s.center_x = SPRITE_SIZE/2 + col * SPRITE_SIZE;
        s.center_y = SPRITE_SIZE/2 + row * SPRITE_SIZE;
        platforms.add(s);
      }
      else if(values[col].equals("2")){
        Sprite s = new Sprite(snow, SPRITE_SCALE);
        s.center_x = SPRITE_SIZE/2 + col * SPRITE_SIZE;
        s.center_y = SPRITE_SIZE/2 + row * SPRITE_SIZE;
        platforms.add(s);
      }
      else if(values[col].equals("3")){
        Sprite s = new Sprite(brown_brick, SPRITE_SCALE);
        s.center_x = SPRITE_SIZE/2 + col * SPRITE_SIZE;
        s.center_y = SPRITE_SIZE/2 + row * SPRITE_SIZE;
        platforms.add(s);
      }
      else if(values[col].equals("4")){
        Sprite s = new Sprite(crate, SPRITE_SCALE);
        s.center_x = SPRITE_SIZE/2 + col * SPRITE_SIZE;
        s.center_y = SPRITE_SIZE/2 + row * SPRITE_SIZE;
        platforms.add(s);
      }
    }
  }
}
 
