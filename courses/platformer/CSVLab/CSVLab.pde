/* CSV Lab
   This is NOT a coding lab. 
   Study the code below. Make sure you understand how the code reads in
   a csv file and create a game/stage map.
   The code is from the tutorial: https://youtu.be/RhD6bzSHBeI
   
   Do the following:
   1) Modify the "map.csv" file and design a Platformer stage map with all of the tiles given
   in the data folder.
   2) Assume the Sprite scale where tiles are 50 x 50, modify the csv file to match
   the exact dimensions of the window(800 x 600). Since we haven't done scrolling, we can't
   see tiles outside of this range. 
*/


final static float MOVE_SPEED = 5;
final static float SPRITE_SCALE = 50.0/128;
final static float SPRITE_SIZE = 50;


//declare global variables
Sprite p;
PImage snow, crate, red_brick, brown_brick;
ArrayList<Sprite> platforms;


//initialize them in setup().
void setup(){
  size(800, 600);
  imageMode(CENTER);
  p = new Sprite("player.png", 1.0, 100, 300);
  p.change_x = 0;
  p.change_y = 0;
  platforms = new ArrayList<Sprite>();
  red_brick = loadImage("red_brick.png");
  brown_brick = loadImage("brown_brick.png");
  crate = loadImage("crate.png");
  snow = loadImage("snow.png");
  createPlatforms("map.csv");
}

// modify and update them in draw().
void draw(){
  background(255);
  
  p.display();
  p.update();
  
  for(Sprite s: platforms)
    s.display();
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

// called whenever a key is pressed.
void keyPressed(){
  if(keyCode == RIGHT){
    p.change_x = MOVE_SPEED;
  }
  else if(keyCode == LEFT){
    p.change_x = -MOVE_SPEED;
  }
  else if(keyCode == UP){
    p.change_y = -MOVE_SPEED;
  }
  else if(keyCode == DOWN){
    p.change_y = MOVE_SPEED;
  }
}

// called whenever a key is released.
void keyReleased(){
  if(keyCode == RIGHT){
    p.change_x = 0;
  }
  else if(keyCode == LEFT){
    p.change_x = 0;
  }
  else if(keyCode == UP){
    p.change_y = 0;
  }
  else if(keyCode == DOWN){
    p.change_y = 0;
  }
}
