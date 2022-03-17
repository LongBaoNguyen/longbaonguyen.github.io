public class AnimatedSprite extends Sprite{
  PImage[] currentImages;
  PImage[] standNeutral;
  PImage[] moveLeft;
  PImage[] moveRight;
  int direction;
  int index;
  int frame;
  // implement the constructor, remember to call super() appropriately.
  // initialize direction, index and frame. The PImage arrays can be initialized
  // as null. 
  public AnimatedSprite(PImage img, float scale){
    // TODO: fill in one line of code

    
    direction = NEUTRAL_FACING;
    index = 0;
    frame = 0;
  }
  public void updateAnimation(){
  // TODO:
  // frame is increased by 1
  // every 5 frames do:
  //    call selectionDirection
  //    call selectCurrentImages
  //    call advanceToNextImage
  
  
  
  
  
  
  }
  // if sprite is moving right, set direction to RIGHT_FACING
  // else if it is moving left, set direction to LEFT_FACING
  // otherwise set it to NEUTRAL_FACING
  public void selectDirection(){
    if(change_x > 0)
      direction = RIGHT_FACING;
    else if(change_x < 0)
      direction = LEFT_FACING;    
    else
      direction = NEUTRAL_FACING;  
  }

  // if direction is RIGHT_FACING, LEFT_FACING or NEUTRAL_FACING
  // set currentImages to the appropriate PImage array. 
  public void selectCurrentImages(){
    if(direction == RIGHT_FACING)
      currentImages = moveRight;
    else if(direction == LEFT_FACING)
      currentImages = moveLeft;
    else
      currentImages = standNeutral;
  }
  public void advanceToNextImage(){
    // TODO:
    // increase index by 1
    // if index is at end of array loop back to 0
    // assign image variable(from Sprite class) to currentImages at index.

    
    
  }
}
